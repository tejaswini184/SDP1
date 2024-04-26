from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
   # path('admin/', admin.site.urls),
    path('', homepage, name='homepage'),
    path('userhomepage/', userhomepage, name='userhomepage'),
    path('contactus/', contactus, name='contactus'),
    path('changes/', changes, name='changes'),

    ]