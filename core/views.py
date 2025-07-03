from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import (
    ListView, DetailView, CreateView, UpdateView, DeleteView, TemplateView
)
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy

from .forms import AutorForm, CategoriaForm, PostForm, BuscarPostForm
from .models import Post

# -------------------------------
# Vistas funcionales
# -------------------------------

def index(request):
    return render(request, 'core/index.html')

def crear_autor(request):
    if request.method == "POST":
        form = AutorForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("✅ Autor guardado correctamente.")
    else:
        form = AutorForm()
    return render(request, "core/formulario.html", {"form": form, "titulo": "Nuevo Autor"})

def crear_categoria(request):
    if request.method == "POST":
        form = CategoriaForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("✅ Categoría guardada correctamente.")
    else:
        form = CategoriaForm()
    return render(request, "core/formulario.html", {"form": form, "titulo": "Nueva Categoría"})

def crear_post(request):
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponse("✅ Post guardado correctamente.")
    else:
        form = PostForm()
    return render(request, "core/formulario.html", {"form": form, "titulo": "Nuevo Post"})

def buscar_post(request):
    resultados = []
    if request.method == "POST":
        form = BuscarPostForm(request.POST)
        if form.is_valid():
            titulo = form.cleaned_data['titulo']
            resultados = Post.objects.filter(titulo__icontains=titulo)
    else:
        form = BuscarPostForm()
    return render(request, "core/buscar.html", {"form": form, "resultados": resultados})

# -------------------------------
# Vistas basadas en clase (CBV) para Post
# -------------------------------

class PostListView(ListView):
    model = Post
    template_name = 'core/pages_list.html'
    context_object_name = 'posts'

class PostDetailView(DetailView):
    model = Post
    template_name = 'core/page_detail.html'
    context_object_name = 'post'

class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    template_name = 'core/post_form.html'
    fields = ['titulo', 'subtitulo', 'contenido', 'imagen', 'autor', 'categoria']
    success_url = reverse_lazy('pages')

class PostUpdateView(LoginRequiredMixin, UpdateView):
    model = Post
    template_name = 'core/page_form.html'
    fields = ['titulo', 'subtitulo', 'contenido', 'imagen', 'autor', 'categoria']
    success_url = reverse_lazy('pages')

class PostDeleteView(LoginRequiredMixin, DeleteView):
    model = Post
    template_name = 'core/page_confirm_delete.html'
    success_url = reverse_lazy('pages')

# -------------------------------
# Vista About
# -------------------------------

class AboutView(TemplateView):
    template_name = 'core/about.html'
