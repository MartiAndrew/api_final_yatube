# api_final
# Проект «API для Yatube»

### В данной работе при помощи Django REST Framework я создаю  REST API для собственного приложения Yatube

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
python -m venv venv
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

## Примеры ответов от эндпоинтов

### Request 1: ```POST http://127.0.0.1:8000/api/v1/users/```
                {
                    "username": "testuser1",
                    "password": "Pass1111"
                }
### Response 1:     
                {
                    "email": "",
                    "username": "testuser1",
                    "id": 3
                }

### Request 2: ```POST http://127.0.0.1:8000/api/v1/posts/```
                {
                    "text": "пост тест1"
                }
### Response 2:     
                {
                    "id": 1,
                    "author": "testuser1",
                    "text": "пост тест1",
                    "pub_date": "2023-03-01T21:45:04.057617Z",
                    "image": null,
                    "group": null
                }

### Request 3: ```GET http://127.0.0.1:8000/api/v1/groups/```

### Response 3:     
                {
                    "id": 1,
                    "title": "diary",
                    "slug": "notes",
                    "description": "daily maily"
                }

### Request 4: ```POST http://127.0.0.1:8000/api/v1/posts/1/comments/```
                {
                    "text": "Не уверен!"
                }
### Response 4:     
                {
                        "id": 1,
                        "author": "testuser1",
                        "text": "Не уверен!",
                        "created": "2023-03-01T22:05:15.630813Z",
                        "post": 1
                }

### Request 5: ```POST http://127.0.0.1:8000/api/v1/follow/```
                {
                    "following": "Marti"
                }

### Response 5:     
               {
                    "id": 1,
                    "user": "testuser1",
                    "following": "Marti"
               }

Автор: [Андрей Мишков](https://github.com/MartiAndrew)