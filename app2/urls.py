from django.urls import path
from app2.views import *
app_name='something4'

urlpatterns=[
    path('html1/',html1,name='html1'),
    path('html2/',html2,name='html2'),
]