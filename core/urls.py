from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='inicio'),
    path('autor/', views.crear_autor, name='crear_autor'),
    path('categoria/', views.crear_categoria, name='crear_categoria'),
    path('post/', views.crear_post, name='crear_post'),
    path('buscar/', views.buscar_post, name='buscar_post'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
