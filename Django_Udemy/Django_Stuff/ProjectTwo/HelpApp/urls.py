from django.conf.urls import url
from HelpApp import views

urlpatterns = [
    url(r'^..',views.help, name='help')
]
