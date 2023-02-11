from django.urls import path
from . import views

urlpatterns = [
    path("",views.index),
    path("register/",views.register),
    path("userlogin/",views.userlogin),
    path("loginemp/",views.loginemp),
    path("email/",views.email),
    path('addmail/',views.addmail),
    path("adminlogin/",views.adminlogin),
    path('dashboard/',views.dashbaord),
    path('action/<int:eid>/',views.action),
    path('actiontaken/',views.actiontaken),
     path('table/',views.table),
    
]
