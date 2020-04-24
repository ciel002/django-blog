from django.urls import path

from home import views

app_name = 'home'
urlpatterns = [
    path('', views.index_view, name='index'),
    path('contact/', views.contact_view, name='contact'),
    path('contact/send_contact_email/', views.contact_send_mail_view, name='send_contact_email'),
    path('map/', views.map_view, name='map'),
]