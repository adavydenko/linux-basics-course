[English](03-Networking-Basics.md) | **Русский**
# Основы сети: switching и routing

- Перейти к [видеоуроку](https://kodekloud.com/topic/networking-basics/)

## Цели раздела

После раздела студент должен уметь:

- понимать разницу между switching и routing;
- смотреть сетевые интерфейсы;
- назначать IP-адрес интерфейсу;
- смотреть таблицу маршрутизации;
- добавлять маршрут через gateway.

## Switching

Switching помогает соединять интерфейсы внутри одной сети.

![switch](../../images//switch.PNG)

Посмотреть интерфейсы на хосте:

```shell
$ ip link
eth0: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc fq_codel state UP mode DEFAULT group default qlen 1000
```

Назначить IP-адрес интерфейсу:

```shell
$ ip addr add 192.168.1.10/24 dev eth0
```

## Routing

Router соединяет разные сети.

![route](../../images//routing.PNG)

Посмотреть текущую таблицу маршрутизации можно через старую команду `route`:

```shell
$ route
Kernel IP routing table
Destination Gateway Genmask Flags Metric Ref Use Iface
```

Современная команда:

```shell
$ ip route
```

Добавить маршрут к сети `192.168.2.0/24` через gateway `192.168.1.1`:

```shell
$ ip route add 192.168.2.0/24 via 192.168.1.1
```

Проверить результат:

```shell
$ route
Kernel IP routing table
Destination Gateway Genmask Flags Metric Ref Use Iface
192.168.2.0 192.168.1.1 255.255.255.0 UG 0 0 0 eth0
```

Посмотреть IP-адреса интерфейсов:

```shell
$ ip addr
```

Чтобы сделать изменения постоянными, их нужно записать в конфигурацию сети. В старых Debian/Ubuntu-системах это мог быть `/etc/network/interfaces`; в современных системах чаще используются NetworkManager, Netplan или systemd-networkd.

## Практическое задание

1. Выполните `ip link`.
2. Выполните `ip addr`.
3. Выполните `ip route`.
4. Найдите интерфейс с активным IP-адресом.
5. Объясните, какой маршрут используется по умолчанию.

## Контрольные вопросы

1. Чем switch отличается от router?
2. Что показывает `ip link`?
3. Что показывает `ip route`?
4. Что такое gateway?
