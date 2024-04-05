from django.urls import path
from . import views

urlpatterns = [
    path("",views.kiran,name='kiran'),
    path("jailava",views.jailava,name='jailava'),
    path("aravinda",views.aravinda,name='aravinda'),
    path("truelover",views.truelover,name='truelover'),
    path("godzilla",views.godzilla,name='godzilla'),
    path("hanuman",views.hanuman,name='hanuman'),
    path("sundaram",views.sundaram,name='sundaram'),
    path("mastushases",views.mastushases,name='mastushades'),
    path("joe",views.joe,name='joe'),
    path("animal",views.animal,name='animal'),
    path("tillu",views.tillu,name='tillu'),
    path("romantic",views.romantic,name='romantic'),
    path("babblegum",views.babblegum,name='babblegum'),
]
