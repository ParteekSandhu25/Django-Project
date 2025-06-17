from django.views.generic import ListView, DeleteView
from .models import Post

class HomePage(ListView):
    http_method_names = ["get"]
    template_name = "feed/homepage.html"
    model = Post 
    context_object_name = "posts"
    queryset = Post.objects.all().order_by("-id")[0:10]

class PostDetailView(DeleteView):
    http_method_names = ['get']
    template_name = 'feed/detail.html'
    model = Post 
    context_object_name = "post"