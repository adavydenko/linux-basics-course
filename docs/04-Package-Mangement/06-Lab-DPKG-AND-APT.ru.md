[English](06-Lab-DPKG-AND-APT.md) | **Русский**
# Лабораторная работа: DPKG и APT

- Перейти к [лабораторной работе](https://kodekloud.com/topic/lab-dpkg-and-apt-2/)

## Цели лабораторной работы

После выполнения работы студент должен уметь:

- выбрать пакетный менеджер для Debian-based дистрибутива;
- установить локальный `.deb` пакет через `dpkg`;
- установить пакет через `apt`;
- искать пакеты в репозитории;
- удалять установленные пакеты.

## Задания

1. Ответить, какие пакетные менеджеры используются в Debian-based дистрибутивах:

   ```text
   Debian-based дистрибутивы используют dpkg и apt.
   ```

2. Установить пакет браузера `firefox`, скачанный в `/root/firefox.deb`. Зависимости могут не установиться автоматически:

   ```shell
   $ sudo dpkg -i /root/firefox.deb
   ```

3. Установить пакет через `APT`:

   ```shell
   $ sudo apt install firefox
   ```

4. Найти пакет для установки браузера Chromium. Используйте `apt search`; описание пакета: Chromium web browser, open-source version of Chrome.

   ```shell
   $ sudo apt search chromium-browser
   ```

5. Установить `chromium-browser`:

   ```shell
   $ sudo apt install -y chromium-browser
   ```

6. Удалить браузер `firefox`:

   ```shell
   $ sudo apt remove firefox
   ```

## Что нужно сдать

- Команды установки через `dpkg` и `apt`.
- Результат поиска Chromium через `apt search`.
- Команду удаления `firefox`.
- Объяснение, почему `dpkg -i` может завершиться ошибкой зависимостей.

## Контрольные вопросы

1. Чем `dpkg -i` отличается от `apt install`?
2. Что делает флаг `-y`?
3. Почему перед установкой иногда полезно выполнить `apt update`?
4. Как найти пакет, если известно только описание программы?

