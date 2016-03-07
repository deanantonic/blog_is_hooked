from django.shortcuts import render

# Create your views here.
# Create your views here.

from blog.models import Blog, Category
from django.shortcuts import render_to_response, get_object_or_404


def index(request):
    return render(request, 'index.html')

def single_project(request):
    return render(request, 'single-project.html')

def index1(request):
    return render_to_response('index1.html', {
        'categories': Category.objects.all(),
        'posts': Blog.objects.all()[:5]
    })

def view_post(request, slug):   
    return render_to_response('view_post.html', {
        'post': get_object_or_404(Blog, slug=slug)
    })

def view_category(request, slug):
    category = get_object_or_404(Category, slug=slug)
    return render_to_response('view_category.html', {
        'category': category,
        'posts': Blog.objects.filter(category=category)[:5]
    })