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
    posts = Post.objects.all()
    return render(request, 'author.html', {'posts': posts})

def search(request):
    if request.method == "GET":
        query = request.GET.get('query')

        if query == '':
            query = 'None'

        results = Post.objects.filter(title__icontains=query)
        count = results.count()

    return render(request, 'search.html', {'query': query, 'results': results, "count": count})
