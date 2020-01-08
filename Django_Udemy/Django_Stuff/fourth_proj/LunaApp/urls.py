from django.conf.urls import url
from LunaApp import views

urlpatterns = [
    url(r'BH', views.LunIndex, name='LunIndex')
]