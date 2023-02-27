# api_final
# Проект «API для Yatube»

### В данном работе при помощи Django REST Framework я создаю  REST API для собственного приложения Yatube

### Совокупность всех описанных мной эндпоинтов позволит работать приложению с другими приложениями, телеграмм-ботом, или с Frontend - приложением.

### В проекте использованы технологии: Python 3.8, Django 3.2, DRF, JWT + Djoser

## Как запустить проект:

Клонировать репозиторий и перейти в него в командной строке:

```
git clone https://github.com/MartiAndrew/api_final_yatube.git
```

```
cd api_final_yatube
```

Cоздать и активировать виртуальное окружение:

```
python -m venv env
```

```
source venv/scripts/activate
```

Установить зависимости из файла requirements.txt:

```
python -m pip install --upgrade pip
```

```
pip install -r requirements.txt
```

Выполнить миграции:

```
python manage.py migrate
```

Запустить проект:

```
python manage.py runserver
```

## Примеры работы с API 

Для неавторизованных пользователей работа с API доступна в режиме чтения.

```r
GET api/v1/posts/ - получить список всех публикаций.
При указании параметров limit и offset выдача должна работать с пагинацией
GET api/v1/posts/{id}/ - получение публикации по id
GET api/v1/groups/ - получение списка доступных сообществ
GET api/v1/groups/{id}/ - получение информации о сообществе по id
GET api/v1/{post_id}/comments/ - получение всех комментариев к публикации
GET api/v1/{post_id}/comments/{id}/ - Получение комментария к публикации по id
```
Автор: [Андрей Мишков](https://github.com/MartiAndrew)