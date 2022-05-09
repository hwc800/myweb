from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include

from box import views


urlpatterns = [
    url(r'^root_login', views.root_login, name='root_login'),
    url(r'^box_content', views.box_content, name='box_content'),
    url(r'^box_mode', views.box_mode, name='box_mode'),
    url(r'^box_index', views.box_index, name='box_index'),
]