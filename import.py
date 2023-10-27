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

now = datetime.now()
now_fr = now.strftime("%Y-%m-%dT%H:%M:%SZ")

for item in data:
    categ, created = Categories.objects.get_or_create(title="Games")
    article = Articles(
        user_id=1,
        status="PB",
        title=item['title'],
        content=item['pitch'],
        published_at=now_fr,
        category=categ
    )

    img_url = item['screenshot']
    if img_url:
        response = requests.get(img_url)
        if response.status_code == 200:
            image_name = img_url.split("/")[-1]
            image_content = BytesIO(response.content)
            article.cover.save(image_name, File(image_content), save=True)

    img_url = item['icon']
    if img_url:
        response = requests.get(img_url)
        if response.status_code == 200:
            image_name = img_url.split("/")[-1]
            image_content = BytesIO(response.content)
            article.thumb.save(image_name, File(image_content), save=True)
    
    article.save()

    tag, created = Tags.objects.get_or_create(word=item['year'])
    article.tags.add(tag)
    tag, created = Tags.objects.get_or_create(word=item['producer'])
    article.tags.add(tag)