from django.shortcuts import render
from .models import Blog

# Create your views here.
def index(request):
    '''get the latest 3 blogs'''
    blogs = Blog.objects.all().order_by('-id')[:3]
    context = {
        'blogs':blogs
    }
    return render(request, 'index.html',context)

def about(request):
    return render(request, 'about-us.html') 

def contact(request):
    return render(request, 'contact.html')

def services(request):
    return render(request, 'service.html')

def blog(request):
    blogs = Blog.objects.all()
    context = {
        'blogs':blogs
    }
    return render(request, 'blog.html',context)

def blogpost(request, blog_id):
    blog = Blog.objects.get(id=blog_id)
    all_blogs = Blog.objects.all()
    context = {
        'blog':blog,
        'all_blogs':all_blogs
    }
    return render(request, 'single-blog.html',context)

