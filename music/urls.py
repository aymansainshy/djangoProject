from django.urls import  path 
from . import  views

app_name = 'music'


urlpatterns = [
    path('', views.index , name='index'),
    path('<str:id>/', views.detail , name='detail'),

    #/music/<album_id>/favorite/
    path('<str:id>/favorite/', views.favorite , name='favorite'),
]