#!/usr/bin/env python3
"""
Post-process docs/book/print.html before WeasyPrint converts it to PDF.

Делает несколько правок, которые сложно или неудобно делать на уровне
markdown / mdBook:

  1. Помечает «языковой переключатель» (<p><a>English</a> | <strong>Русский</strong></p>)
     классом ``lang-switcher`` — CSS прячет его при печати.
  2. Помечает короткие «истории-связки» классом ``story-bridge``, чтобы они
     рендерились компактной врезкой, а не занимали целую полосу.
  3. Оборачивает первую главу — Введение и Настройку окружения — так,
     чтобы заголовки и колонтитулы вели себя корректно.

Скрипт идемпотентен: повторный запуск не ломает уже обработанный файл.

Использование:
    python3 scripts/postprocess-print-html.py docs/book/print.html
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path


# Заголовки коротких историй-мостиков (по факту с сайта). Если по такому
# заголовку ничего не найдено — просто пропускаем (идемпотентно).
STORY_BRIDGE_HEADINGS = [
    "Первая рабочая встреча Боба",
    "Первый рабочий день Боба",
    "История: WAR",
    "История: отставание от графика",
    "История: инцидент безопасности",
    "История: сетевой инцидент",
    "История: работа сверхурочно",
    "История: демонстрация под угрозой",
    "Где находится моё хранилище?",
    "Статусная встреча проекта",
    "Финал",
    "Возврат к Бобу",
]


LANG_SWITCHER_RE = re.compile(
    r'(<div[^>]*break-before:\s*page[^>]*></div>)\s*'
    r'(<p>\s*<a[^>]*>English</a>\s*\|\s*<strong>Русский</strong>\s*</p>)',
    re.IGNORECASE,
)

# Резервный паттерн — на случай, если переключатель идёт без div-разрыва
# (например, у самой первой главы или у вложенных подразделов).
LANG_SWITCHER_STANDALONE_RE = re.compile(
    r'<p>\s*<a[^>]*>English</a>\s*\|\s*<strong>Русский</strong>\s*</p>',
    re.IGNORECASE,
)


def mark_lang_switcher(html: str) -> tuple[str, int]:
    """Пометить классом lang-switcher все языковые переключатели."""

    count = 0

    def repl(match: re.Match) -> str:
        nonlocal count
        count += 1
        page_break, paragraph = match.group(1), match.group(2)
        # Добавим class="lang-switcher", если его ещё нет
        if 'class="lang-switcher"' in paragraph:
            return match.group(0)
        paragraph = paragraph.replace('<p>', '<p class="lang-switcher">', 1)
        return f'{page_break}\n{paragraph}'

    html = LANG_SWITCHER_RE.sub(repl, html)

    def repl_standalone(match: re.Match) -> str:
        nonlocal count
        para = match.group(0)
        if 'class="lang-switcher"' in para:
            return para
        count += 1
        return para.replace('<p>', '<p class="lang-switcher">', 1)

    html = LANG_SWITCHER_STANDALONE_RE.sub(repl_standalone, html)
    return html, count


def fix_toc_anchors(html: str) -> tuple[str, int]:
    """Снять путь-префикс с внутристраничных ссылок оглавления.

    mdBook при сборке print.html переписывает сырые HTML-ссылки
    ``<a href="#X">`` в ``<a href="00-Frontmatter/04-TOC.ru.html#X">``
    (резолвит относительно исходной страницы). В объединённом документе
    такого «файла-якоря» нет, и WeasyPrint не может посчитать номер
    страницы через target-counter. Возвращаем ссылки к виду ``#X``,
    чтобы они указывали на реальные id заголовков.

    Префикс ищем динамически — это путь к самому файлу оглавления,
    поэтому правка не зависит от его конкретного имени.
    """

    # Находим все префиксы вида "<путь>/<что-то>-TOC.ru.html#"
    prefixes = set(
        re.findall(r'href="([^"#]*TOC\.ru\.html)#', html, re.IGNORECASE)
    )
    count = 0
    for prefix in prefixes:
        before = html
        html = html.replace(f'href="{prefix}#', 'href="#')
        count += before.count(f'href="{prefix}#')
    return html, count


def wrap_story_bridges(html: str) -> tuple[str, int]:
    """Найти короткие истории-мостики и обернуть их в <section class="story-bridge">.

    Эвристика:
      • заголовок <h1 id="...">Текст</h1>, где Текст входит в STORY_BRIDGE_HEADINGS;
      • от заголовка и до следующего <h1 ...> (или конца) — это содержимое истории;
      • если содержимое короткое (< ~1500 символов чистого текста), оборачиваем.
    """

    count = 0

    # Сначала найдём все позиции <h1>, чтобы потом ходить по парам.
    h1_re = re.compile(
        r'<h1[^>]*id="([^"]+)"[^>]*>(?:<a[^>]*>)?([^<]+)(?:</a>)?</h1>',
        re.IGNORECASE,
    )

    pieces: list[str] = []
    last_end = 0
    matches = list(h1_re.finditer(html))

    for i, m in enumerate(matches):
        heading_text = m.group(2).strip()
        start = m.start()
        end = matches[i + 1].start() if i + 1 < len(matches) else len(html)

        # Кусок до этого заголовка — оставляем как есть
        pieces.append(html[last_end:start])

        chunk = html[start:end]
        is_bridge = heading_text in STORY_BRIDGE_HEADINGS

        # Идемпотентность: если непосредственно перед этим H1 в исходном
        # HTML уже стоит открывающий <section class="story-bridge">,
        # значит история уже обёрнута — пропускаем, чтобы не вкладывать
        # секции друг в друга при повторном прогоне.
        window = html[max(0, start - 80):start]
        already_wrapped = '<section class="story-bridge">' in window

        if is_bridge and not already_wrapped:
            # Длина «чистого» текста для проверки, что это короткая история
            text_only = re.sub(r'<[^>]+>', '', chunk)
            if len(text_only.strip()) < 1500:
                # В конце chunk оказывается page-break-div, который mdBook
                # вставил перед СЛЕДУЮЩЕЙ главой. Его нельзя оставлять внутри
                # секции — иначе серый фон истории растянется до разрыва на
                # всю страницу. Выносим этот разрыв за пределы </section>.
                trailing_break = ''
                m_break = re.search(
                    r'(<div[^>]*break-before:\s*page[^>]*></div>\s*)$', chunk
                )
                if m_break:
                    trailing_break = m_break.group(1)
                    chunk = chunk[: m_break.start()]
                pieces.append(
                    f'<section class="story-bridge">\n{chunk}\n</section>\n'
                    f'{trailing_break}'
                )
                count += 1
            else:
                pieces.append(chunk)
        else:
            pieces.append(chunk)

        last_end = end

    pieces.append(html[last_end:])
    return ''.join(pieces), count


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        'print_html',
        nargs='?',
        default='docs/book/print.html',
        help='путь к print.html (по умолчанию docs/book/print.html)',
    )
    parser.add_argument(
        '--check',
        action='store_true',
        help='только проверить, без записи',
    )
    args = parser.parse_args()

    path = Path(args.print_html)
    if not path.exists():
        print(f'error: {path} не найден', file=sys.stderr)
        return 1

    html = path.read_text(encoding='utf-8')
    original = html

    html, switchers = mark_lang_switcher(html)
    html, bridges = wrap_story_bridges(html)
    html, toc_fixed = fix_toc_anchors(html)

    if html == original:
        print('postprocess: изменений нет (файл уже обработан или нет совпадений)')
        return 0

    if args.check:
        print(
            f'postprocess (check): найдено {switchers} язык. переключателей, '
            f'{bridges} историй-связок, {toc_fixed} ссылок оглавления'
        )
        return 0

    path.write_text(html, encoding='utf-8')
    print(
        f'postprocess: {path} — помечено {switchers} язык. переключателей, '
        f'обёрнуто {bridges} историй-связок, исправлено {toc_fixed} ссылок оглавления'
    )
    return 0


if __name__ == '__main__':
    sys.exit(main())
