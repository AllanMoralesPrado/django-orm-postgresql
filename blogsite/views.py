from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.template import loader
from .models import Post
# Para vistas basadas en clase
from django.views import View

def index(request):
    posts = Post.objects.all().values()
    template = loader.get_template('index.html')
    context = {
        'posts': posts,
    }
    return HttpResponse(template.render(context, request))

class Index(View):
    def get(self, request):
        posts = Post.objects.all().values()
        template = loader.get_template('index.html')
        context = {
            'posts': posts,
        }
        return HttpResponse(template.render(context, request))
    
# class Index(View):
#     template_name = 'index.html'

#     def get(self, request):
#         posts = Post.objects.all().values()
#         context = {
#             'posts': posts,
#         }
#         return render(request, self.template_name, context)
    
def agregar(request):
    template = loader.get_template('agregar.html')
    return HttpResponse(template.render({}, request))

def agregarregistro(request):
    titulo = request.POST['title']
    contenido = request.POST['content']
    autor = request.POST['author']
    post = Post(title=titulo, content=contenido, author=autor)
    post.save()
    return HttpResponseRedirect(reverse('index'))

def eliminar(request, id):
    post = Post.objects.get(id=id)
    post.delete()
    return HttpResponseRedirect(reverse('index'))

def actualizar(request, id):
    post = Post.objects.get(id=id)
    template = loader.get_template('actualizar.html')
    context = {
        'post': post,
    } 
    return HttpResponse(template.render(context, request))

def actualizarregistro(request, id):
    titulo = request.POST['title']
    contenido = request.POST['content']
    autor = request.POST['author']
    post = Post.objects.get(id=id)
    post.title = titulo
    post.content = contenido
    post.author = autor
    print(post.title, post.content, post.author)
    post.save()
    post2 = Post.objects.get(id=id)
    print(post2.title, post2.content, post2.author)
    return HttpResponseRedirect(reverse('index'))

def mandar_por_mandar(request):
    post = Post.objects.get(id=1)
    post.title = "A"
    post.content = "B"
    post.author = "C"
    post.save()
    return HttpResponseRedirect(reverse('index'))