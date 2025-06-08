# Документация DH|Education

## Описание

Данный пакет предназначен для образовательной платформы DH

## Установка

```commandline
poetry add git+https://github.com/JohnSoi/dh-education.git
```

Если планируется активное разработка в пакете, то лучше добавить локальную зависимость:
```commandline
poetry add ../dh-education --group dev
```


## Состав

<pre>
dh_education
├── models
├── consts
├── main
└── settings
</pre>

## Полезные команды 

* Запуск сервера

```bash
uvicorn dh_education.main:app --reload
```

* Создание миграции:  
```bash  
poetry run alembic revision --autogenerate -m "Create contact table"
```

*Обновление БД:  
```bash  
poetry run alembic upgrade head
```
