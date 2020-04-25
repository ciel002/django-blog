from django.urls import path

from project import views

app_name = 'project'
urlpatterns = [
    path('', views.index_view, name='index'),
    path('yzb/', views.yzb_view, name='yzb'),
    path('yzb/zxxx', views.yzb_zxxx_view, name='yzb_zxxx'),
    # path('yzb/unzxxx', views.yzb_unzxxx_view, name='yzb_unzxxx'),
    # path('yzb/page/<page>', views.yzb_view, name='yzb'),
]
