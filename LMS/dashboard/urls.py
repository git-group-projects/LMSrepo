from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('comment/', views.comment, name='comment'),
    path('<str:slug>', views.post, name='post'),
]