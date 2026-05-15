[English](02-DNS.md) | **Русский**
# DNS

- Перейти к [видеоуроку](https://kodekloud.com/topic/dns/)

DNS (`Domain Name System`, система доменных имён) — распределённая система, которая сопоставляет имена хостов с IP-адресами. Благодаря DNS каждому клиенту не нужно вручную синхронизировать файл `hosts`. Сервер имён публикует IP-адрес для домена и даёт единую точку обновления, если IP-адрес меняется.

## Цели раздела

После раздела студент должен уметь:

- объяснить, зачем нужен DNS;
- использовать `ping` для проверки доступности;
- понимать роль `/etc/hosts`, `/etc/resolv.conf`, `/etc/nsswitch.conf`;
- назвать базовые типы DNS-записей;
- проверять разрешение имён через `nslookup` и `dig`.

## `ping`

Команда `ping` проверяет, доступна ли удалённая машина или сервер:

```bash
$ ping 192.168.1.11
Reply from 192.168.1.11: bytes=32 time=4ms TTL=117
Reply from 192.168.1.11: bytes=32 time=4ms TTL=117
```

Аргументом может быть IP-адрес или имя хоста. Чтобы использовать своё имя вместо IP-адреса, можно добавить запись в `/etc/hosts`:

```bash
$ cat >> /etc/hosts
192.168.1.11 db
```

После этого имя можно использовать в `ping`:

```bash
$ ping db
PING db (192.168.1.11) 56(84) bytes of data.
64 bytes from db (192.168.1.11): icmp_seq=1 ttl=64 time=0.052 ms
64 bytes from db (192.168.1.11): icmp_seq=2 ttl=64 time=0.079 ms
```

В `/etc/hosts` можно определить много имён:

```bash
$ cat >> /etc/hosts
192.168.1.10 web
192.168.1.11 db
192.168.1.12 nfs
192.168.1.20 web
192.168.1.21 db-1
192.168.1.22 nfs-1
```

## Файлы DNS-настроек

Файл `/etc/resolv.conf` указывает DNS-серверы:

```bash
$ cat /etc/resolv.conf
nameserver 192.168.1.100
```

Файл `/etc/nsswitch.conf` задаёт порядок источников, которые система использует для поиска информации: имена хостов, пользователи, группы и так далее.

```bash
$ cat /etc/nsswitch.conf
# ...
hosts: files dns
# ...
```

Строка `hosts: files dns` означает: сначала смотреть локальные файлы, например `/etc/hosts`, затем обращаться к DNS.

## Доменные имена

![DNS](../../images//dns.PNG)

Примеры доменных зон:

- `.com` — коммерческие или общие домены;
- `.net` — сетевые или общие домены;
- `.edu` — образовательные организации;
- `.org` — организации, часто некоммерческие.

![Root](../../images//root.PNG)

## Типы DNS-записей

![Record](../../images//record.PNG)

- `A` — сопоставляет имя с IPv4-адресом;
- `AAAA` — сопоставляет имя с IPv6-адресом;
- `CNAME` — задаёт псевдоним: одно имя указывает на другое.

Проверить DNS-разрешение можно через `nslookup`:

```bash
$ nslookup www.google.com
Server: 8.8.8.8
Address: 8.8.8.8#53
Non-authoritative answer:
Name: www.google.com
Address: 172.217.0.132
```

Более подробную информацию показывает `dig`:

```bash
$ dig www.google.com
; <<>> DiG 9.10.3-P4-Ubuntu <<>> www.google.com
;; global options: +cmd
;; Got answer:
;; ->>HEADER<<- opcode: QUERY, status: NOERROR, id: 28065
;; flags: qr rd ra; QUERY: 1, ANSWER: 6, AUTHORITY: 0, ADDITIONAL: 1
;; QUESTION SECTION:
;www.google.com. IN A
;; ANSWER SECTION:
www.google.com. 245 IN A 64.233.177.103
;; Query time: 5 msec
;; SERVER: 8.8.8.8#53(8.8.8.8)
```

## Практическое задание

1. Добавьте тестовую запись в `/etc/hosts`.
2. Проверьте её через `ping`.
3. Посмотрите DNS-сервер в `/etc/resolv.conf`.
4. Проверьте порядок разрешения имён в `/etc/nsswitch.conf`.
5. Выполните `nslookup` и `dig` для одного домена.

## Контрольные вопросы

1. Чем `/etc/hosts` отличается от DNS?
2. Что означает строка `hosts: files dns`?
3. Чем запись `A` отличается от `CNAME`?
4. Когда удобнее использовать `dig`, а не `ping`?
