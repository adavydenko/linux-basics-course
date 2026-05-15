# Основы Linux

Учебное пособие по базовой работе с Linux. Материал основан на конспектах курса [Linux Basics Course](https://bit.ly/3gGnxm0) от KodeKloud и адаптируется для русскоязычных студентов.

## Для кого этот курс

Курс рассчитан на студентов 2 курса факультета прикладной математики, которым нужно уверенно работать в Linux: запускать команды, ориентироваться в файловой системе, управлять пакетами, пользователями, правами доступа, сервисами, сетью и хранилищами.

После прохождения курса студент должен уметь:

- работать в командной строке без графического интерфейса;
- читать справку по командам и самостоятельно разбираться с опциями;
- выполнять типовые операции с файлами, каталогами, архивами и текстовыми данными;
- понимать базовую структуру Linux: ядро, процессы, файловая система, пользователи, права;
- устанавливать и обновлять пакеты;
- подключаться к удалённым машинам по SSH;
- диагностировать простые проблемы с сетью, сервисами и диском;
- оформлять результат лабораторной работы так, чтобы его можно было проверить.

## Статус русской версии

Русские материалы лежат рядом с оригиналами и имеют суффикс `.ru.md`.

На текущем этапе русская версия подготовлена для всех исходных уроков: у каждого англоязычного файла есть русская пара. Дополнительные разделы, добавленные для учебной программы, тоже включены в русское оглавление.

Перед публикацией студентам всё ещё полезно выполнить финальный редакторский проход:

- проверить единообразие терминов;
- убедиться, что примеры команд соответствуют используемому дистрибутиву и лабораторной среде;
- сохранены ли команды, пути, имена файлов и ссылки на изображения;
- уточнить критерии сдачи лабораторных работ;
- при необходимости добавить вводные комментарии к изображениям с английскими подписями.

## Правила перевода

- Команды, параметры, пути, имена файлов и вывод терминала не переводятся.
- При первом упоминании полезно давать английский термин в скобках: `оболочка (shell)`, `точка монтирования (mount point)`.
- Дальше в тексте используется русский термин.
- Заголовки должны быть понятными студенту, без лишнего капса.
- Если изображение содержит английские подписи, рядом в тексте нужно дать русское объяснение.
- Структуру русской версии желательно держать близкой к оригиналу, чтобы было проще сверять изменения.

## Рекомендуемая последовательность изучения

- [01. Введение](docs/01-Introduction/01-Introduction.ru.md)

- [02. Работа с командной строкой, часть I](docs/02-Working-With-Shell-Part-I)
  - [Введение в оболочку](docs/02-Working-With-Shell-Part-I/01-Introduction-to-Shell.ru.md)
  - [Базовые команды Linux](docs/02-Working-With-Shell-Part-I/02-Basic-Commands.ru.md)
  - [Справка в командной строке](docs/02-Working-With-Shell-Part-I/03-Command-Line-Help.ru.md)
  - [Лабораторная работа: оболочка и базовые команды](docs/02-Working-With-Shell-Part-I/04-lab-working-with-shell.ru.md)
  - [Оболочка Bash](docs/02-Working-With-Shell-Part-I/05-Bash-Shell.ru.md)
  - [Лабораторная работа: Bash](docs/02-Working-With-Shell-Part-I/06-Lab-Linux-Bash-Shell.ru.md)

- [03. Работа с командной строкой, часть II](docs/05-Working-With-Shell-Part-II)
  - [История: отставание от графика](<docs/05-Working-With-Shell-Part-II/01-Behind-Schedule(story).ru.md>)
  - [Архивация и сжатие файлов](docs/05-Working-With-Shell-Part-II/02-File-Compression-and-Archival.ru.md)
  - [Поиск файлов и шаблонов](docs/05-Working-With-Shell-Part-II/03-Searching-for-files-and-patterns.ru.md)
  - [Перенаправление ввода-вывода](docs/05-Working-With-Shell-Part-II/04-IO-Redirection.ru.md)
  - [Лабораторная работа: командная строка, часть II](docs/05-Working-With-Shell-Part-II/05-Lab-Working-With-Shell-Part-II.ru.md)
  - [Редактор Vi](docs/05-Working-With-Shell-Part-II/06-Vi-Editor.ru.md)
  - [Лабораторная работа: Vi](docs/05-Working-With-Shell-Part-II/07-Lab-VI-Editor.ru.md)
  - [03.5 Работа с текстовыми данными](docs/11-Text-Processing/01-Text-Processing.ru.md)
  - [03.6 Shell scripting](docs/12-Shell-Scripting/01-Shell-Scripting.ru.md)
  - [03.7 Python из командной строки](docs/16-Python-from-Command-Line/01-Python-from-Command-Line.ru.md)
  - [03.8 Git из командной строки](docs/15-Git-from-Command-Line/01-Git-from-Command-Line.ru.md)

- [04. Ключевые понятия Linux](docs/03-Linux-Core-Concepts)
  - [Первая рабочая встреча Боба](docs/03-Linux-Core-Concepts/01-Bobs-first-team-meeting.ru.md)
  - [Ядро Linux](docs/03-Linux-Core-Concepts/02-The-Linux-Kernel.ru.md)
  - [Работа с оборудованием](docs/03-Linux-Core-Concepts/03-Working-with-hardware.ru.md)
  - [Лабораторная работа: ядро Linux](docs/03-Linux-Core-Concepts/04-Lab-Linux-Kernel.ru.md)
  - [Последовательность загрузки Linux](docs/03-Linux-Core-Concepts/05-Linux-Boot-Sequence.ru.md)
  - [Уровни запуска и targets systemd](docs/03-Linux-Core-Concepts/06-Run-Levels.ru.md)
  - [Типы файлов в Linux](docs/03-Linux-Core-Concepts/07-File-Types.ru.md)
  - [Иерархия файловой системы](docs/03-Linux-Core-Concepts/08-Filesystem-Hierarchy.ru.md)
  - [Лабораторная работа: уровни запуска и файловая система](docs/03-Linux-Core-Concepts/09-Lab-Linux-RunLevels-Filesystem-Hierarchy.ru.md)

- [05. Управление пакетами](docs/04-Package-Mangement)
  - [Дистрибутивы и пакетные менеджеры](docs/04-Package-Mangement/01-Package-Management-Distribution.ru.md)
  - [RPM и YUM](docs/04-Package-Mangement/02-RPM-and-YUM.ru.md)
  - [Лабораторная работа: RPM и YUM](docs/04-Package-Mangement/03-Lab-RPM-and-YUM.ru.md)
  - [DPKG и APT](docs/04-Package-Mangement/04-DPKG-AND-APT.ru.md)
  - [APT и APT-GET](docs/04-Package-Mangement/05-APT-vs-APT-GET.ru.md)
  - [Лабораторная работа: DPKG и APT](docs/04-Package-Mangement/06-Lab-DPKG-AND-APT.ru.md)

- [06. Процессы и ресурсы](docs/13-Processes-and-Resources)
  - [Процессы и ресурсы](docs/13-Processes-and-Resources/01-Processes-and-Resources.ru.md)

- [07. Безопасность и права доступа](docs/06-Security-and-File-Permissions)
  - [История: инцидент безопасности](<docs/06-Security-and-File-Permissions/01-The-Security-Incident(story).ru.md>)
  - [Учётные записи Linux](docs/06-Security-and-File-Permissions/02-Linux-Accounts.ru.md)
  - [Управление пользователями](docs/06-Security-and-File-Permissions/03-User-Management.ru.md)
  - [Файлы управления доступом](docs/06-Security-and-File-Permissions/04-Access-Control-Files.ru.md)
  - [Права доступа к файлам](docs/06-Security-and-File-Permissions/05-File-Permissions.ru.md)
  - [SSH и SCP](docs/06-Security-and-File-Permissions/06-SSH-and-SCP.ru.md)
  - [IPtables](docs/06-Security-and-File-Permissions/07-IPtables.ru.md)
  - [Cron](docs/06-Security-and-File-Permissions/08-Cronjob.ru.md)
  - [07.1 Удалённая работа](docs/14-Remote-Work/01-Remote-Work.ru.md)

- [08. Сети](docs/07-Networking)
  - [История: сетевой инцидент](<docs/07-Networking/01-The-Network-Issue(story).ru.md>)
  - [DNS](docs/07-Networking/02-DNS.ru.md)
  - [Основы сети: switching и routing](docs/07-Networking/03-Networking-Basics.ru.md)
  - [Диагностика сетевых проблем](docs/07-Networking/04-Troubleshooting.ru.md)
  - [08.1 Современная сеть в Linux](docs/17-Modern-Networking/01-Modern-Networking.ru.md)

- [09. Хранилища в Linux](docs/08-Storage-in-Linux)
  - [Где находится моё хранилище?](docs/08-Storage-in-Linux/01-Where's-my-Storage.ru.md)
  - [Диски и разделы](docs/08-Storage-in-Linux/02-Storage-Basics.ru.md)
  - [Файловые системы в Linux](docs/08-Storage-in-Linux/03-File-System-in-Linux.ru.md)
  - [DAS, NAS и SAN](docs/08-Storage-in-Linux/04-DAS-NAS-and-SAN.ru.md)
  - [LVM](docs/08-Storage-in-Linux/05-LVM.ru.md)
  - [Статусная встреча проекта](docs/08-Storage-in-Linux/06-Project-Status-Meeting.ru.md)

- Дополнительные топики
  - [Управление сервисами с systemd](docs/09-Service-management-with-SYSTEMD)
  - [История: работа сверхурочно](docs/09-Service-management-with-SYSTEMD/01-Working-Overtime-Story.ru.md)
  - [Создание собственного systemd-сервиса](docs/09-Service-management-with-SYSTEMD/02-Creating-a-SYSTEMD-Service.ru.md)
  - [Инструменты systemd](docs/09-Service-management-with-SYSTEMD/03-SYSTEMD-Tools.ru.md)
  - [Контейнеры в Linux](docs/18-Linux-Containers/01-Linux-Containers.ru.md)

- [10. Финальный практикум](docs/10-The-Client-Demonstration)
  - [10.1 Диагностика Linux](docs/19-Diagnostics/01-Diagnostics.ru.md)
  - [История: демонстрация под угрозой](<docs/10-The-Client-Demonstration/01-Client-Demonstration-in-Jeopardy!(story).ru.md>)
  - [10.2 Демонстрационный troubleshooting-кейс](docs/10-The-Client-Demonstration/02-Troubleshoot-the-Development-Environment.ru.md)
  - [Финал](<docs/10-The-Client-Demonstration/03-Finale(story).ru.md>)
  - [10.3 Итоговый проект](docs/20-Final-Project/01-Final-Project.ru.md)
