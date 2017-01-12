# short-url

Written using Python 3.6 and Django 1.10.2.

## Testing Locally

Set up and activate virtual env.
```
virtualenv <local-path> -p python3
cd <local-path>
source bin/activate
```

Install requirements.
```
pip install django==1.10.2
```

Manage project
```
cd src
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

Available at port :8000