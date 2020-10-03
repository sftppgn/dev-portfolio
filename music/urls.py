from django.urls import path
from . import views 

app_name='music'

urlpatterns = [
    path('', views.home, name='home'),
    path('music/closeFile', views.closeFile, name='closeFile',namespace='music'),
]