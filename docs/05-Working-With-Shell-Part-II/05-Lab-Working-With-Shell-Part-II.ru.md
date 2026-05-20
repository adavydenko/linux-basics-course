[English](05-Lab-Working-With-Shell-Part-II.md) | **Русский**
# Лабораторная работа: командная строка, часть II

- [Доп. лабораторная](https://kodekloud.com/topic/lab-working-with-shell-ii/)

## Цели лабораторной работы

После выполнения работы студент должен уметь:

- создавать сжатые архивы;
- распаковывать gzip-файлы;
- искать файлы через `find`;
- искать строки через `grep`;
- перенаправлять вывод и ошибки;
- читать сжатые man-страницы без распаковки.

## Задания

В этой работе вы соберёте вместе все навыки модуля: архивирование и сжатие, поиск файлов и строк, перенаправление потоков. Задания идут от простого к составному — в последних шагах команды уже объединяются в конвейер.

1. Соберите сжатый архив каталога `python`. Опция `-z` сразу сжимает архив через gzip, поэтому итоговый файл будет именно `/home/bob/python.tar.gz`:

   ```shell
   $ tar -zcf /home/bob/python.tar.gz /home/bob/reptile/snake/python
   ```

2. Распакуйте файл `eaglet.dat.gz` прямо в каталоге `eagle`, где он лежит. `gunzip` заменит сжатый файл распакованным:

   ```shell
   $ gunzip /home/bob/birds/eagle/eaglet.dat.gz
   ```

3. Найдите файл `caleston-code`, не зная, в каком он каталоге. Раз каталог неизвестен, поиск начинается от корня `/`, а это требует `sudo`:

   ```shell
   $ sudo find / -name caleston-code
   ```

4. Найдите файл `dummy.service` и запишите его абсолютный путь в `/home/bob/dummy-service`. Сначала `find` подскажет путь, затем `echo` с `>` сохранит его в файл:

   ```shell
   $ sudo find / -name dummy.service
   $ echo /etc/systemd/system/dummy.service > /home/bob/dummy-service
   ```

5. Найдите в `/etc` файл, содержащий строку `172.16.238.197`, и сохраните результат в `/home/bob/ip`. Здесь работает уже `grep`: он ищет не файл, а строку внутри файлов, а `>` отправляет находку в файл:

   ```shell
   $ sudo grep -ir 172.16.238.197 /etc/ > /home/bob/ip
   ```

6. Создайте файл `/home/bob/file_wth_data.txt` с единственной строкой `a file in my home directory`:

   ```shell
   $ echo "a file in my home directory" > /home/bob/file_wth_data.txt
   ```

7. Запустите `python3 /home/bob/my_python_test.py` и перенаправьте только поток ошибок `STDERR` в `/home/bob/py_error.txt` — за это отвечает `2>`:

   ```shell
   $ python3 /home/bob/my_python_test.py 2> /home/bob/py_error.txt
   ```

8. Прочитайте сжатую man-страницу `/usr/share/man/man1/tail.1.gz` без распаковки и сохраните её первую строку в `/home/bob/pipes`. Здесь три действия соединены в конвейер: `zcat` читает сжатый файл, `head -1` берёт первую строку, `>` записывает её в файл:

   ```shell
   $ zcat /usr/share/man/man1/tail.1.gz | head -1 > /home/bob/pipes
   ```

## Что нужно сдать

Оформите отчёт по [единому формату](../00-Lab-Environment/01-Lab-Environment-Setup.ru.md#формат-отчёта-по-лабораторной-работе). Дополнительно для этой работы приложите:

- Команды, которыми были выполнены задания.
- Вывод `ls -lh /home/bob/python.tar.gz`.
- Содержимое файлов `/home/bob/dummy-service`, `/home/bob/ip`, `/home/bob/py_error.txt`, `/home/bob/pipes`.

## Контрольные вопросы

1. Почему `tar -zcf` удобнее, чем отдельные `tar` и `gzip`?
2. Что делает `2>`?
3. Почему для поиска по `/` часто нужен `sudo`?
4. Как работает pipeline `zcat | head`?
