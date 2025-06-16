from django.shortcuts import render
from django.http import HttpResponse
from .forms import AutorForm, CategoriaForm, PostForm, BuscarPostForm
from .models import Post

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
        form = PostForm(request.POST)
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

