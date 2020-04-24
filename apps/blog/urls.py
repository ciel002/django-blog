from django.urls import path

from blog import views

app_name = 'blog'
urlpatterns = [
    path('', views.index_view, name='index'),
    path('page/<int:page>/', views.index_view, name='index_page'),
    path('category/<str:category_name>/', views.index_view, name='index_category'),
    path('category/<str:category_name>/page/<int:page>/', views.index_view, name='index_category_page'),
    path('post/<str:title>/', views.post_view, name='post'),
]