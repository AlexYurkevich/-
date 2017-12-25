from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View
import logging


# Create your views here.


class Test(View):
    def get(self, request):
        data = {
            'horses': [
                {'nickname': 'Сахарок', 'age': 10, 'number': 3, 'id': 1},
                {'nickname': 'Lucky guy', 'age': 12, 'number': 7, 'id': 2},
                {'nickname': 'Firefly', 'age': 15, 'number': 5, 'id': 3},
                {'nickname': 'Беркут', 'age': 13, 'number': 8, 'id': 4},
                {'nickname': 'Галоп', 'age': 11, 'number': 11, 'id': 5},
                {'nickname': 'Invincible', 'age': 14, 'number': 1, 'id': 6},
                {'nickname': 'Пегас', 'age': 12, 'number': 2, 'id': 7}
            ]
        }
        logging.info(123)
        return render(request, 'horses.html', data)


class Horse(View):
    def get(self, request, id):
        data = {
            'horse': {
                'id': id
            }
        }
        logging.info(data)
        return render(request, 'horse_info.html', data)