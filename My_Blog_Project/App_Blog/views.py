from django.shortcuts import render, HttpResponseRedirect
from django.views.generic import CreateView, UpdateView, ListView, View, TemplateView, DeleteView
from App_Blog.models import Blog, Comment, Like
from django.urls import reverse, reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from App_Blog.forms import CommentForm
# unique id generate kore
import uuid

# Create your views here.


class BlogList(ListView):
    context_object_name = 'blogs'
    model = Blog
    template_name = 'App_Blog/blog_list.html'


class CreateBlog(LoginRequiredMixin, CreateView):
    model = Blog
    template_name = 'App_Blog/create_blog.html'
    # je je fields rakhte cai
    fields = ('blog_title', 'blog_content', 'blog_image')

    def form_valid(self, form):
        blog_obj = form.save(commit=False)
        blog_obj.author = self.request.user
        title = blog_obj.blog_title
        # space replace by hipane...tar sathe extra enique id jora dibe
        blog_obj.slug = title.replace(" ", "-") + "-" + str(uuid.uuid4())
        blog_obj.save()
        return HttpResponseRedirect(reverse('index'))

@login_required
def blog_details(request, slug):
    blog = Blog.objects.get(slug=slug)
    # generating the comment form
    comment_form = CommentForm()
    # Jodi form ti sumit kora hoy
    if request.method == 'POST':
        # form er vetor sumit kora info ashbe
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            # commont form er  user hobe ..akhon login kora user
            comment.user = request.user
            # kon blog er sathe connect hobe (ei blog page ai)
            comment.blog = blog
            comment.save()
            # je blog page a asi sei page ei niye ashte hobe....jehetu eti argument accecpt kore tai arg pass korte hobe slug er moddhe
            return HttpResponseRedirect(reverse('App_Blog:blog_details', kwargs={'slug':slug}))



    return render(request, 'App_Blog/blog_details.html', context={'blog':blog, 'comment_form':comment_form})
