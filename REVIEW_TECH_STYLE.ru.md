# Сквозная ревизия: стиль и техника

## Задача 1. Стилистические дефекты

### Модуль 00 — Lab Environment
- `01-Lab-Environment-Setup.ru.md:21` — заголовок «Что понадобится» открывается строкой `Установленный Docker. Проверить, что он работает:` и сразу командой — нет вводного абзаца.
- `:84` — раздел «Когда команды требуют `sudo`» местами в «обзывающем» стиле без объяснения, в каких случаях `sudo` срабатывает не на любой команде (alias, builtin).

### Модуль 02 — Shell I
- `02-Basic-Commands.ru.md:18` — раздел открывается командой без отдельного мотивирующего абзаца.
- `:127` — подраздел «Альтернатива cd: стек каталогов» использует англ. термины `pushd`/`popd` без русского эквивалента в скобках.
- `05-Bash-Shell.ru.md:21` — после H2 «Виды оболочек» сразу маркированный список — нужно одно предложение «зачем это знать».
- `:38` — `chsh` (change shell) — расшифровано «change shell», но не указано «изменить оболочку».
- `:119` — раздел «Переменная PATH» строится «вот так делается X» без сцены, зачем.

### Модуль 03 — Linux Core
- `02-The-Linux-Kernel.ru.md:65` — таблица расшифровки `4.15.0-72-generic` показывает `15` как «major», но текст выше уже использует «старшая (major)» без расшифровки.
- `03-Working-with-hardware.ru.md:42` — `udev` (user-space device manager) при первом упоминании не расшифрован.
- `04-Lab-Linux-Kernel.ru.md` — в шагах 2–3 «текстовые ответы» в кодовых блоках выглядят как команды.
- `06-Run-Levels.ru.md:18` — мотивирующий абзац идёт после заголовка «Systemd targets», оригинальный поясняющий абзац перед «Цели раздела» отсутствует.
- `07-File-Types.ru.md:13` — кавычки `"всё является файлом"` ASCII вместо «ёлочек».
- `09-Lab-Linux-RunLevels-Filesystem-Hierarchy.ru.md:24` — `sudo ls /root` без пояснения, какие лабораторные предполагаются от пользователя `bob` или `student`.

### Модуль 04 — Пакеты
- `02-RPM-and-YUM.ru.md:20` — «RPM-based дистрибутивы» без русского варианта («дистрибутивы на базе RPM»).
- `:84` — последовательность из шести команд `yum repolist`, `yum provides scp`, `yum install httpd`, и т.д. почти без сюжетной связки.
- `03-Lab-RPM-and-YUM.ru.md:33` — `firefox-68.6.0-1.el7.centos.x86_64.rpm` устаревшее (2019), но это не помечено как «учебный пример».
- `04-DPKG-AND-APT.ru.md:19` — расшифровка «Debian Package — Debian Package Manager» избыточна и нелогична.

### Модуль 05 — Shell II
- `02-File-Compression-and-Archival.ru.md:78` — «tarball» введён без русского эквивалента.
- `03-Searching-for-files-and-patterns.ru.md:96` — раздел «Поиск целого слова» открывается командой без пояснительного абзаца.
- `07-Lab-VI-Editor.ru.md:23` — текстовый «ответ» в кодовом блоке `Нажмите i` визуально читается как команда оболочки.

### Модуль 06 — Безопасность
- `02-Linux-Accounts.ru.md:46` — последовательность `cat /etc/passwd`, `cat /etc/group`, `id michael`, `grep ... /etc/passwd` идёт без логических связок.
- `:67` — `last` показывает выходы тоже, не только входы — описание неполное.
- `05-File-Permissions.ru.md:55` — раздел «Изменение прав: chmod» начинается сразу с подраздела «Символьная форма» — нет промежуточного предложения между общим описанием и таблицей.
- `06-SSH-and-SCP.ru.md` — отсутствует раздел «Практическое задание», нарушает единый формат модуля.
- `07-IPtables.ru.md:67` — последовательность правил без сюжетной связки между двумя командами.

### Модуль 07 — Сеть
- `02-DNS.ru.md` — везде использован `bash`-fenced код, а в остальном пособии — `shell`. Несоответствие.
- `:99` — раздел «Типы DNS-записей» открывается списком без вводного абзаца.

