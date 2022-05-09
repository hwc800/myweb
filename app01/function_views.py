from django.shortcuts import render

# Create your views here.
import db


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

