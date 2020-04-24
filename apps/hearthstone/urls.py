from django.urls import path

from hearthstone import views

urlpatterns = [
    path('', views.index)
]
