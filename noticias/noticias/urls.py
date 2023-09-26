"""noticias URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from sitio import views

urlpatterns = [
    path('inicio/', views.inicio),
    path('api/noticias/', views.api_noticias_como_html),
    path('api/noticias/<int:noticia_pk>/', views.api_noticias_como_json),
    path('prueba_form_pelado/', views.prueba_form_pelado),
    path('prueba_form_django/', views.prueba_form_django),
    path('prueba_form_django_reloaded/', views.prueba_form_django_reloaded),
    path('rebuild_and_update_index/', views.rebuild_and_update_index),
    path('search/', include('haystack.urls')),
    path('admin/', admin.site.urls),
]
