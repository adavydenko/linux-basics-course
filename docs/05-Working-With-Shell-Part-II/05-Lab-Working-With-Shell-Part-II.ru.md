[English](05-Lab-Working-With-Shell-Part-II.md) | **Русский**
# Лабораторная работа: командная строка, часть II

- Перейти к [лабораторной работе](https://kodekloud.com/topic/lab-working-with-shell-ii/)

## Цели лабораторной работы

После выполнения работы студент должен уметь:

- создавать сжатые архивы;
- распаковывать gzip-файлы;
- искать файлы через `find`;
- искать строки через `grep`;
- перенаправлять вывод и ошибки;
- читать сжатые man-страницы без распаковки.

## Задания

1. Создать сжатый архив каталога `python`. Итоговый файл должен быть доступен как `/home/bob/python.tar.gz`:

   ```shell
   $ tar -zcf /home/bob/python.tar.gz /home/bob/reptile/snake/python
   ```

2. Распаковать файл `eaglet.dat.gz`, расположенный в каталоге `eagle`, в том же месте:

   ```shell
   $ gunzip /home/bob/birds/eagle/eaglet.dat.gz
   ```

3. Найти файл `caleston-code`, если неизвестно, в каком каталоге он сохранён:

   ```shell
   $ sudo find / -name caleston-code
   ```

4. Найти файл `dummy.service` и записать его абсолютный путь в `/home/bob/dummy-service`:

   ```shell
   $ sudo find / -name dummy.service
   $ echo /etc/systemd/system/dummy.service > /home/bob/dummy-service
   ```

5. Найти файл в `/etc`, который содержит строку `172.16.238.197`, и сохранить результат в `/home/bob/ip`:

   ```shell
   $ sudo grep -ir 172.16.238.197 /etc/ > /home/bob/ip
   ```

6. Создать файл `/home/bob/file_wth_data.txt` с одной строкой `a file in my home directory`:

   ```shell
   $ echo "a file in my home directory" > /home/bob/file_wth_data.txt
   ```

7. Запустить `python3 /home/bob/my_python_test.py` и перенаправить `STDERR` в `/home/bob/py_error.txt`:

   ```shell
   $ python3 /home/bob/my_python_test.py 2> /home/bob/py_error.txt
   ```

8. Прочитать файл `/usr/share/man/man1/tail.1.gz` без распаковки и скопировать первую строку в `/home/bob/pipes`:

   ```shell
   $ zcat /usr/share/man/man1/tail.1.gz | head -1 > /home/bob/pipes
   ```

## Что нужно сдать

- Команды, которыми были выполнены задания.
- Вывод `ls -lh /home/bob/python.tar.gz`.
- Содержимое файлов `/home/bob/dummy-service`, `/home/bob/ip`, `/home/bob/py_error.txt`, `/home/bob/pipes`.

## Контрольные вопросы

1. Почему `tar -zcf` удобнее, чем отдельные `tar` и `gzip`?
2. Что делает `2>`?
3. Почему для поиска по `/` часто нужен `sudo`?
4. Как работает pipeline `zcat | head`?
