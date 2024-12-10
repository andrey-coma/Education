from pprint import pprint
from pymongo import MongoClient
import csv

client = MongoClient({'localhost': 27017})
db = client['images_base']
images_info = db.unsplashcom
data = []

for image in images_info.find():
    data.append(image)

# pprint(data, sort_dicts=False)

with open('images_info.csv', 'w') as f:
    writer = csv.writer(f)
    writer.writerow(('title', 'category', 'url', 'image'))
    for i in data:
        writer.writerow((i['title'], i['category'], i['url'], i['image']))