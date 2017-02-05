# short-url

A url shortening web application written using Python 3.6 and Django 1.10.2.

[anyz.me](http://www.anyz.me)


## Set up environment
```
git clone https://github.com/alanypz/link-shrink.git
virtualenv link-shrink -p python3
source link-shrink/bin/activate
```

Note that src/anyz/settings contains python modules for both local and production. The init file within the directory can be updated to modify priority.

## Heroku server

Run local instance of Heroku.
```
heroku local web
```

Deploy to remote Heroku server.
```
git push <heroku-git-link> master
```

## Local server

Install requirements before attempting to run server locally.
```
cd link-shrink/src
pip install requirements.txt
```

## Manage Django project
```
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```


