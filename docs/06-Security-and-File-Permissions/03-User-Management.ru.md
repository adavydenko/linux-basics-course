[English](03-User-Management.md) | **Русский**
# Управление пользователями

- Перейти к [видеоуроку](https://kodekloud.com/topic/user-management/)

В этом разделе мы научимся создавать и удалять пользователей и группы в Linux.

## Цели раздела

После раздела студент должен уметь:

- создавать локального пользователя;
- проверять запись пользователя в `/etc/passwd`;
- менять пароль;
- задавать UID, GID, домашний каталог, shell и комментарий;
- удалять пользователя;
- создавать и удалять группы.

## Создание пользователя

Создать локального пользователя `bob`:

```shell
$ useradd bob
```

Посмотреть сведения о пользователе `bob`: домашний каталог, UID, GID и shell:

```shell
$ grep -i bob /etc/passwd
bob:x:1002:1002::/home/bob:/bin/sh
```

![useradd](../../images//useradd.PNG)

Узнать имя текущего пользователя:

```shell
$ whoami
bob
```

Пароли пользователей хранятся в `/etc/shadow`. Обычный пользователь не должен иметь доступ к чтению этого файла:

```shell
$ sudo grep -i bob /etc/shadow
bob:!:18341:0:99999:7:::
```

Сменить пароль текущего пользователя можно через `passwd`. Для конкретного пользователя используется `passwd <username>`:

```shell
$ passwd bob
Changing password for user bob.
New UNIX password:
Retype new UNIX password:
passwd: all authentication tokens updated successfully.
```

## Управление пользователями

`useradd` можно использовать с параметрами:

```shell
$ useradd -u 1009 -g 1009 -d /home/robert -s /bin/bash -c "Mercury Project member" bob
```

Здесь:

- `-u` задаёт UID;
- `-g` задаёт основную группу;
- `-d` задаёт домашний каталог;
- `-s` задаёт shell;
- `-c` задаёт комментарий.

![manage](../../images//manage.PNG)

Удалить пользователя:

```shell
$ userdel bob
```

Создать группу:

```shell
$ groupadd -g 1011 developer
```

Удалить группу:

```shell
$ groupdel developer
```

## Практическое задание

1. Создайте пользователя `student1`.
2. Проверьте запись в `/etc/passwd`.
3. Создайте группу `lab`.
4. Создайте пользователя с заданным shell `/bin/bash`.
5. Удалите тестового пользователя и группу.

## Контрольные вопросы

1. Где хранится информация о пользователях?
2. Почему `/etc/shadow` должен быть защищён?
3. Что делает опция `-s` у `useradd`?
4. Чем `userdel` отличается от удаления домашнего каталога вручную?
