from django.shortcuts import render
from django.views.generic.base import TemplateView, RedirectView
from .models import Post
from django.shortcuts import get_object_or_404
from django.views.generic import (
    ListView,
    DetailView,
    UpdateView,
    DeleteView,
    FormView,
    CreateView,
)
from .forms import PostForm
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response

# Create your views here.

# class IndexView(TemplateView):
#     template_name = "index.html"
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context["name"] = "ali"
#         context["posts"] = Post.objects.all()
#         return context
#


class PostListView(ListView):
    # queryset = Post.objects.all()
    model = Post
    context_object_name = "posts"
    paginate_by = 3
    ordering = "id"
    # def get_queryset(self):
    #     posts = Post.objects.filter(status=True)
    #     return posts


class PostDetailView(DetailView):
    model = Post
    context_object_name = "post"


class PostCreateView(CreateView):
    form_class = PostForm
    success_url = "/blog/post/"
    template_name = "blog/post_create.html"

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class PostCreateView(PermissionRequiredMixin, LoginRequiredMixin, CreateView):
    model = Post
    form_class = PostForm
    success_url = "/blog/post/"
    permission_required = "blog.view_post"

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostEditView(PermissionRequiredMixin, LoginRequiredMixin, UpdateView):
    model = Post
    context_object_name = "post"
    form_class = PostForm
    success_url = "/blog/post/"
    permission_required = "blog.view_post"


class PostDeleteView(PermissionRequiredMixin, LoginRequiredMixin, DeleteView):
    model = Post
    context_object_name = "post"
    success_url = "/blog/post/"
    permission_required = "blog.view_post"


@api_view()
def api_post_list_view(request):
    return Response({"name": "Alireza"})
