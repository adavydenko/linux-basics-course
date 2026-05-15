[English](03-SYSTEMD-Tools.md) | **Русский**
# Инструменты systemd

- Перейти к [видеоуроку](https://kodekloud.com/topic/systemd-tools/)

В этом разделе мы рассмотрим два основных инструмента systemd:

- `systemctl`;
- `journalctl`.

## Цели раздела

После раздела студент должен уметь:

- запускать, останавливать и перезапускать сервисы;
- включать и отключать автозапуск;
- смотреть статус сервиса;
- смотреть и редактировать unit-файлы;
- читать логи через `journalctl`.

## `systemctl`

`systemctl` — основная команда для управления сервисами на сервере с systemd.

Она используется для:

- `start`, `stop`, `restart`, `reload`;
- `enable`, `disable`;
- просмотра и управления units;
- просмотра и изменения targets.

![Systemctl](../../images/systemctl.png)

## Частые команды `systemctl`

Запустить сервис:

```shell
$ sudo systemctl start docker
```

Остановить сервис:

```shell
$ sudo systemctl stop docker
```

Перезапустить сервис:

```shell
$ sudo systemctl restart docker
```

Перезагрузить конфигурацию сервиса без полного перезапуска, если сервис это поддерживает:

```shell
$ sudo systemctl reload docker
```

Включить автозапуск:

```shell
$ sudo systemctl enable docker
```

Отключить автозапуск:

```shell
$ sudo systemctl disable docker
```

Посмотреть статус:

```shell
$ systemctl status docker
```

При нормальной работе сервис часто имеет состояние `active (running)`.

![Other](../../images/otherstate.PNG)

После изменения unit-файла нужно выполнить:

```shell
$ sudo systemctl daemon-reload
```

Редактировать unit-файл полностью:

```shell
$ sudo systemctl edit project-mercury.service --full
```

Посмотреть target по умолчанию:

```shell
$ systemctl get-default
```

Изменить target по умолчанию:

```shell
$ sudo systemctl set-default multi-user.target
```

Вывести все загруженные units:

```shell
$ systemctl list-units --all
```

Вывести только активные units:

```shell
$ systemctl list-units
```

Посмотреть содержимое unit-файла и путь к нему:

```shell
$ systemctl cat project-mercury.service
```

## `journalctl`

`journalctl` используется для просмотра логов, собранных systemd.

`systemd-journald` собирает сообщения ядра, сервисов systemd и других источников. Это один из главных инструментов диагностики сервисов.

![Journalctl](../../images/journalctl.png)

Показать все записи журнала от старых к новым:

```shell
$ journalctl
```

Показать логи текущей загрузки:

```shell
$ journalctl -b
```

Показать логи конкретного сервиса:

```shell
$ journalctl -u docker.service
```

Показать логи сервиса начиная с указанного времени:

```shell
$ journalctl -u docker.service --since "2022-01-01 13:45:00"
```

## Практическое задание

1. Посмотрите статус любого сервиса.
2. Посмотрите его unit-файл через `systemctl cat`.
3. Посмотрите логи через `journalctl -u`.
4. Найдите target по умолчанию.
5. Выведите список активных units.

## Контрольные вопросы

1. Чем `restart` отличается от `reload`?
2. Что делает `enable`?
3. Когда нужен `daemon-reload`?
4. Как посмотреть логи конкретного сервиса?
