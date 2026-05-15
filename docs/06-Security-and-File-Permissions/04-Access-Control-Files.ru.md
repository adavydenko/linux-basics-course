[English](04-Access-Control-Files.md) | **Русский**
# Файлы управления доступом

- Перейти к [видеоуроку](https://kodekloud.com/topic/access-control-files/)

Файлы управления доступом находятся в `/etc`. Обычно их может читать широкий круг пользователей, но изменять должен только `root`.

## Цели раздела

После раздела студент должен уметь:

- читать структуру `/etc/passwd`;
- понимать назначение `/etc/shadow`;
- читать структуру `/etc/group`;
- объяснить, почему эти файлы критичны для безопасности.

## `/etc/passwd`

Получить сведения об учётной записи `bob`:

```shell
$ grep -i ^bob /etc/passwd
bob:x:1002:1002::/home/bob:/bin/sh
USERNAME:PASSWORD:UID:GID:GECOS:HOMEDIR:SHELL
```

![passwd](../../images//passwd.PNG)

Поле `x` в колонке пароля означает, что хэш пароля хранится не здесь, а в `/etc/shadow`.

## `/etc/shadow`

Пароли пользователей хранятся в `/etc/shadow` в виде хэшей:

```shell
$ sudo grep -i ^bob /etc/shadow
bob:$6$0h0utOtO$5JcuRxR7y72LLQk4Kdog7u09LsNFS0yZPkIC8pV9tgD0wXCHutYcWF/7.eJ3TfGfG0lj4JF63PyuPwKC18tJS.:18188:0:99999:7:::

USERNAME:PASSWORD:LASTCHANGE:MINAGE:MAXAGE:WARN:INACTIVE:EXPDATE
```

![shadow](../../images//shadow.PNG)

## `/etc/group`

Проверить группы, к которым относится `bob`:

```shell
$ grep -i ^bob /etc/group
NAME:PASSWORD:GID:MEMBERS
```

![egp](../../images//egp.PNG)

## Практическое задание

1. Найдите запись своего пользователя в `/etc/passwd`.
2. Определите UID, GID, домашний каталог и shell.
3. Найдите группы своего пользователя через `id` и `/etc/group`.
4. Попробуйте прочитать `/etc/shadow` без `sudo` и объясните результат.

## Контрольные вопросы

1. Почему пароль не хранится напрямую в `/etc/passwd`?
2. Что такое GECOS?
3. Какой файл содержит список групп?
4. Почему изменение этих файлов вручную опасно?