### Модуль 08 — Хранилища
- `02-Storage-Basics.ru.md:14` — `MBR` и `GPT` в целях раздела упомянуты не расшифрованными; `MBR` так и не расшифрован полностью (Master Boot Record).
- `:53` — раздел «Создание разделов» сразу даёт `sudo gdisk /dev/sdb` без объяснения, какой диск брать в учебном окружении.
- `03-File-System-in-Linux.ru.md:34` — переход от `mkfs.ext4` к `mkdir /mnt/ext4` без связующего абзаца — стиль «команда → команда».
- `04-DAS-NAS-and-SAN.ru.md:21` — `Fibre Channel` упомянут без перевода/пояснения.
- `05-LVM.ru.md` — отсутствует секции «Практическое задание» и единый формат сдачи.

### Модуль 09 — Systemd
- `02-Creating-a-SYSTEMD-Service.ru.md:67` — раздел `[Install]` в «обзывающем» тоне, без объяснения деталей `Wants=`/`Requires=`.
- `03-SYSTEMD-Tools.ru.md:121` — секциям `journalctl` не хватает связки «зачем именно `-b`», `--since` и `-u` — следуют одна за другой без переходов.

### Модули 11–20
- Модули 11, 12, 13, 14, 15, 17, 18 — отсутствует маркер `[English] | **Русский**` (сквозной дефект).
- `11-Text-Processing/01-Text-Processing.ru.md` — в нём «вы» вперемешку с безличными формами.
- `12-Shell-Scripting/01-Shell-Scripting.ru.md:18` — раздел «Первый скрипт» начинается с команды без вводной строки.
- `:121` — `set -euo pipefail` объясняется одной фразой без явной расшифровки `-e -u -o`.
- `13-Processes-and-Resources/01-Processes-and-Resources.ru.md:99` — раздел «Долгие задачи» сразу `nohup` без напоминания, что такое сессия.
- `16-Python-from-Command-Line/01-Python-from-Command-Line.ru.md:67` — `venv` без «virtual environment» в скобках при первом упоминании в заголовке.
- `17-Modern-Networking/01-Modern-Networking.ru.md:3` — упомянут «iproute2» без расшифровки/пояснения.
- `:75` — abbr `nftables`, `ufw`, `firewalld` маркированным списком без вводного предложения после заголовка.
- `18-Linux-Containers/01-Linux-Containers.ru.md:17` — «namespaces» и «cgroups» расшифрованы, но «bind mount» — заголовок без русского эквивалента в скобках.
- `19-Diagnostics/01-Diagnostics.ru.md:30` — последовательность `journalctl` без связок (три варианта подряд).
- `20-Final-Project/01-Final-Project.ru.md:3` — первый абзац опечатка: «реальную работу не складывается» (несогласовано).
- `21-Appendix-Cheat-Sheet/01-Command-Cheat-Sheet.ru.md` — раздел «Редактор vi» содержит обозначения клавиш без вводного абзаца.

## Задача 2. Технические дефекты

