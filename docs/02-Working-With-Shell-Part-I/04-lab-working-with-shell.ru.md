[English](04-lab-working-with-shell.md) | **Русский**
# Лабораторная работа: оболочка и базовые команды

- Перейти к [лабораторной работе](https://kodekloud.com/topic/lab-working-with-the-shell/)

## Цели лабораторной работы

После выполнения работы студент должен уметь:

- определять домашний каталог пользователя;
- различать команду и аргумент;
- определять тип команды;
- создавать, перемещать, переименовывать и удалять каталоги;
- использовать абсолютные пути в командах.

## Задания

1. Проверить домашний каталог пользователя `bob` через `/etc/passwd`:

   ```shell
   $ grep bob /etc/passwd | cut -d ":" -f6
   ```

2. Проверить домашний каталог текущего пользователя через встроенную переменную shell:

   ```shell
   $ echo $HOME
   ```

3. В команде `echo Welcome` определить, чем является слово `Welcome`:

   ```shell
   $ echo Welcome
   ```

   `Welcome` — это аргумент команды `echo`.

4. Определить тип команды `git`:

   ```shell
   $ type git
   ```

5. Создать каталог:

   ```shell
   $ mkdir /home/bob/birds
   ```

6. Создать вложенные каталоги рекурсивно:

   ```shell
   $ mkdir -p /home/bob/fish/salmon
   ```

7. Создать ещё несколько каталогов:

   ```shell
   $ mkdir -p /home/bob/mammals/elephant
   $ mkdir -p /home/bob/mammals/monkey
   $ mkdir /home/bob/birds/eagle
   $ mkdir -p /home/bob/reptile/snake
   $ mkdir -p /home/bob/reptile/frog
   $ mkdir -p /home/bob/amphibian/salamander
   ```

8. Переместить каталог:

   ```shell
   $ mv /home/bob/reptile/frog /home/bob/amphibian
   ```

9. Переименовать каталог:

   ```shell
   $ mv /home/bob/reptile/snake /home/bob/reptile/crocodile
   ```

10. Удалить каталог:

    ```shell
    $ rm -r /home/bob/reptile
    ```

## Что нужно сдать

- Список выполненных команд.
- Краткое объяснение команд `grep`, `cut`, `mkdir -p`, `mv`, `rm -r`.
- Вывод `ls` или `tree`, подтверждающий итоговую структуру каталогов.

## Контрольные вопросы

1. Почему `mkdir -p` удобен для создания вложенных каталогов?
2. Чем перемещение каталога отличается от переименования с точки зрения команды `mv`?
3. Почему команду `rm -r` нужно использовать осторожно?
4. Как узнать, где находится домашний каталог текущего пользователя?

