import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                      'img_dump.settings')

import django
django.setup()
from app_img.models import Images
from django.utils import timezone


img_pages = [
            {'title': 'Bike Fall',
             'url':'https://imgflip.com/s/meme/Bike-Fall.jpg',
            },
            {'title': 'Paid',
             'url':'https://i.imgflip.com/2xscjb.png',
            },
            {'title': 'Spongebob',
             'url':'https://imgflip.com/s/meme/Imagination-Spongebob.jpg',
            }
            ]


def populate(img_pages):

    for dic in img_pages:
        p = Images.objects.create()
        p.title = dic['title']
        p.url = dic['url']
        p.created = timezone.now()
        p.save()
        print(f"Populando: - {dic['title']} - {dic['url']} -")



if __name__ == '__main__':
    print('Empezando la population...')
    populate(img_pages)
