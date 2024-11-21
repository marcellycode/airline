from django.contrib import admin
from django.urls import path, include 
from flights import views  

urlpatterns = [
    path('admin/', admin.site.urls),
    path('flights/', include("flights.urls")),
    path('users/', include("users.urls"))

]

