
####  Приложение для получение всех типов HTML тегов с определенной страницы.

#### API:

*POST: : localhost/tags/

BODY : { url :<site_url>}

RESPONSE: 201, “task_id”

*GET: localhost/tags/<task_id>

RESPONSE: 200, { HTML_tags : [] }


#### Для правильной работы приложения:

- Python 3.5 >

- Redis

#### Для старта выполните следующие действия:

- Необходимо создать и активировать виртуальное окружение:
```http
  python3 -m venv {name}
```
```http
  source venv/bin/activate
```
- Загрузить код данного приложения

- Запустить скрипт `start_app.sh`(подгрузятся необходимые пакеты и запустится сервер)

- В случае обновления кода для того чтобы обновить зависимости и провести синтаксическую проверку, запустите `update_req_and_lint.sh`.
