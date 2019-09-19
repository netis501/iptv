# IPtvDream 4X
[![](https://img.shields.io/bitbucket/pipelines/iptvdream/iptvdream-4x.svg)](https://bitbucket.org/iptvdream/iptvdream-4x/addon/pipelines/home)

Плагин для просмотра iptv на ресивeрах (тв-приставках) с enigma2.
*NO WARRANTIES[*](#markdown-header-no-warranties) (Отказ от ответственности)[*](#markdown-header-no-warranties)*.

[![](https://c5.patreon.com/external/logo/become_a_patron_button.png)](https://www.patreon.com/iptvdream4x)

Отчёты об ошибках, пожелания, предложения, пулл-реквесты и прочая помощь приветствуется!

# Release notes

## 4.46

- поддержка логотипов каналов для совок

## 4.45

- исправлены мелкие ошибке в скине

## 4.44

- исправлен крэш на дмм
- исправлен крэш на некоторых провайдерах

## 4.43

- добавлены логотипы каналов в инфобарe
- небольшие улучшения скина

## 4.42

- исправление крэша на атв прошивке

## 4.41

- добавлено онли4тв, спасибо @soveni

## 4.40

- немецкая локализация
- сохранение фаворитов для совок

## 4.39

- добавлены пункты в меню для открытия настроек и для очистки логина + пароля

## 4.38

- исправлен крэш при неверно выставленной дате

## 4.37

- исправлен крэш на некоторых прошивках

## 4.36

- добавлен выбор аудио дорожки
- обновлён перевод

## 4.35

- исправлен крэш при выборе keymap

## 4.34

- для эдем используется лайт плейлист, можно выбрать полный по кнопке меню находясь в списке каналов

## 4.33

- убрана пауза при вводе численного кода
- поддержка настроек на стороне апи: выбор сервера, выбор качества

## 4.32

- исправлен крэш при первом старте плагина

## 4.31

- исправлена обработка исключений в епг кеше
- id каналов m3u определяются из урл (более стабильный список избранное)
- список провайдеров отсортирован по имени
- убран эдем-yahan, используйте эдем-soveni

## 4.30

- исправлен крэш

## 4.29

- Старые хорошие фичи снова на месте:
    - Упорядочивание избранного
    - Выбор сортировки списка каналов
- Установка зависимостей при старте: json, html, exteplayer3, ServiceApp
- Добавлено новое-тв 

## 4.28

- упрощена навигация по архиву

## 4.27

- откат изменений

## 4.26

- каналы с одинаковым tvg-id для иптв-е2 и шура
- авто обновление тв - программы в списке каналов (нужно тестирование)

## 4.25

- исправлен оттклуб

## 4.24

- исправлено епг на каналах с одинаковым tvg-id
- отдельное окно для детального епг
- обновление прогрессбара в окне "епг по дням"

## 4.23

- исправлен кингмод

## 4.22

- Добавлен кинобум
- Добавлен кингмод
- Поддержка буквенных tvg-id в xmltv

## 4.21

- Добавлена картина тв
- Исправлен крэш в настройках
- Начальная реализация обновления прогресса в списке епг

## 4.20

- Исправлено сохранение favourites

## 4.19

- Добавлено pure

## 4.18

- Добавлен Эмигрант тв
- Добавлено Амиго тв
- Добавлено iptv-e2 от Совени

## 4.17

- исправлена нумерация каналов совок.тв
- отображение даты окончания подписки для наше.тв и др.

## 4.16

- исправлено имя плагина в сообщениях об ошибке
- изменён урл епг

## 4.15

- добавлена Шура
- исправлено листание групп кнопками Букет+/Букет-

## 4.14

- добавлены не достающие логотипы
- изменён урл обновления

## 4.13

- исправилены потерянные файлы

## 4.12

- добавлено лого балтик, спасибо Tall
- добавлен едем с источником епг от совени
- добавлен оттклуб с источником епг от яхан

## 4.11

- добавлен baltic.tv

## 4.10

- сделал сборку deb (надо протестировать)
- добавлен редирект на динамические ссылки для радуги, совок и другие для использования в букетах.
  Формат: http://localhost:9001/PROVIDER/CHANNEL_ID

## 4.9

- добавили новый иптв провайдер

## 4.8

- добавлено озо, миви, наше (спасибо freeuser)
- поддержка фуллшд скина
- запрещен повторный вход в плагин

## 4.7

- исправлен крэш при загрузке епг

## 4.6

- ввод букв в логин-пароль по синей кнопке
- исправлен крэш едема при отсутствии интернета
- добавлена радуга и телепром
- выход из плагина по кнопке экзит

## 4.5

- Поддержка избранных каналов
- Возможность выбора двух типов управления (enigma и neutrino)
- Улучшение интерфейса
- Исправление багов

## 4.4

- beta релиз

## 4.3

- Первая версия 4X


# *NO WARRANTIES.
*Authors are not responsible for the media streams content which one can access with this plugin.*
The plugin serves as an advanced media player.
The software provides graphical user interface to see teleguide and watch OTT media streams.
REST API implementation for specific media providers are contributed in the open source manner.
When using this plugin user is responsible to check that content from the corresponding provider
does not violate any international and local laws including copyright laws.
See `LICENSE` file for more info.


# *ОТКАЗ ОТ ОТВЕТСТВЕННОСТИ.
*Авторы не несут ответственности за медиа потоки доступные через этот плагин.*
Плагин является медиаплеером с расширенными возможностями.
Это программное обеспечение предоставляет графический интерфейс для доступа к программе телепередач и OTT медиа потокам.
Имплементации REST API для конкретных медиа провайдеров вносятся в рамках проекта с открытым исходным кодом.
При использовании плагина пользователь должен удостоверится что медиа контент соответствующего провайдера
не нарушает международных и местных законов включая законы о защите авторских прав.
Смотрите файл `LICENSE` для более детальной информации.
