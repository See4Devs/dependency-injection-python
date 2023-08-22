# Dependency Injection examples with Django, FastAPI and Flask

This is a sample project on how to use Dependency Injection with popular frameworks : Django, FastAPI and Flask

## How to Run the Django Application

```bash
pip3 install Django django-injector
cd django_di_project
python3 manage.py runserver
```

![Django Application](https://i.imgur.com/rNmNXYv.png)

## How to Run the Flask Application

```bash
pip3 install Flask Flask-Injector
cd flask_di_project
python3 app.py
```

![Flask Application](https://i.imgur.com/0pyhFZv.png)

## How to Run the FastAPI Application

```bash
pip3 install fastapi uvicorn
cd fast_di_project
uvicorn main:app --reload
```

![FastAPI Application](https://i.imgur.com/JFY2YIP.png)
