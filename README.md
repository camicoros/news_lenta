# Новостная лента
для входа в админку:
```
login: root 
password: root
```
### Запуск проекта из docker
```
docker build -t news .
docker run --name news -it -p 8000:8000 news
```
### Заполнение тестовыми данными
```
python manage.py loaddata dump.json
```

### Автор
Саушкин Денис