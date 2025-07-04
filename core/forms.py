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
        fields = ['titulo', 'subtitulo', 'contenido', 'imagen', 'autor', 'categoria']

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)
    
        if user and Autor.objects.filter(user=user).exists():
            self.fields['autor'].queryset = Autor.objects.filter(user=user)
        else:
            self.fields['autor'].queryset = Autor.objects.none()

class BuscarPostForm(forms.Form):
    titulo = forms.CharField(label='Buscar por título', max_length=100)
