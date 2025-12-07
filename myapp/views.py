from django.shortcuts import render, redirect
from .models import Blog, Book, Subscriber
from django.contrib import messages
from .forms import BlogForm
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
    print(blogs.query)
    context = {'blogs': blogs}
    
    return render (request, 'blog_list.html', context)

def subscribe(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        if Subscriber.objects.filter(email=email).exists():
            messages.error(request, 'You are already subscribed.')
            
        else:
            subscriber = Subscriber(email=email)
            subscriber.save()
            
            messages.success(request, 'Thank you for subscribing!')
            
            return redirect('subscribe')
    
    return render(request, 'subscribe.html')

def add_blog(request):
    if request.method == 'POST':
        form = BlogForm(request.POST)
        if form.is_valid():
            blog = form.save()
            return redirect('blogs')
    else:
        form = BlogForm()
    return render(request, 'add_blog.html', {'form': form})