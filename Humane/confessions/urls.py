from django.urls import path,include
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from . import views

urlpatterns = [
    path('', views.confessions, name = "confessions"),
] 

urlpatterns += staticfiles_urlpatterns()