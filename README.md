# Проект Product_api

## Описание

 Приложение для взаимодействия с товарами.

## Возможности

- Получить список товаров
- Добавить товар

## Технологии

- Python 3.9.10
- Django 4.2.16
- Django Rest Framework 3.15.2
- подробнее см. прилагаемый файл зависимостей requrements.txt

## Установка

Клонировать репозиторий и перейти в него в командной строке:

```bash
git clone git@github.com:Alimovriq/product_api.git
```

```bash
cd product_api
```

Cоздать и активировать виртуальное окружение:

```bash
python3 -m venv env
```

```bash
source env/bin/activate
```

Установить зависимости из файла requirements.txt:

```bash
python3 -m pip install --upgrade pip
```

```bash
pip install -r requirements.txt
```

Выполнить миграции:

```bash
python3 manage.py makemigrations
```

```bash
python3 manage.py migrate
```

Собрать статику:

```bash
python3 manage.py collectstatic
```

Запустить проект:

```bash
python3 manage.py runserver
```

### Автор

Алимов Ринат
<https://github.com/Alimovriq>
