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
        rep = render(requests, "mytemplates/box_index.html")
        rep.set_cookie("user_id", 10000)

        return render(requests, "mytemplates/box_index.html", content)


def box_content(requests):
    import datetime, time
    if requests.method == 'POST':
        user_id = requests.COOKIES.get("user_id")
        content_title = requests.POST.get("content_title")
        article_introduce = requests.POST.get("article_introduce")
        # 插入content
        g = requests.POST.get("content")
        content_id = time.time()
        content_date = str(datetime.datetime.now())[:19]
        content = g
        db.insert(user_id=user_id, content=content, content_data=content_date, content_id=content_id)
        data = {"content": g}
        # 插入导航表
        db.insert(user_id=user_id, article_title=content_title, article_introduce=article_introduce, date=content_date)

        return render(requests, "page/show_mode.html", data)
