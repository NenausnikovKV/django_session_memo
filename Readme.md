Simple example of session using. Application has single page. 
It shows count of one session browsing.

## Install app 

### install django
```
sudo apt install python3-django
pip install django
```

### Migrate db migrations
I use django-default sqllite.
```
python manage.py migrate
```

### test app
```
python manage.py test
```

Run server on 8000 port
```
python manage.py runserver 8000
````

## Use app
### Browser 
Go to the url http://127.0.0.1:8000/session/ from your browser 
and update page. You have to see changing session counter after every page update

### Django client

Go to the Django shell 
```
python manage.py shell
```
and run the following code

```
from django.test import Client, TestCase
client = Client()
response = client.get("/session/")
response.content
```
After each get request you will be able to see new larger request count.
