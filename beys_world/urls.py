from django.urls import path

from beys_world import views

app_name = 'beys_world'

urlpatterns = [
    path('', views.index, name='index'),
    path('all_parts/', views.all_parts, name='all_parts'),
    path('register_blade/', views.register_blade, name='register_blade'),

]