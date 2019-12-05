from django.urls import path
from .views import home
from .views import categoria

urlpatterns = [
    path('', home, name='home'),
    path('<slug:slug>', categoria, name='categoria'),
]
