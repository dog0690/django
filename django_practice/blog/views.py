from django.shortcuts import render
from .models import Post
# Create your views here.
posts = [
    {
        'author': 'coryMS',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'November 19, 2024',
    },
    {
        'author': 'charley',
        'title': 'Blog Post 2',
        'content': 'second post',
        'date_posted': 'November 20, 2024',
    }
]
def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html', {'title': 'about'})