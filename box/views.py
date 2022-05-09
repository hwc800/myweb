from django.shortcuts import render
import db


# Create your views here.
def root_login(requests):
    if requests.method == 'GET':
        return render(requests, "page/login/login.html")


def box_mode(requests):
    if requests.method == 'GET':

        return render(requests, "page/mode.html")


def box_index(requests):
    if requests.method == 'GET':
        result = db.article_title(10000)
        page = 0
        data = {}
        for app in result:
            data[page] = app
            page += 1
        content = {
            "data": data
        }
        return render(requests, "mytemplates/box_index.html", content)


def box_content(requests):
    import datetime
    if requests.method == 'POST':

        g = requests.POST.get("content")
        user_id = 10000
        content_date = str(datetime.datetime.now())[:19]
        content = g
        db.insert(user_id=user_id, content=content, content_data=content_date)
        data = {"content": g}
        print(111)
        return render(requests, "page/show_mode.html", data)
