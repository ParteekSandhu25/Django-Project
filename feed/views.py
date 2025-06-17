from django.views.generic import ListView, DeleteView
from .models import Post
from django.views.generic.edit import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render

class HomePage(LoginRequiredMixin, ListView):
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

class CreateNewPost(LoginRequiredMixin, CreateView):
    model = Post
    template_name = 'feed/create.html'
    fields= ['text']
    success_url = "/"

    def dispatch(self, request, *args, **kwargs):
        self.request = request
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.author = self.request.user
        obj.save()
        return super().form_valid(form)
    
    def post(slef, request, *args, **kwargs):
        post = Post.objects.create(
            text = request.POST.get('text'),
            author = request.user
        )

        return render(
            render, 
            "includes/post.html",
            {
                "post": post, 
                "show_detail_link": True
            },
            content_type="application/html"

        )