from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('festivals/',festivals,name='festivals'),
    path('historical/',historical,name='historical'),
    path('cultures/',cultures,name='cultures'),
    path('artforms/',artforms,name='artforms'),
    path('login/', login, name='login'),
    path('login1/', login1, name='login1'),
    path('signup/', signup, name='signup'),
    path('signup1/', signup1, name='signup1'),
    path('logout/', logout, name='logout'),
    path('feedback/',feedback,name='feedback'),
    path('contactmail/',contactmail,name='contactmail'),

    ]