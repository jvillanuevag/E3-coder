from django.urls import path
from . import views

from .views import (
    PostListView, PostDetailView,
    PostCreateView, PostUpdateView,
    PostDeleteView, AboutView
)

urlpatterns = [
    path('', views.index, name='inicio'),
    path('autor/', views.crear_autor, name='crear_autor'),
    path('categoria/', views.crear_categoria, name='crear_categoria'),
    path('post/', views.crear_post, name='crear_post'),
    path('buscar/', views.buscar_post, name='buscar_post'),

    # 👉 Estas son las rutas que necesitas para que {% url 'pages' %} funcione
    path('pages/', PostListView.as_view(), name='pages'),
    path('pages/create/', PostCreateView.as_view(), name='page_create'),
    path('pages/<int:pk>/', PostDetailView.as_view(), name='page_detail'),
    path('pages/<int:pk>/edit/', PostUpdateView.as_view(), name='page_edit'),
    path('pages/<int:pk>/delete/', PostDeleteView.as_view(), name='page_delete'),

    # Acerca de mí
    path('about/', AboutView.as_view(), name='about'),
]
