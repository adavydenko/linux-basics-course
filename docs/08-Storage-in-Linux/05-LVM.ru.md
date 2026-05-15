[English](05-LVM.md) | **Русский**
# LVM: Logical Volume Manager

- Перейти к [видеоуроку](https://kodekloud.com/topic/lvm/)

LVM позволяет объединять несколько физических томов — дисков или разделов — в группу томов, а затем создавать из неё логические тома нужного размера.

## Цели раздела

После раздела студент должен уметь:

- объяснить термины PV, VG и LV;
- создать physical volume;
- создать volume group;
- создать logical volume;
- создать файловую систему на LV;
- смонтировать LV;
- увеличить логический том и файловую систему.

![LVM](../../images/lvm.PNG)

## Основные понятия

- `PV` (`Physical Volume`) — физический том: диск или раздел, подготовленный для LVM.
- `VG` (`Volume Group`) — группа томов, объединяющая один или несколько PV.
- `LV` (`Logical Volume`) — логический том, созданный внутри VG.

## Работа с LVM

Установить пакет:

```shell
$ sudo apt-get install lvm2
```

Создать physical volume:

```shell
$ sudo pvcreate /dev/sdb
Physical volume "/dev/sdb" successfully created
```

Создать volume group:

```shell
$ sudo vgcreate caleston_vg /dev/sdb
Volume group "caleston_vg" successfully created
```

Посмотреть physical volumes:

```shell
$ sudo pvdisplay
```

Посмотреть volume groups:

```shell
$ sudo vgdisplay
```

Создать logical volume размером 1G:

```shell
$ sudo lvcreate -L 1G -n vol1 caleston_vg
Logical volume "vol1" created.
```

Посмотреть logical volumes:

```shell
$ sudo lvdisplay
$ sudo lvs
```

Создать файловую систему:

```shell
$ sudo mkfs.ext4 /dev/caleston_vg/vol1
```

Создать точку монтирования и смонтировать:

```shell
$ sudo mkdir -p /mnt/vol1
$ sudo mount -t ext4 /dev/caleston_vg/vol1 /mnt/vol1
```

## Увеличение logical volume

Проверить свободное место в VG:

```shell
$ sudo vgs
VG #PV #LV #SN Attr VSize VFree
caleston_vg 1 1 0 wz--n- 20.00g 19.00g
```

Увеличить LV на 1G:

```shell
$ sudo lvresize -L +1G /dev/caleston_vg/vol1
Logical volume vol1 successfully resized.
```

Проверить размер файловой системы:

```shell
$ df -hP /mnt/vol1
```

Увеличить файловую систему ext4:

```shell
$ sudo resize2fs /dev/caleston_vg/vol1
```

Проверить результат:

```shell
$ df -hP /mnt/vol1
Filesystem Size Used Avail Use% Mounted on
/dev/mapper/caleston_vg-vol1 2.0G 1.6M 1.9G 1% /mnt/vol1
```

![LVM2](../../images/lvm2.PNG)

## Важное предупреждение

Команды LVM меняют структуру хранения данных. Выполняйте их только на учебных дисках или в лабораторной среде.

## Контрольные вопросы

1. Чем PV отличается от VG?
2. Что такое LV?
3. Почему после `lvresize` для ext4 нужен `resize2fs`?
4. Какая команда показывает свободное место в volume group?
