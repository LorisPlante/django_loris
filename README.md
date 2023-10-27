```sh
python -m venv venv
.venv\Scripts\activate.ps1

# install django
.\venv\Scripts\pip install django

# verif install et version
django-admin --version

# demarrer un projet
django-admin startproject config .

# ajouter l'app
django-admin startapp www  # ("www" nom de l'app)



# test fonctionnement / lancer l'app
python manage.py runserver


# configurer la base de données
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser

```
