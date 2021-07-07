"""practice_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from collections import namedtuple
from django.conf.urls import handler400, static
from django.contrib import admin
from django.urls import path, include
from django.urls import re_path
from firstapp import views
from practice_project import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from rest_framework.urlpatterns import format_suffix_patterns
from firstapp import views

urlpatterns = [
    path('', views.index, name='home'),
    path('reg_user/', views.reg_user, name='reg_user'),
    path('auth_user/', views.auth_user, name='auth_user'),
    path('change_create/', views.change_create, name='change_create'),
    path('add_proc/', views.add_proc, name='add_proc'),
    path('add_video/', views.add_video, name='add_video'),
    path('add_mother/', views.add_mother, name='add_mother'),
    path('add_client/', views.add_client, name='add_client'),
    path('add_order/', views.add_order, name='add_order'),
    path('chage_rud/', views.change_rud, name='change_rud'),
    path('view_proc/', views.view_proc, name='view_proc'),
    path('view_video/', views.view_video, name='view_video'),
    path('view_mother/', views.view_mother, name='view_mother'),
    path('view_client/', views.view_client, name='view_client'),
    path('view_order/', views.view_order, name='view_order'),
    path('view_proc/update_proc/<int:id>/', views.update_proc, name='update_proc'),
    path('view_video/update_video/<int:id>/', views.update_video, name='video_update'),
    path('view_mother/update_mother/<int:id>/', views.update_mother, name='update_mother'),
    path('view_client/update_client/<int:id>/', views.update_client, name='update_client'),
    path('view_order/update_order/<int:id>/', views.update_order, name='update_order'),
    path('view_proc/delete_proc/<int:id>/', views.delete_proc, name='delete_proc'),
    path('view_video/delete_video/<int:id>/', views.delete_video, name='delete_video'),
    path('view_mother/delete_mother/<int:id>/', views.delete_mother, name='delete_mother'),
    path('view_client/delete_client/<int:id>/', views.delete_client, name='delete_client'),
    path('view_order/delete_order/<int:id>/', views.delete_order, name='delete_order'),
    path('view_order_extra/', views.view_order_extra, name='view_order_extra'),
    path('api_auth/', include('rest_framework.urls')),
    path('user/', views.UserList.as_view()),
    path('user/<int:pk>/', views.UserDetail.as_view()),
    path('client', views.ClientList.as_view()),
    path('client/<int:pk>/', views.ClientDetail.as_view()),
    path('order/', views.OrderList.as_view()),
    path('order/<int:pk>/', views.OrderDetail.as_view()),
    path('proc/', views.ProcessorList.as_view()),
    path('proc/<int:pk>/', views.ProcessorDetail.as_view()),
    path('video/', views.VideocardList.as_view()),
    path('video/<int:pk>/', views.VideocardDetail.as_view()),
    path('mother/', views.MotherboardList.as_view()),
    path('mother/<int:pk>/', views.MotherboardDetail.as_view()),
    path('admin/', admin.site.urls),
]

urlpatterns = format_suffix_patterns(urlpatterns)

handler404 = views.pageNotFound