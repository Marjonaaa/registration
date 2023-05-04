
from django.urls import path
from .views import *
urlpatterns = [
    path('', home, name='home'),
    path('open/<int:id>/', open, name="open"),
    path('delete/<id>', delete),
]