# Proyecto Final - Blog Universitario en Django

Este proyecto es un blog web desarrollado con Django como entrega final del curso. La aplicación permite a los usuarios registrarse, iniciar sesión, crear perfiles, publicar páginas tipo blog y comunicarse mediante mensajes privados.

## Características principales

- **Inicio** con bienvenida al sitio.
- **Vista "Acerca de mí"** (About), accesible desde la barra de navegación.
- **Listar páginas/blogs** en la ruta `/pages/` con opción de ver detalle, editar o borrar.
- **Detalle de cada página/blog** al hacer clic en "Leer más".
- **Formulario para crear, editar y eliminar publicaciones**, visible solo si estás logueado.
- **Autenticación de usuarios**: registro, login, logout.
- **Perfiles de usuario personalizados** con avatar, biografía, cumpleaños y más.
- **Mensajería entre usuarios registrados**.
- **Buscador por título de publicaciones**.
- **Categorías** para clasificar los posts (por ejemplo: Noticias, Tecnología, Ofertas, Anuncios).
- **Filtrado automático del autor**: solo se muestra el autor que está logueado.

##  Tecnologías utilizadas

- Python 3.13
- Django 5.2.3
- HTML + Bootstrap 5
- SQLite (en desarrollo)
- CKEditor para texto enriquecido

## Estructura general

- accounts/ → App para registro y login de usuarios
- core/ → App principal: modelos, vistas y templates
- templates/ → HTMLs base y de cada vista
- media/ → Imágenes subidas por los usuarios
- static/ → Estilos, imágenes fijas y scripts


##  Instalación local

1. Clona el repositorio:

```bash
git clone https://github.com/tuusuario/tu-repo-blog.git
cd tu-repo-blog

python -m venv venv
source venv/bin/activate  # o venv\Scripts\activate en Windows
pip install -r requirements.txt
