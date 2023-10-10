from django.contrib import admin
from django.urls import path
from eoapp.views import ulogin, usignup, uhome, ulogout

urlpatterns = [
    path('admin/', admin.site.urls), 
    path("", uhome, name="uhome"),
    path("ulogin" , ulogin , name="ulogin"),
    path("usignup" , usignup , name="usignup"),
    path("ulogout" , ulogout, name="ulogout"),
 
]
