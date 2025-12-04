from django.shortcuts import render
from .models import Blog

def index(request):
    context = {
        "title": "Django Template Tags",
        
        "students": [
            # {'name': 'John', 'age': 21, 'grade': 'B'},
            # {'name': 'Jane', 'age': 20, 'grade': 'A'}
        ]
    }
    
    return render(request, 'index.html', context)

def about(request):
    
    return render(request, 'about.html')

def contact(request):
    
    return render(request, 'contact.html')

def blog_list(request):
    blogs = Blog.objects.all()
    context = {'blogs': blogs}
    
    return render (request, 'blog_list.html', context)