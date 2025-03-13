from django.urls import path

from beys_world import views

app_name = 'beys world'

urlpatterns = [
    path('', views.index, name='index'),
]