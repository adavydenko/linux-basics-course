[English](02-Troubleshoot-the-Development-Environment.md) | **Русский**
# Диагностика среды разработки

- Перейти к [лабораторной работе](https://kodekloud.com/topic/lab-troubleshoot-the-development-environment/)

Этот раздел — практический troubleshooting-кейс. Нужно перенести приложение на сервер, настроить базу данных, исправить конфигурацию, запустить приложение и оформить его как systemd-сервис.

## Цели раздела

После раздела студент должен уметь:

- копировать архив на удалённый сервер;
- распаковывать приложение в `/opt`;
- проверять состояние PostgreSQL;
- редактировать конфигурационные файлы;
- диагностировать ошибку подключения приложения к БД;
- менять владельца файлов;
- активировать Python virtualenv;
- создавать systemd unit для приложения.

## Ход работы

1. Скопировать `caleston-code.tar.gz` с ноутбука Bob в домашний каталог Bob на web-сервере `devapp01`:

   ```bash
   scp caleston-code.tar.gz devapp01:~/
   ```

2. На `devapp01` распаковать архив в `/opt`. Каталог `/opt` принадлежит `root`, поэтому нужен `sudo`:

   ```bash
   ssh devapp01
   sudo tar -zxf caleston-code.tar.gz -C /opt
   ```

3. Удалить tar-файл с `devapp01`:

   ```bash
   rm caleston-code.tar.gz
   ```

4. Проверить, что существует путь `/opt/caleston-code/mercuryProject/`:

   ```bash
   ls -l /opt/caleston-code/mercuryProject/
   ```

5. Подключиться к серверу базы данных `devdb01` и проверить статус PostgreSQL:

   ```bash
   exit
   ssh devdb01
   systemctl status postgresql.service
   ```

   Если статус `Active: inactive (dead)`, база данных не запущена.

6. Добавить строку в конец `/etc/postgresql/10/main/pg_hba.conf`, чтобы web-приложение могло подключаться к БД:

   ```text
   host all all 0.0.0.0/0 md5
   ```

   Редактирование:

   ```bash
   sudo vi /etc/postgresql/10/main/pg_hba.conf
   ```

7. Запустить PostgreSQL:

   ```bash
   sudo systemctl start postgresql.service
   ```

8. Проверить, на каком порту работает PostgreSQL:

   ```bash
   sudo netstat -ptean
   ```

   В современных системах можно использовать:

   ```bash
   sudo ss -tulpen | grep postgres
   ```

9. Вернуться на `devapp01`, перейти в каталог приложения и попробовать запустить web-приложение:

   ```bash
   exit
   ssh devapp01
   cd /opt/caleston-code/mercuryProject
   python3 manage.py runserver 0.0.0.0:8000
   ```

   Если приложение выводит stack trace и падает, значит запуск не удался. Остановите его через `Ctrl+C`.

10. Найти причину ошибки.

    В конце stack trace указано, что приложение не может подключиться к базе данных по заданному адресу и порту. Вспомните порт PostgreSQL, найденный на предыдущем шаге.

11. Найти файл, где описана настройка `DATABASES`:

    ```bash
    find . -type f -exec grep -l 'DATABASES = {' "{}" \;
    ```

    Открыть найденный файл:

    ```bash
    vi ./mercury/settings.py
    ```

    В секции `DATABASES` указать правильный host и port.

12. Изменить владельца всех файлов и каталогов под `/opt/caleston-code` на пользователя `mercury`:

    ```bash
    sudo chown -R mercury /opt/caleston-code
    ```

13. Активировать virtualenv и выполнить миграции:

    ```bash
    source ../venv/bin/activate
    python3 manage.py migrate
    ```

    `venv` — виртуальное окружение Python. Оно позволяет устанавливать зависимости проекта отдельно от системной установки Python.

14. Создать systemd unit для запуска приложения как сервиса.

    Сначала остановите запущенное приложение через `Ctrl+C`. Узнайте полный путь к `python3`:

    ```bash
    which python3
    ```

    Создайте unit-файл:

    ```bash
    sudo vi /etc/systemd/system/mercury.service
    ```

    Содержимое. Если на предыдущем шаге `which python3` показал путь к Python внутри `venv`, используйте именно его:

    ```ini
    [Unit]
    Description=Project Mercury Web Application

    [Service]
    ExecStart=/opt/caleston-code/venv/bin/python3 manage.py runserver 0.0.0.0:8000
    Restart=on-failure
    WorkingDirectory=/opt/caleston-code/mercuryProject/
    User=mercury

    [Install]
    WantedBy=multi-user.target
    ```

15. Перезагрузить конфигурацию systemd, включить и запустить сервис:

    ```bash
    sudo systemctl daemon-reload
    sudo systemctl enable mercury
    sudo systemctl start mercury
    ```

16. Проверить статус и логи:

    ```bash
    systemctl status mercury
    journalctl -u mercury
    ```

## Технические замечания

- В unit-файлах лучше использовать абсолютные пути, потому что окружение systemd отличается от интерактивного shell.
- Для Python-приложений важно запускать интерпретатор из `venv`, иначе сервис может не увидеть зависимости проекта.
- После создания или изменения unit-файла нужен `systemctl daemon-reload`.
- Если сервис не запускается, сначала смотрите `systemctl status`, затем `journalctl -u`.
- `netstat` может отсутствовать в современных системах; используйте `ss`.

## Контрольные вопросы

1. Почему для распаковки в `/opt` нужен `sudo`?
2. Где PostgreSQL хранит правила доступа клиентов?
3. Как понять, на каком порту слушает база данных?
4. Почему приложение могло падать при запуске?
5. Зачем нужен `WorkingDirectory` в unit-файле?
6. Что делает `systemctl daemon-reload`?
