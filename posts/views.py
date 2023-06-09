from django.shortcuts import render
from .models import Post
# Create your views here.
def index(request):
    posts = Post.objects.all()
    return render(request, 'index.html', {'posts': posts})

def post(request, pk):
    post = Post.objects.get(id=pk)
    posts = Post.objects.all()[:3]
    return render(request, 'post.html', {'post': post, 'posts': posts})

def author(request):
    return render(request, 'author.html')