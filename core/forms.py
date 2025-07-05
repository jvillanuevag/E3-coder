from django import forms
from .models import Autor, Categoria, Post

class AutorForm(forms.ModelForm):
    class Meta:
        model = Autor
        fields = ['nombre', 'email']

class CategoriaForm(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = ['nombre']

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['titulo', 'subtitulo', 'contenido', 'imagen', 'categoria']

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)

    def save(self, commit=True):
        post = super().save(commit=False)
        if self.user:
            try:
                post.autor = Autor.objects.get(user=self.user)
            except Autor.DoesNotExist:
                post.autor = None
        if commit:
            post.save()
        return post

class BuscarPostForm(forms.Form):
    titulo = forms.CharField(label='Buscar por título', max_length=100)
