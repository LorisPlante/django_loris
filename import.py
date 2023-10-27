from siteApp.models import Articles, Categories, Tags
from datetime import datetime
import json
from django.core.files import File
import requests
from io import BytesIO

# python manage.py runscript import.py

# Chargement des données
URL = "https://api.atontour.org/v1/games/"

response = requests.get(URL)
response_json = response.json()

data = response_json["records"]
print(data)

now = datetime.now()
now_fr = now.strftime("%Y-%m-%dT%H:%M:%SZ")

for item in data:
    categ, created = Categories.objects.get_or_create(title="Games")