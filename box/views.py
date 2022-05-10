from django.shortcuts import render
import db
import wwd.config_db as config_db


# Create your views here.
def root_login(requests):
    if requests.method == 'GET':
        return render(requests, "page/login/login.html")


def box_mode(requests):
    if requests.method == 'GET':
        rep = render(requests, "page/mode.html")
        rep.set_cookie("user_id", 10000)
        return rep


def box_index(requests):
    if requests.method == 'GET':
        result = db.article_title()
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
        content_id = str(time.time())
        content_date = str(datetime.datetime.now())[:19]
        content = g
        db.insert(config_db.markdown_content, user_id=user_id, content=content, content_date=content_date, article_id=content_id)
        data = {"content": g}
        # 插入导航表
        db.insert(config_db.user_data, article_id=content_id, user_id=user_id, article_title=content_title, article_introduce=article_introduce, date=content_date)

        return render(requests, "page/show_mode.html", data)


# def box_show_mode(requests):
#     if requests.method == "GET":
#         requests.
#         return render(requests, "page/show_mode.html", data)