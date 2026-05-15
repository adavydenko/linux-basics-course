[English](04-Troubleshooting.md) | **Русский**
# Диагностика сетевых проблем

- Перейти к [видеоуроку](https://kodekloud.com/topic/troubleshooting/)

В этом разделе мы разберём сетевую проблему, с которой столкнулся Bob: он не может подключиться к серверу репозитория.

## Цели раздела

После раздела студент должен уметь:

- проверять состояние сетевого интерфейса;
- проверять разрешение имени в IP-адрес;
- проверять доступность через `ping`;
- смотреть маршрут через `traceroute`;
- проверять, слушает ли сервис нужный порт;
- поднимать сетевой интерфейс.

![site](../../images/site.PNG)

## Проверить интерфейсы

Используйте `ip link`, чтобы убедиться, что основной интерфейс поднят. В примере интерфейс `enp1s0f1` находится в состоянии `UP`.

```shell
$ ip link
1: lo: <LOOPBACK,UP,LOWER_UP> mtu 65536 qdisc noqueue state UNKNOWN mode DEFAULT group default qlen 1000
2: enp1s0f1: <BROADCAST,BROADCAST,MULTICAST,UP> mtu 1500 qdisc fq_codel state UP mode DEFAULT group default qlen 1000
```

## Проверить DNS

Проверить, разрешается ли имя хоста в IP-адрес:

```shell
$ nslookup caleston-repo-01
Server:      192.168.1.100
Address:     192.168.1.100 #53

Non-authoritative answer:
Name: caleston-repo-01
Address: 192.168.2.5
```

## Проверить связность

`ping` помогает проверить, отвечает ли удалённый узел:

```shell
$ ping caleston-repo-01
PING caleston-repo-01 (192.168.2.5) 56(84) bytes of data.

--- localhost ping statistics ---
3 packets transmitted, 0 received, 100% packet loss, time 2034ms
```

Если DNS работает, но `ping` не проходит, проблема может быть в маршрутизации, firewall или самом удалённом хосте.

## Проверить маршрут

`traceroute` показывает промежуточные узлы между источником и назначением:

```shell
$ traceroute 192.168.2.5

Tracing route to example.com [192.168.2.5]
over a maximum of 30 hops:
1 <1 ms <1 ms <1 ms 192.168.1.1
2 <2 ms <1 ms <1 ms 192.168.2.1
3 * * * Request timed out.
```

## Проверить порт

В оригинальном материале используется `netstat`:

```shell
$ netstat -an | grep 80 | grep -i LISTEN
```

В современных системах чаще используют `ss`:

```shell
$ ss -tuln | grep ':80'
```

![net](../../images/net.PNG)

## Поднять интерфейс

Если интерфейс выключен, его можно поднять:

```shell
$ ip link set dev enp1s0f1 up
```

![iplink](../../images/iplink.PNG)

## Контрольный порядок диагностики

1. `ip link` — интерфейс включён?
2. `ip addr` — есть IP-адрес?
3. `ip route` — есть маршрут?
4. `nslookup` или `dig` — работает DNS?
5. `ping` — есть связность?
6. `ss` или `netstat` — слушает ли сервис порт?

## Контрольные вопросы

1. Что проверяет `ip link`?
2. Почему DNS может работать, а `ping` всё равно нет?
3. Для чего нужен `traceroute`?
4. Чем `ss` отличается от старого `netstat`?
