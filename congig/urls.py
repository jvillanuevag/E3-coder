"""
URL configuration for congig project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from django.urls import path
from core import views
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls')),  
]


urlpatterns = [
    path('', views.index, name='inicio'),
    path('autor/', views.crear_autor, name='crear_autor'),
    path('categoria/', views.crear_categoria, name='crear_categoria'),
    path('post/', views.crear_post, name='crear_post'),
    path('buscar/', views.buscar_post, name='buscar_post'),
]

