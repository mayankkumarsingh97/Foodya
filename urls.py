from django.urls import path
from django.conf.urls import url
from django.views.generic import TemplateView

from . import views

app_name = 'home'

urlpatterns = [
    path('', views.index, name='index'),
    path('thankyou', views.thankyou, name='thankyou'),
    path('contact1', views.contact1, name='contact1'),
    path('contact2', views.contact2, name='contact2'),

]
