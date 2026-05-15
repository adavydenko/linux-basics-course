[English](09-Lab-Linux-RunLevels-Filesystem-Hierarchy.md) | **Русский**
# Лабораторная работа: уровни запуска и файловая система

- Перейти к [лабораторной работе](https://kodekloud.com/topic/lab-linux-kernel-modules-boot-and-filetypes/)

## Цели лабораторной работы

После выполнения работы студент должен уметь:

- запускать команды с `sudo`;
- проверять init-систему;
- смотреть и менять target systemd по умолчанию;
- определять тип файлов;
- ориентироваться в назначении системных каталогов.

## Задания

1. Запустить команду, требующую прав суперпользователя:

   ```shell
   $ sudo ls /root
   ```

2. Проверить, какая init-система используется: `systemd` или SysV:

   ```shell
   $ sudo ls -l /sbin/init
   ```

3. Проверить target systemd по умолчанию:

   ```shell
   $ sudo systemctl get-default
   ```

4. Изменить target systemd на `multi-user.target`:

   ```shell
   $ sudo systemctl set-default multi-user.target
   ```

5. Определить тип файла `/root/firefox.deb`:

   ```shell
   $ sudo file /root/firefox.deb
   ```

6. Определить тип файла `/root/sample_script.sh`:

   ```shell
   $ sudo file /root/sample_script.sh
   ```

7. Ответить, какой каталог рекомендуется для установки сторонней IDE:

   ```text
   Стороннее программное обеспечение обычно устанавливают в /opt.
   ```

8. Ответить, где находятся файлы блочных устройств, которые видны через `lsblk`:

   ```text
   Файлы устройств находятся в каталоге /dev.
   ```

9. Найти производителя Ethernet Controller в системе:

   ```shell
   $ sudo lshw
   ```

   В выводе найдите сетевой раздел и поле `vendor`.

## Что нужно сдать

- Вывод `systemctl get-default`.
- Вывод `ls -l /sbin/init`.
- Результаты `file` для двух файлов.
- Ответы по каталогам `/opt` и `/dev`.
- Фрагмент `lshw` с производителем сетевого контроллера.

## Контрольные вопросы

1. Зачем нужен `sudo`?
2. Как узнать target systemd по умолчанию?
3. Почему стороннее ПО часто ставят в `/opt`?
4. Что хранится в `/dev`?

