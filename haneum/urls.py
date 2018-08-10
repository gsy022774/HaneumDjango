from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [
    path('', views.search, name='search'),
    url(r'^articles/$', views.articles, name='articles'),
    path('analytics/', views.analytics, name='analytics'),
    path('prediction/', views.prediction, name='prediction'),
]
