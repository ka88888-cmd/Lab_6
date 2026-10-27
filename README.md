**ФИО:** Гончарова Екатерина Ивановна
**Группа:** 221141
**Вариант:** 9  
**Лабораторная:** №6

## Задания и файлы

| Задание | Файл | Описание |
|---------|------|----------|
| Среднее 1 | flask_hello.py | Flask-приложение «Hello World» |
| Среднее 9 | jinja_template.py, templates/index.html | Шаблон Jinja2 с данными |
| Среднее 6 | fastapi_hello.py | FastAPI «Hello» |
| Повышенное 9 | sqlalchemy_app.py | Подключение SQLAlchemy к SQLite |
| Повышенное 2 | fastapi_db.py | FastAPI с базой данных SQLite |

## Запуск

```bash
pip install -r requirements.txt

python flask_hello.py          # http://127.0.0.1:5000
python jinja_template.py       # http://127.0.0.1:5000
python fastapi_hello.py        # http://127.0.0.1:8000/docs
python sqlalchemy_app.py
python fastapi_db.py           # http://127.0.0.1:8001/docs

```