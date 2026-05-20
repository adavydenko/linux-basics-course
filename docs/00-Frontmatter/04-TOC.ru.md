<div class="toc">

# Оглавление

<ul>
<li class="lvl-1"><a href="#Настройка-окружения-для-лабораторных-работ">Настройка окружения для лабораторных работ<span class="toc-line"></span></a></li>

<li class="lvl-1" style="margin-top: 1.4em;">Часть I. Основы</li>
<li class="lvl-2"><a href="#Введение">Введение<span class="toc-line"></span></a></li>
<li class="lvl-2"><a href="#Введение-в-оболочку-linux">Введение в оболочку Linux<span class="toc-line"></span></a></li>
<li class="lvl-3"><a href="#Базовые-команды-linux">Базовые команды Linux<span class="toc-line"></span></a></li>
<li class="lvl-3"><a href="#Справка-в-командной-строке">Справка в командной строке<span class="toc-line"></span></a></li>
<li class="lvl-3"><a href="#Лабораторная-работа-оболочка-и-базовые-команды">Лабораторная работа: оболочка и базовые команды<span class="toc-line"></span></a></li>
<li class="lvl-3"><a href="#Оболочка-bash">Оболочка Bash<span class="toc-line"></span></a></li>
<li class="lvl-3"><a href="#Лабораторная-работа-bash">Лабораторная работа: Bash<span class="toc-line"></span></a></li>
<li class="lvl-2"><a href="#Ключевые-понятия-linux">Ключевые понятия Linux<span class="toc-line"></span></a></li>
<li class="lvl-3"><a href="#Работа-с-оборудованием">Работа с оборудованием<span class="toc-line"></span></a></li>
<li class="lvl-3"><a href="#Лабораторная-работа-ядро-linux">Лабораторная работа: ядро Linux<span class="toc-line"></span></a></li>
<li class="lvl-3"><a href="#Последовательность-загрузки-linux">Последовательность загрузки Linux<span class="toc-line"></span></a></li>
<li class="lvl-3"><a href="#Уровни-запуска-и-targets-systemd">Уровни запуска и targets systemd<span class="toc-line"></span></a></li>
<li class="lvl-3"><a href="#Типы-файлов-в-linux">Типы файлов в Linux<span class="toc-line"></span></a></li>
<li class="lvl-3"><a href="#Иерархия-файловой-системы">Иерархия файловой системы<span class="toc-line"></span></a></li>
<li class="lvl-3"><a href="#Лабораторная-работа-уровни-запуска-и-файловая-система">Лабораторная работа: уровни запуска и файловая система<span class="toc-line"></span></a></li>
<li class="lvl-2"><a href="#Дистрибутивы-и-пакетные-менеджеры">Дистрибутивы и пакетные менеджеры<span class="toc-line"></span></a></li>
<li class="lvl-3"><a href="#Пакетные-менеджеры-rpm-и-yum">Пакетные менеджеры RPM и YUM<span class="toc-line"></span></a></li>
<li class="lvl-3"><a href="#Лабораторная-работа-rpm-и-yum">Лабораторная работа: RPM и YUM<span class="toc-line"></span></a></li>
<li class="lvl-3"><a href="#Пакетные-менеджеры-dpkg-и-apt">Пакетные менеджеры DPKG и APT<span class="toc-line"></span></a></li>
<li class="lvl-3"><a href="#apt-и-apt-get">APT и APT-GET<span class="toc-line"></span></a></li>
<li class="lvl-3"><a href="#Лабораторная-работа-dpkg-и-apt">Лабораторная работа: DPKG и APT<span class="toc-line"></span></a></li>
<li class="lvl-2"><a href="#Архивация-и-сжатие-файлов">Архивация и сжатие файлов<span class="toc-line"></span></a></li>
<li class="lvl-3"><a href="#Поиск-файлов-и-шаблонов">Поиск файлов и шаблонов<span class="toc-line"></span></a></li>
<li class="lvl-3"><a href="#Перенаправление-ввода-вывода">Перенаправление ввода-вывода<span class="toc-line"></span></a></li>
<li class="lvl-3"><a href="#Лабораторная-работа-командная-строка-часть-ii">Лабораторная работа: командная строка, часть II<span class="toc-line"></span></a></li>
<li class="lvl-3"><a href="#Редактор-vi">Редактор Vi<span class="toc-line"></span></a></li>
<li class="lvl-3"><a href="#Лабораторная-работа-vi">Лабораторная работа: Vi<span class="toc-line"></span></a></li>

