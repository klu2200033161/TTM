from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('Hello/', hello1),
    path('hello/', hello, name='hello'),
    path('', newhomepage, name='newhomepage'),
    path('package/', travelpackage, name='package'),
    path('p/', print1, name='p'),
    path('print/', Print_to_console, name='print'),
    path('ran1/', random123, name='random123'),
    path('rand/', rand, name='rand'),
    path('date/', getdate1, name='date'),
    path('date1/', get_date, name='date1'),
    # path('tz/',tzfunctioncall,name='tz'),
    # path('tz1/',tzfunctioncall,name='tz1')
    path('reg/', register1, name='register1'),
    path('reg1/', registerloginfunction, name='registerloginfunction'),
    path('pie1/',pie_chart1,name='pie_chart1'),
    path('pie/',pie_chart,name='pie_chart'),
    path('slide/',slides,name='slides'),
    path('weathercall/',weather,name='weather'),
    path('weatherlogic',weatherlogic,name='weatherlogic'),
    path('log/',login,name='login'),
    path('log1/',login1,name='login1'),
    path('sign/',signup,name='signup'),
    path('sign1/',signup1,name='signup1'),
    path('logout/',logout,name='logout'),
    path('contact1/',contactmail1,name='contactmail1'),
    path('contact/',contactmail,name='contactmail'),
]
