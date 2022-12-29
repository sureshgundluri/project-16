from django.urls import path
from app1.views import *
app_name='something3'

urlpatterns=[
    path('sunday/',sunday,name='sunday'),
    path('rokesh/',rokesh,name='rokesh'),
]