<li class="lvl-1" style="margin-top: 1.4em;">Часть II. Безопасность и сети</li>
<li class="lvl-2"><a href="#Учётные-записи-linux">Учётные записи Linux<span class="toc-line"></span></a></li>
<li class="lvl-3"><a href="#Управление-пользователями">Управление пользователями<span class="toc-line"></span></a></li>
<li class="lvl-3"><a href="#Файлы-управления-доступом">Файлы управления доступом<span class="toc-line"></span></a></li>
<li class="lvl-3"><a href="#Права-доступа-к-файлам">Права доступа к файлам<span class="toc-line"></span></a></li>
<li class="lvl-3"><a href="#ssh-и-scp">SSH и SCP<span class="toc-line"></span></a></li>
<li class="lvl-3"><a href="#iptables">IPtables<span class="toc-line"></span></a></li>
<li class="lvl-3"><a href="#cron-в-linux">Cron в Linux<span class="toc-line"></span></a></li>
<li class="lvl-2"><a href="#dns">DNS<span class="toc-line"></span></a></li>
<li class="lvl-3"><a href="#Основы-сети-коммутация-и-маршрутизация">Основы сети: коммутация и маршрутизация<span class="toc-line"></span></a></li>
<li class="lvl-3"><a href="#Диагностика-сетевых-проблем">Диагностика сетевых проблем<span class="toc-line"></span></a></li>

<li class="lvl-1" style="margin-top: 1.4em;">Часть III. Хранилища и службы</li>
<li class="lvl-2"><a href="#Диски-и-разделы">Диски и разделы<span class="toc-line"></span></a></li>
<li class="lvl-3"><a href="#Файловые-системы-в-linux">Файловые системы в Linux<span class="toc-line"></span></a></li>
<li class="lvl-3"><a href="#das-nas-и-san">DAS, NAS и SAN<span class="toc-line"></span></a></li>
<li class="lvl-3"><a href="#lvm-logical-volume-manager">LVM: Logical Volume Manager<span class="toc-line"></span></a></li>
<li class="lvl-2"><a href="#Создание-собственного-systemd-сервиса">Создание собственного systemd-сервиса<span class="toc-line"></span></a></li>
<li class="lvl-3"><a href="#Инструменты-systemd">Инструменты systemd<span class="toc-line"></span></a></li>
<li class="lvl-3"><a href="#Таймеры-systemd">Таймеры systemd<span class="toc-line"></span></a></li>
<li class="lvl-2"><a href="#Диагностика-среды-разработки">Демонстрационный кейс по диагностике<span class="toc-line"></span></a></li>

<li class="lvl-1" style="margin-top: 1.4em;">Часть IV. Автоматизация и эксплуатация</li>
<li class="lvl-2"><a href="#Работа-с-текстовыми-данными">Работа с текстовыми данными<span class="toc-line"></span></a></li>
<li class="lvl-2"><a href="#Скрипты-для-оболочки">Скрипты для оболочки<span class="toc-line"></span></a></li>
<li class="lvl-2"><a href="#Процессы-и-ресурсы">Процессы и ресурсы<span class="toc-line"></span></a></li>
<li class="lvl-2"><a href="#Удалённая-работа">Удалённая работа<span class="toc-line"></span></a></li>
<li class="lvl-2"><a href="#git-из-командной-строки">Git из командной строки<span class="toc-line"></span></a></li>
<li class="lvl-2"><a href="#python-из-командной-строки">Python из командной строки<span class="toc-line"></span></a></li>

<li class="lvl-1" style="margin-top: 1.4em;">Часть V. Современная сеть, контейнеры, диагностика</li>
<li class="lvl-2"><a href="#Современная-сеть-в-linux">Современная сеть в Linux<span class="toc-line"></span></a></li>
<li class="lvl-3"><a href="#Постоянная-сеть-netplan-и-networkmanager">Постоянная сеть: Netplan и NetworkManager<span class="toc-line"></span></a></li>
<li class="lvl-2"><a href="#Контейнеры-в-linux">Контейнеры в Linux<span class="toc-line"></span></a></li>
<li class="lvl-2"><a href="#Диагностика-linux">Диагностика Linux<span class="toc-line"></span></a></li>
<li class="lvl-2"><a href="#Итоговый-проект">Итоговый проект<span class="toc-line"></span></a></li>

<li class="lvl-1" style="margin-top: 1.4em;">Приложения</li>
<li class="lvl-2"><a href="#Глоссарий">Глоссарий<span class="toc-line"></span></a></li>
<li class="lvl-2"><a href="#Источники-и-рекомендуемая-литература">Источники и рекомендуемая литература<span class="toc-line"></span></a></li>
<li class="lvl-2"><a href="#Банк-упражнений">Банк упражнений<span class="toc-line"></span></a></li>
<li class="lvl-2"><a href="#Педагогический-аппарат-пособия">Педагогический аппарат пособия<span class="toc-line"></span></a></li>
<li class="lvl-2"><a href="#Методичка-преподавателя">Методичка преподавателя<span class="toc-line"></span></a></li>
<li class="lvl-2"><a href="#Приложение-Регулярные-выражения">Приложение. Регулярные выражения<span class="toc-line"></span></a></li>
<li class="lvl-2"><a href="#Приложение-Шпаргалка-по-командам-linux">Приложение. Шпаргалка по командам Linux<span class="toc-line"></span></a></li>
</ul>

</div>
