[English](02-Linux-Accounts.md) | **Русский**
# Учётные записи Linux

- Перейти к [видеоуроку](https://kodekloud.com/topic/linux-accounts/)

В этом разделе мы рассмотрим базовый контроль доступа в Linux и подготовимся к теме прав доступа к файлам.

## Цели раздела

После раздела студент должен уметь:

- понимать, где хранятся сведения о пользователях и группах;
- читать базовую информацию из `/etc/passwd` и `/etc/group`;
- узнавать UID и GID пользователя;
- смотреть текущие входы в систему;
- переключаться между пользователями;
- понимать разницу между `su` и `sudo`.

![linux](../../images/linux.PNG)

## Учётные записи пользователей

Информация о пользователях хранится в `/etc/passwd`:

```shell
$ cat /etc/passwd
```

Информация о группах хранится в `/etc/group`:

```shell
$ cat /etc/group
```

![user](../../images/user.PNG)

У каждого пользователя есть имя и уникальный идентификатор UID. Также у пользователя есть основной идентификатор группы GID. Проверить эти данные можно командой `id`:

```shell
$ id michael
uid=1001(michael) gid=1001(michael) groups=1001(michael),1003(developers)
```

Дополнительную информацию, например домашний каталог и shell по умолчанию, можно увидеть в `/etc/passwd`:

```shell
$ grep -i michael /etc/passwd
michael:x:1001:1001::/home/michael:/bin/sh
```

![group](../../images/group.PNG)

Список пользователей, которые сейчас вошли в систему:

```shell
$ who
bob pts/2 Apr 28 06:48 (172.16.238.187)
```

Команда `last` показывает историю входов пользователей и перезагрузок системы:

```shell
$ last
michael :1 :1 Tue May 12 20:00 still logged in
sarah :1 :1 Tue May 12 12:00 still running
reboot system boot 5.3.0-758-gen Mon May 11 13:00 - 19:00 (06:00)
```

## Переключение пользователей

Для переключения на другого пользователя используется `su`:

```shell
$ su -
Password:
root ~#
```

Запустить одну команду от имени другого пользователя можно через `su -c`, но для административных задач чаще используют `sudo`:

```shell
$ su -c "whoami"
Password:
root
```

Рекомендуемый способ запускать команду с правами администратора — `sudo`:

```shell
$ sudo apt-get install nginx
[sudo] password for michael:
```

![who](../../images/who.PNG)

Пользователи, которым разрешено использовать `sudo`, описываются в `/etc/sudoers` и связанных файлах:

```shell
$ sudo cat /etc/sudoers
```

![sudo](../../images/sudo.PNG)

Чтобы запретить прямой вход под `root`, можно назначить ему shell `nologin`:

```shell
$ grep -i ^root /etc/passwd
root:x:0:0:root:/root:/usr/sbin/nologin
```

## Контрольные вопросы

1. Что такое UID и GID?
2. Чем `/etc/passwd` отличается от `/etc/shadow`?
3. Когда лучше использовать `sudo`, а не `su`?
4. Как узнать, кто сейчас вошёл в систему?
