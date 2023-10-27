```sh
python -m venv venv
.\venv\Scripts\activate.ps1

# install django
.\venv\Scripts\pip install django

# verif install et version
django-admin --version

# demarrer un projet
django-admin startproject config .

# ajouter l'app
django-admin startapp www  # ("www" nom de l'app)

# configurer la base de données
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser

# test fonctionnement / lancer l'app
python manage.py runserver

```

title
content
published_at
user
status (DF, PB, CL)
category 1-N
tags N-N
icon / cover (images)

commentaire = exo

```sh
.\venv\Scripts\pip install Pillow

python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```

# Importer des données

- Utiliser Sqlite3 en direct ( pas bonne idée )
- se greffer sur django dans un script à part

```sh
.\venv\Scripts\pip install django-extensions
.\venv\Scripts\pip install pydotplus

.\venv\Scripts\python manage.py graph_models -a -o models.png # marche pas
.\venv\Scripts\python manaython manage.py graph_models -a -o models.png # marche encore moins
```

- créer un fichier import.py
  - importer nos models Articles, Categories, Tags
  - charger les données de l'API
  - pour chaque
    - instancier un Articles, affectr les valeurs, save
    - charger les images, attacher aux articles
    - tags
- 'python manage.py runscript import.py'

# Rendu routage url / templates

- templates/
  - base.html
- siteApp/templates/
  - list.html
  - single.html
  - categ.html
  - tags.html
