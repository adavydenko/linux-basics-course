# Python из командной строки

Этот раздел не является курсом Python. Его цель — научить запускать Python-скрипты в Linux воспроизводимо: из терминала, с аргументами, логами и изолированным окружением.

## Цели раздела

После раздела студент должен уметь:

- проверить, какой Python запускается;
- запускать Python-файлы из терминала;
- передавать аргументы;
- использовать `stdin`, `stdout`, `stderr`;
- создавать виртуальное окружение через `venv`;
- устанавливать зависимости из `requirements.txt`;
- запускать долгую Python-задачу с логами.

## Какой Python запускается

```shell
$ python --version
$ python3 --version
$ which python
$ which python3
```

В разных системах `python` и `python3` могут указывать на разные интерпретаторы. В учебных инструкциях лучше явно использовать `python3`, если именно он ожидается.

## Запуск файла

```shell
$ python3 script.py
```

Передача аргументов:

```shell
$ python3 script.py input.csv output.txt
```

Внутри Python эти аргументы доступны через `sys.argv` или через библиотеки вроде `argparse`.

## Перенаправления и коды завершения

Сохранить обычный вывод:

```shell
$ python3 script.py > out.log
```

Сохранить ошибки отдельно:

```shell
$ python3 script.py > out.log 2> err.log
```

Посмотреть код завершения:

```shell
$ echo $?
```

## Виртуальное окружение `venv`

Ставить Python-пакеты глобально через `sudo pip` не стоит: это может сломать системные пакеты и сделать результат невоспроизводимым.

Создать окружение:

```shell
$ python3 -m venv .venv
```

Активировать:

```shell
$ source .venv/bin/activate
```

Проверить Python внутри окружения:

```shell
$ which python
$ python --version
```

Установить зависимости:

```shell
$ pip install -r requirements.txt
```

Сохранить текущие зависимости:

```shell
$ pip freeze > requirements.txt
```

Выйти из окружения:

```shell
$ deactivate
```

## Долгий запуск

```shell
$ nohup .venv/bin/python script.py data.csv > out.log 2> err.log &
```

Для интерактивной работы лучше использовать `tmux`:

```shell
$ tmux
$ source .venv/bin/activate
$ python script.py data.csv
```

## Практическое задание

1. Создайте каталог проекта.
2. Создайте `.venv`.
3. Активируйте окружение.
4. Установите один пакет и сохраните `requirements.txt`.
5. Напишите короткий скрипт, который принимает имя входного файла.
6. Запустите скрипт с перенаправлением stdout и stderr.
7. Запустите скрипт через `nohup`.

## Контрольные вопросы

1. Почему не стоит использовать `sudo pip install`?
2. Что меняется после `source .venv/bin/activate`?
3. Зачем нужен `requirements.txt`?
4. Чем `python script.py > out.log 2> err.log` полезнее простого запуска?

