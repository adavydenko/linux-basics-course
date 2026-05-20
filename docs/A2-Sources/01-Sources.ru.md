# Источники и рекомендуемая литература

Список открытых ресурсов, к которым стоит обращаться при изучении Linux. Все ссылки на момент составления пособия (2026 г.) ведут на бесплатные публичные материалы. Они не цитируются в основном тексте напрямую — это дополнительный круг чтения, если конкретная тема вас зацепила и хочется глубже.

## Документация в самой системе

С Linux всегда поставляется его лучшая и самая точная документация. Перед поиском в интернете заглядывайте сначала сюда — часто этого достаточно:

**`man`** — справочные страницы. `man bash`, `man 5 fstab`, `man ssh_config`. Номер раздела (1 — команды, 5 — форматы файлов, 8 — администрирование) помогает попасть точно в нужную статью.

**`info`** — расширенный формат справки от GNU. Для команд из coreutils часто полнее, чем `man`: `info coreutils 'cp invocation'`.

**`--help`** — короткая справка к самой команде. Подходит, чтобы быстро вспомнить опции.

**`/usr/share/doc/`** — пакетные документации, файлы `README`, `NEWS`, примеры конфигов.

## Документация ядра и подсистем

**kernel.org** — официальный сайт ядра Linux. Документация — https://www.kernel.org/doc/html/latest/

**The Linux Kernel Archives — admin guide** — https://docs.kernel.org/admin-guide/

**Linux man-pages project** — https://man7.org/linux/man-pages/ — те же `man`-страницы в удобном веб-виде, всегда актуальная версия.

## Документация дистрибутивов

**Ubuntu Server Guide** — https://documentation.ubuntu.com/server/

**Debian Reference / Wiki** — https://wiki.debian.org/ и https://www.debian.org/doc/

**Red Hat / RHEL documentation** — https://docs.redhat.com/en/documentation/red_hat_enterprise_linux

**Fedora Documentation** — https://docs.fedoraproject.org/en-US/docs/

**Arch Wiki** — https://wiki.archlinux.org/ — несмотря на привязку к Arch, считается одной из лучших общих документаций по Linux. Многие статьи (про systemd, networking, GRUB) применимы к любому дистрибутиву.

**Gentoo Wiki** — https://wiki.gentoo.org/ — глубокие технические статьи, особенно по сборке ядра и init-системам.

## Сетевые протоколы и стандарты

**IETF Datatracker (RFC)** — https://datatracker.ietf.org/ — первоисточник стандартов. Полезные RFC:

- RFC 1034, 1035 — DNS;
- RFC 4253 — SSH Transport Layer Protocol;
- RFC 791, 793 — IP, TCP;
- RFC 8200 — IPv6;
- RFC 9110, 9111 — HTTP/1.1.

**iana.org** — реестр зарегистрированных портов, ASN, доменов верхнего уровня. https://www.iana.org/assignments/

## Утилиты: официальные сайты и репозитории

- **systemd** — https://systemd.io/ и `man 7 systemd.unit`, `man 5 systemd.service`, `man 7 systemd.timer`;
- **iproute2** — https://wiki.linuxfoundation.org/networking/iproute2;
- **nftables** — https://wiki.nftables.org/;
- **iptables** — https://www.netfilter.org/projects/iptables/;
- **OpenSSH** — https://www.openssh.com/manual.html;
- **GNU Bash Reference Manual** — https://www.gnu.org/software/bash/manual/;
- **GNU Coreutils Manual** — https://www.gnu.org/software/coreutils/manual/;
- **GNU sed Manual** — https://www.gnu.org/software/sed/manual/;
- **GNU Awk User's Guide** — https://www.gnu.org/software/gawk/manual/;
- **Vim documentation** — https://vimhelp.org/ (актуально и для классического `vi`);
- **Docker docs** — https://docs.docker.com/;
- **Git Book** — https://git-scm.com/book/ru/v2 (есть русский перевод);
- **Python venv** — https://docs.python.org/3/library/venv.html.

## Учебники и сборники

**The Linux Documentation Project (TLDP)** — https://tldp.org/ — большая база свободных руководств. Часть устарела, но «Bash Beginners Guide», «Advanced Bash-Scripting Guide», «Linux System Administrator's Guide» по-прежнему полезны.

**Beej's Guide to Unix IPC, Network Programming** — https://beej.us/guide/ — мягкое введение в системное программирование Unix.