1. `04/03-Lab-RPM-and-YUM.ru.md:34` — `firefox-68.6.0-1.el7.centos.x86_64.rpm` — Lab требует RHEL/CentOS, а курс на Ubuntu 22.04; нужна оговорка.
2. `04/06-Lab-DPKG-AND-APT.ru.md:38` — `apt search chromium-browser` ищет с конкретным именем; пользователь имени не знает — нужен `apt search chromium`.
3. `04/04-DPKG-AND-APT.ru.md:75` — `sudo apt edit-sources` в Ubuntu 22.04+: основной `sources.list` пустой, всё в `sources.list.d/`.
4. `04/04-DPKG-AND-APT.ru.md:101` — `sudo apt list | grep telnet` — без `--installed` выводит всё с предупреждением «WARNING: apt does not have a stable CLI interface».
5. `06/06-SSH-and-SCP.ru.md:57` — `ssh-keygen -t rsa` устаревший; в модуле 14 уже рекомендован `ed25519` — нестыковка.
6. `06/06-SSH-and-SCP.ru.md:49` — путь `/home/bob/.ssh/id_rsa.pub`; для `ed25519` будет `id_ed25519.pub`.
7. `06/02-Linux-Accounts.ru.md:119` — `root` с `/usr/sbin/nologin` — в реальности root так не блокируют.
8. `06/03-User-Management.ru.md:23` — `useradd bob` без `sudo` — без прав root завершится ошибкой.
9. `06/03-User-Management.ru.md:46` — `passwd bob` без `sudo` для чужого пароля не сработает.
10. `06/03-User-Management.ru.md:65` — `useradd -u 1009 -g 1009 ...` без `sudo`.
11. `06/05-File-Permissions.ru.md:46` — пример `cd /home/bob/random_dir` для проверки `x`-бита не убедителен.
12. `06/07-IPtables.ru.md:36` — `sudo apt install iptables` — на Ubuntu 22.04 стоит по умолчанию.
13. `07/02-DNS.ru.md:25` — пример вывода `ping` в Windows-формате (`Reply from ... TTL=117`), не Linux.
14. `07/03-Networking-Basics.ru.md:33` — `ip addr add 192.168.1.10/24 dev eth0` без `sudo`.
15. `07/03-Networking-Basics.ru.md:62` — `ip route add 192.168.2.0/24 via 192.168.1.1` без `sudo`.
16. `07/03-Networking-Basics.ru.md:45` — `route` без оговорки «устаревшая команда, в Ubuntu 22.04 не установлена по умолчанию».
17. `07/04-Troubleshooting.ru.md:82` — `netstat` оставлен как «старый материал»; стоит явно отметить, что `net-tools` не установлен.
18. `07/04-Troubleshooting.ru.md:98` — `ip link set dev enp1s0f1 up` без `sudo`.
19. `08/03-File-System-in-Linux.ru.md:58` — пример `/etc/fstab` с `errors=panic` опасен; в Ubuntu стандарт `errors=remount-ro`.
20. `08/03-File-System-in-Linux.ru.md:64` — `rw 0 0` — обычно `defaults`.
21. `08/02-Storage-Basics.ru.md:34` — «major=8» — для NVMe major=259; стоит оговорить.
22. `08/05-LVM.ru.md:37` — `sudo apt-get install lvm2` — в курсе договорено использовать `apt`.
23. `08/04-DAS-NAS-and-SAN.ru.md:22` — «NAS близко к NFS-серверу» — формулировка спорная.
24. `09/02-Creating-a-SYSTEMD-Service.ru.md:71` — `WantedBy=graphical.target` для серверного сценария лучше `multi-user.target`.
25. `13/01-Processes-and-Resources.ru.md:87` — `nice -n 10 long-task.sh` — без `./` команда не запустится.
26. `13/01-Processes-and-Resources.ru.md:96` — `renice -n 10 -p 12345` — без `sudo` поднимать `nice` обратно нельзя.
27. `17/01-Modern-Networking.ru.md:84` — `python3 -m http.server 8000` — `python3` может быть не установлен.
28. `19/01-Diagnostics.ru.md:73` — `ps aux --sort=-%mem | head` — `--sort` GNU расширение, стоит упомянуть.
29. `04/05-APT-vs-APT-GET.ru.md:24` — «Пример установки» обещает сравнить через apt и apt-get, но реальных команд нет.
30. `06/08-Cronjob.ru.md:82` — `crontab -v` помечена как «нестандартная»; в Linux не работает — стоит явно написать.
31. `02/05-Bash-Shell.ru.md:33` — `chsh` без `sudo` для своей оболочки работает, для другого пользователя — нет; подаётся универсально.

## Задача 3. Визуальные дефекты SVG

Проверены 25+ SVG. Палитра выдержана. Тексты не обрезаются, но точечные замечания:

1. `ru_partition.svg` — «Primary Partition 1/2/3/4», «Extended Partition» — англ. внутри схемы при русском заголовке.
2. `ru_run-levels.svg` — `runlevel 5` / `runlevel 3` — кода-метка без расшифровки в схеме.
3. `ru_systemctl.svg` — «Units» английское слово без русского пояснения.
4. `ru_site.svg` — «Repository Server» англ., в тексте — «сервер репозитория».
5. `ru_io.svg` — `stdin/stdout/stderr` + русские пояснения — допустимо, но визуально неоднородно.
6. `ru_lvm.svg` — «LV» без расшифровки в схеме (есть только в заголовке).
7. `ru_perm.svg` — «Назначение» — «чтение/запись/выполнение» без англ. `read/write/execute`.
8. `ru_vi.svg` — «Last line» англ., в тексте — «Режим последней строки».
9. `ru_filesystem.svg` — в схеме отсутствует `/root`, упомянутый в тексте.

## Общая рекомендация по SVG

Привести все англоязычные слова внутри схем (`Primary Partition`, `Extended Partition`, `Last line`, `Units`, `Repository Server`) к единому стилю: либо двойная подпись (рус. + англ. в скобках), либо только русская + англ. вариант оставить только в коде/команде.

В `ru_filesystem.svg` добавить `/root`.

## Итог

Стилистическая однообразность нарушена: вычитанные модули 02, 03, 05, 06, 07 заметно отличаются от 11–20 по тону и оформлению. Технические недоработки сосредоточены в модулях 06–08 (забытый `sudo`, устаревшие опции, неверные примеры вывода). SVG в целом выдержаны, но имеют точечные англоязычные островки.
