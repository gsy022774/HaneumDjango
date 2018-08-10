from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [
    path('search/', views.search, name='search'),
    url(r'^articles/(?P<company_name>[ㄱ-힣a-zA-Z0-9]+)/$', views.articles, name='article'),
    path('analytics/<int:company_no>/', views.analytics, name='analytics'),
    path('prediction/<int:company_no>/', views.prediction, name='prediction'),
]