**Filesystem Hierarchy Standard (FHS)** — https://refspecs.linuxfoundation.org/fhs.shtml — официальное описание назначения каталогов корня.

**LVM HOWTO** — https://tldp.org/HOWTO/LVM-HOWTO/ — подробное руководство по LVM.

**Linux From Scratch** — https://www.linuxfromscratch.org/ — для понимания, как Linux устроен изнутри: каждый компонент собирается вручную.

## Регулярные выражения

**`man 7 regex`** — стандарт POSIX regex прямо в системе.

**regex101.com** — https://regex101.com/ — интерактивный отладчик регулярных выражений с подсветкой.

**Mastering Regular Expressions, 3rd ed., Jeffrey Friedl** — классическая книга про регэкспы. Платная, но полнота и глубина того стоят.

## Безопасность

**SSH key best practices** — https://infosec.mozilla.org/guidelines/openssh

**OWASP Cheat Sheets** — https://cheatsheetseries.owasp.org/ — короткие практические рекомендации по безопасности; для Linux актуальны блоки про SSH, TLS, аутентификацию.

**CIS Benchmarks** — https://www.cisecurity.org/cis-benchmarks/ — отраслевые контрольные списки безопасной настройки систем (Ubuntu, RHEL, и т.п.). Регистрация бесплатная.

## Русскоязычные ресурсы

**Хабр, потоки «Системное администрирование», «*nix», «Linux для всех»** — https://habr.com/ru/hubs/ — статьи разного уровня и качества; на старте курса полезно отлавливать там обзорные тексты.

**Lib.ru: Linux** — https://lib.ru/UNIXFAQ/ — архив переведённых руководств и HOWTO; часть устарела, но базовые тексты по `tar`, `find`, `awk` читаемы и сегодня.

**OpenNet.ru** — https://www.opennet.ru/man.shtml — русскоязычные `man`-страницы и новости open-source. Особенно удобно, если в системе нет русифицированного `man`.

**Wiki ALT Linux** — https://www.altlinux.org/Wiki/Main_Page — статьи на русском, многое применимо к Debian/Ubuntu.

**Курсы Stepik «Введение в Linux», «Bash scripting»** — https://stepik.org/ (бесплатные форматы существуют, проверяйте актуальный список курсов).

**OTUS, курсы «Администратор Linux», «DevOps»** — https://otus.ru/ — частично бесплатные открытые уроки; пересматривать по темам, которые в пособии даны коротко.

**Wiki ArchLinux на русском** — https://wiki.archlinux.org/title/Main_page_(Русский) — частичный перевод оригинала, рабочее качество.

## Книги (англоязычные классики)

Эти книги переиздаются регулярно; смысл — самые свежие издания.

- **Brian Ward. How Linux Works, 3rd ed. (2021)** — мягкое и одновременно глубокое введение в устройство Linux. Лучшая книга для перехода от «знаю команды» к «понимаю систему».
- **Mark Bates et al. The Linux Command Line, 2nd ed., William Shotts** — бесплатно доступна на https://linuxcommand.org/tlcl.php; разбор оболочки и базовых команд от первых шагов до скриптинга.
- **Carla Schroder. The Linux Cookbook** — рецепт-ориентированная книга: маленькие задачи и проверенные решения.
- **Evi Nemeth et al. UNIX and Linux System Administration Handbook, 5th ed.** — увесистый системный администраторский справочник.
- **Jeffrey Friedl. Mastering Regular Expressions** — см. выше.
- **Daniel J. Barrett. Linux Pocket Guide** — карманный справочник по командам; удобно держать рядом с клавиатурой.

## Что читать в первую очередь после курса

Если выбирать один источник на каждую тему, чтобы продолжить изучение, мой короткий список:

- общая картина — Brian Ward, *How Linux Works*;
- оболочка и скрипты — William Shotts, *The Linux Command Line*;
- systemd — `man 7 systemd.unit` + статьи Arch Wiki по systemd;
- сеть — Arch Wiki «Network configuration», `man 5 systemd.network`, RFC 1034/1035 для DNS;
- безопасность — Mozilla OpenSSH guidelines + CIS Benchmark для своего дистрибутива;
- регулярные выражения — Friedl + regex101 для отладки.

Этого набора хватит, чтобы за несколько месяцев перейти от «прошёл базовый курс» до «уверенно решает реальные задачи».
