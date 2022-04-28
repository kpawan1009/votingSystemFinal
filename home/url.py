
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('about/',views.about,name='about'),
    path('candidateaura/',views.candidateaura,name='candidateaura'),
    path('candidatepalg/',views.candidatepalg,name='candidatepalg'),
    path('palghar/',views.palghar,name='palghar'),
    path('amroha/',views.amroha,name='amroha'),
]
