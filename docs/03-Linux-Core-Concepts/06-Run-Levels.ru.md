[English](06-Run-Levels.md) | **Русский**
# Уровни запуска и targets systemd

- Перейти к [видеоуроку](https://kodekloud.com/topic/runlevels/)

## Цели раздела

После раздела студент должен уметь:

- объяснить, что такое runlevel;
- понимать соответствие runlevels и targets в `systemd`;
- посмотреть текущий и стандартный target;
- изменить target по умолчанию.

## Systemd targets

Сервер можно настроить так, чтобы он загружался в графический или неграфический режим. В классических Linux-системах такие режимы назывались `runlevel`.

- Графический режим обычно соответствовал `runlevel 5`.
- Неграфический многопользовательский режим обычно соответствовал `runlevel 3`.

![run-levels](../../images/run-levels.PNG)

Чтобы посмотреть текущий режим, можно выполнить:

```shell
$ runlevel
```

Во время загрузки init-процесс проверяет нужный режим и запускает программы, необходимые для работы системы в этом режиме. Например, графический режим требует display manager, а неграфический режим может работать без него.

![run-levels1](../../images/run-levels1.PNG)

В современных дистрибутивах, где используется `systemd`, runlevels представлены через `targets`.

- Runlevel 5 соответствует `graphical.target`.
- Runlevel 3 соответствует `multi-user.target`.

![run-levels2](../../images/run-levels2.PNG)

## Просмотр и изменение target

Чтобы посмотреть target по умолчанию, выполните:

```shell
$ systemctl get-default
```

Эта команда смотрит на настройку, связанную с `/etc/systemd/system/default.target`.

Чтобы изменить target по умолчанию, используйте `systemctl set-default`:

```shell
$ systemctl set-default multi-user.target
```

В реальной системе для изменения target обычно нужны права администратора:

```shell
$ sudo systemctl set-default multi-user.target
```

## Практическое задание

1. Выполните `systemctl get-default`.
2. Определите, графический это target или нет.
3. Найдите файл или ссылку `/etc/systemd/system/default.target`.
4. Объясните, почему на сервере часто используют `multi-user.target`, а не `graphical.target`.

## Контрольные вопросы

1. Чем `runlevel` отличается от `systemd target`?
2. Какой target соответствует неграфическому многопользовательскому режиму?
3. Почему графический режим не всегда нужен на сервере?
4. Какая команда меняет target по умолчанию?

