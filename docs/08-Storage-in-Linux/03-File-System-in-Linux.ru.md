[English](03-File-System-in-Linux.md) | **Русский**
# Файловые системы в Linux

- Перейти к [видеоуроку](https://kodekloud.com/topic/file-systems-in-linux/)

В этом разделе мы рассмотрим распространённые файловые системы Linux, включая семейство EXT.

## Цели раздела

После раздела студент должен уметь:

- создать файловую систему ext4;
- создать точку монтирования;
- смонтировать файловую систему;
- проверить монтирование;
- добавить запись в `/etc/fstab`.

![fs](../../images/fs.PNG)

## Работа с ext4

Создать файловую систему на разделе `/dev/sdb1`:

```shell
$ sudo mkfs.ext4 /dev/sdb1
```

Создать каталог-точку монтирования и смонтировать файловую систему:

```shell
$ sudo mkdir /mnt/ext4
$ sudo mount /dev/sdb1 /mnt/ext4
```

Проверить, что файловая система смонтирована:

```shell
$ mount | grep /dev/sdb1
$ df -hP | grep /dev/sdb1
```

Чтобы файловая система была доступна после перезагрузки, добавьте запись в `/etc/fstab`.

Пример структуры `/etc/fstab`:

```text
# <file system> <mount point> <type> <options> <dump> <pass>
/dev/sda1 / ext4 defaults,relatime,errors=panic 0 1
```

Добавить запись для `/dev/sdb1`:

```shell
$ echo "/dev/sdb1 /mnt/ext4 ext4 rw 0 0" | sudo tee -a /etc/fstab
```

Лучше использовать UUID, потому что имена вроде `/dev/sdb1` могут измениться при подключении дисков:

```shell
$ blkid /dev/sdb1
```

![fstab](../../images/fstab.PNG)

## Контрольные вопросы

1. Что делает `mkfs.ext4`?
2. Что такое точка монтирования?
3. Как проверить, что файловая система смонтирована?
4. Почему UUID надёжнее имени `/dev/sdb1` в `/etc/fstab`?
