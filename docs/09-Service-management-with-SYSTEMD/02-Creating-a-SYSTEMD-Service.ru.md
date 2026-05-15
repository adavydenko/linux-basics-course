[English](02-Creating-a-SYSTEMD-Service.md) | **Русский**
# Создание собственного systemd-сервиса

- Перейти к [видеоуроку](https://kodekloud.com/topic/creating-a-systemd-service/)

В этом разделе мы научимся создавать service unit для systemd.

## Цели раздела

После раздела студент должен уметь:

- объяснить, что такое systemd;
- понимать структуру `.service` unit-файла;
- описать секции `[Unit]`, `[Service]`, `[Install]`;
- перезагружать конфигурацию systemd;
- запускать собственный сервис.

Systemd — система инициализации и менеджер сервисов Linux. Большинство крупных дистрибутивов, включая RHEL, CentOS, Fedora, Ubuntu, Debian и Arch Linux, используют systemd как init-систему.

Systemd умеет запускать демоны по требованию, управлять точками монтирования и автомонтирования, собирать логи и выполнять другие задачи администрирования.

## Что такое service unit

Файл с суффиксом `.service` описывает процесс, которым управляет systemd. Обычно он состоит из трёх основных секций.

## `[Unit]`

Секция `[Unit]` содержит описание unit, его поведение и зависимости.

Пример:

```ini
[Unit]
Description=Python Django for Project Mercury
Documentation=http://wiki.caleston-dev.ca/mercury
After=postgresql.service
```

Поля:

- `Description` — краткое описание сервиса;
- `Documentation` — ссылка на документацию;
- `After` — запускать этот unit после указанных units.

## `[Service]`

Секция `[Service]` описывает, какую команду запускать и от какого пользователя:

```ini
[Service]
ExecStart=/usr/bin/project-mercury.sh
User=project_mercury
Restart=on-failure
RestartSec=10
```

Поля:

- `ExecStart` — команда запуска;
- `User` — пользователь, от имени которого работает сервис;
- `Restart` — политика перезапуска;
- `RestartSec` — задержка перед перезапуском.

## `[Install]`

Секция `[Install]` описывает, как unit включается в автозапуск:

```ini
[Install]
WantedBy=graphical.target
```

Для серверных сервисов часто используется `multi-user.target`.

## Запуск сервиса

После создания или изменения unit-файла нужно перезагрузить конфигурацию systemd:

```shell
$ sudo systemctl daemon-reload
```

Запустить сервис:

```shell
$ sudo systemctl start project-mercury.service
```

Включить автозапуск:

```shell
$ sudo systemctl enable project-mercury.service
```

## Контрольные вопросы

1. Зачем нужен `systemctl daemon-reload`?
2. Что делает `ExecStart`?
3. Чем `start` отличается от `enable`?
4. Почему сервис лучше запускать от отдельного пользователя, а не от `root`?
