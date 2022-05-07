from django.shortcuts import render
from django.http import JsonResponse, HttpResponse

# Create your views here.
from app01 import db


def index_select_data(requests):
    if requests.method == 'GET':
        result = db.article_title(10000)
        page = 0
        data = {}
        for app in result:
            data[page] = app
            page += 1
        content ={
            "data": data
        }

        return render(requests, "page/thirst.html", content)

