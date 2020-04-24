from django.urls import path

from project import views

app_name = 'project'
urlpatterns = [
    path('', views.index_view, name='index'),
    path('yzb/', views.yzb_view, name='yzb'),
]
