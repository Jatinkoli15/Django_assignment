from django.urls import path,re_path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('users/', views.all_users, name='all_users'),
    #path('users/<int:user_id>/', views.user_detail, name='user_detail'), using path converter
    re_path(r'^users/user-id-(?P<user_id>\d+)/$', views.user_detail,name='user_detail'), #using regex
]
