from django.contrib import admin
from django.urls import path
from app1.views import *
urlpatterns = [
    path('admin/', admin.site.urls),
    path('fan/', fanlar),
    path('yonalish/', yonalish),
    path('', asosiy),
    path('ustoz/', ustoz),
    path('fan_ochir/<int:son>/', fan_ochir),
    path('yonalish_ochir/<int:son>/', yonalish_ochir),
]
