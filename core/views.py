from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import (
    ListView, DetailView, CreateView, UpdateView, DeleteView, TemplateView
)
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy

from .forms import AutorForm, CategoriaForm, PostForm, BuscarPostForm
from .models import Post, Autor


def index(request):
    return render(request, 'core/index.html')

def crear_autor(request):
    if request.method == "POST":
        form = AutorForm(request.POST)
        if form.is_valid():
            autor = form.save(commit=False)
            autor.user = request.user  # ← vincula el autor al usuario logueado
            autor.save()
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
        form = PostForm(request.POST, request.FILES, user=request.user)
        if form.is_valid():
            form.save()
            return HttpResponse("✅ Post guardado correctamente.")
    else:
        form = PostForm(user=request.user)
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
    form_class = PostForm
    success_url = reverse_lazy('pages')

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user  # ← pasamos el usuario al formulario
        return kwargs

    def form_valid(self, form):
        # Asignar el autor automáticamente
        autor = Autor.objects.get(user=self.request.user)
        form.instance.autor = autor
        return super().form_valid(form)



class PostUpdateView(LoginRequiredMixin, UpdateView):
    model = Post    
    template_name = 'core/page_form.html'
    form_class = PostForm
    success_url = reverse_lazy('pages')

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs


class PostDeleteView(LoginRequiredMixin, DeleteView):
    model = Post
    template_name = 'core/post_confirm_delete.html'
    success_url = reverse_lazy('pages')


class AboutView(TemplateView):
    template_name = 'core/about.html'
