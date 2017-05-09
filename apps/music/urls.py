from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$',views.index),
    url(r'^shop$',views.shop),
    url(r'^home$',views.home),
    url(r'^bio$',views.bio),
    url(r'^shows$',views.shows),
]
