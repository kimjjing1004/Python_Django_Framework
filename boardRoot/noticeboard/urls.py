from django.urls import path
from . import views

app_name = 'noticeboard'
urlpatterns = [
    path('', views.index, name='index'),
    path('write', views.write_article, name='write_article'),
    path('add', views.add_article, name='add_article'),
]