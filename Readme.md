Приложение для получение всех типов HTML тегов с определенной страницы.

API:

*POST: : localhost/tags/
BODY : { url :<site_url>} 
RESPONSE: 201, “task_id”

*GET: localhost/tags/<task_id>
RESPONSE: 200, { HTML_tags : [<list of tags>] }

В результате получаете количество и все типы тегов.

Для правильной работы приложения:

*Python 3.5 >

*Redis

Для старта выполните следующие действия:

1. Необходимо создать и активировать виртуальное окружение:
- python3 -m venv {name} - создание;
- source venv/bin/activate - активация;
2. Загрузить код данного приложения
3. Запустить скрипт 'start_app.sh' и запустить скрипт(подгрузятся необходимые пакеты и запустится сервер)
