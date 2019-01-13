from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'AdventureWeb/index.html')

def home(request):
    return render(request, 'AdventureWeb/home.html')

def news(request):
    return render(request, 'AdventureWeb/news.html')

def gallery(request):
    return render(request, 'AdventureWeb/gallery.html')

def links(request):
    return render(request, 'AdventureWeb/links.html')