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

# ---- CRÉER UNE PROJET ----

## installation et lignes de commande en général

- configurer un Github
  - gitignore :
    - venv
    - sqlite (sauf si interro)
- créer un fichier requirements.txt
  - maintenir à jour à chaque "pip install"

```sh
.\venv\Scripts\pip freeze > requirements.txt
# instller depuis le fichier requirements.txt
.\venv\Scripts\pip install -r requirements.txt

# démarage du projet
# config/settings.py : DATABASES = {}
django-admin startproject config .

# configurer la base de données : tables systèmes
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser

# ajouter l'app
django-admin start app siteApp # 'siteApp' nom de l'app actuel

# lancer le serveur
python manage.py runserver

# arreter le serveur : CTRL + C

# si modif des models
python manage.py makemigrations
python manage.py migrate

# de temps à autre... (import de données)
python manage.py ....

# export
.\venv\Scripts\python manage.py dumpdata > db.json
.\venv\Scripts\python manage.py dumpdata auth.user > user.json
.\venv\Scripts\python manage.py dumpdata --exclude auth.permission > db.json

#import
manage.py loaddate db.json

#changer de mot de passe pour un user

.\venv\Scripts\python manage.py changepassword loris # 'loris' est le nom du user
```

## le projet et ses fichiers

| fichier              | rôle                              |
| -------------------- | --------------------------------- |
| config/setting.py    | réglages globaux                  |
| config/urls.py       | routes                            |
| templates/           | template globaux                  |
| siteApp/             | notre app                         |
| siteApp/models.py    | ORM classes "base de données"     |
| siteApp/admin.py     | déclarer pour l'interface d'admin |
| siteApp/views.py     | les vues (liées aux models)       |
| siteApp/urls.py      | routes (liées aux vues)           |
| siteApp/templates.py |                                   |

models -> views -> urls

### réglages globaux

### routes

- routes globales `config/urls.py`
  - chemin vers l'admin
  - gestion des médias (MEDIA_URL)
  - importer les routes locales
- routes locales

### models

- definition des `class Categories(models.Model):`
- liste des "attibuts"
  `content = models.TextField("Contenu", blank=True)`

  - types
    - champs "standards" : TextField, CharField, DateTimeField, SlugField ....
    - champs "automatiques" : id, DateTimeField (auto_now_add, auto_now)
    - champs "pièces jointes" : images, fichiers (nécessite une configuration en +)
    - champs " relations" :
      - créer le "model" de la table "étrangère"
      - ForeignKey : clé étrangère, 1-N vers table de ref
      - ManyToManyField : table de jointure, N-N vers table de ref
      - OneToOne : 1-1
  - options
    - dépendent du type (voir doc)
    - blank=True (accepte valeur vide ou non)
    - on_delete (gestion des relation)
      - CASCADE, PROTECT, SET_NULL, DO_NOTHING...
    - max_length=255
  - méthodes
    - `__str__(self)` : représentation textuelle
  - class
    - `class Meta:` : verbose name

- si modif : MIGRATION ...

# vues

- 2 parties : python + html

  - python `views.py`
  - html : jinja + templates

- python (class)
  - standard (simplifié) : ListBVeiw, DetailView
  - sur mesure :
