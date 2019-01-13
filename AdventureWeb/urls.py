from django.urls import path, include
from django.views.generic import ListView, DetailView
from . import views
from AdventureWeb.models import Post, Gallery
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
	path('', views.home),
	path('home', views.home),
	path('links', views.links),
	path('news', ListView.as_view( queryset=Post.objects.all().order_by("-date")[:5], template_name="AdventureWeb/news.html")),
	path('gallery', ListView.as_view( queryset=Gallery.objects.all(), template_name="AdventureWeb/gallery.html")),
	]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)