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
```
