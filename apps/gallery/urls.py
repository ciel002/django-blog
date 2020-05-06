from django.urls import path

from gallery import views

app_name = 'gallery'
urlpatterns = [
    path('', views.index_view, name='index'),
    path('list/<int:page>/', views.index_view, name='list')
]