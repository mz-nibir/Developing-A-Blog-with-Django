from django.shortcuts import render, HttpResponseRedirect
from django.views.generic import CreateView, UpdateView, ListView, View, TemplateView, DeleteView
from App_Blog.models import Blog, Comment, Like
from django.urls import reverse, reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.

def blog_list(request):
    return render(request, 'App_Blog/blog_list.html', context={})

class CreateBlog(LoginRequiredMixin, CreateView):
    model = Blog
    template_name = 'App_Blog/create_blog.html'
    fields = '__all__'
