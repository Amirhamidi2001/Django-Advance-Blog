from django.shortcuts import render
from django.views.generic.base import TemplateView, RedirectView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import(
    FormView, CreateView, UpdateView, DeleteView
)

from .models import Post
from .forms import CommentForm, PostForm


class TemplateView(TemplateView):
    template_name = "index.html"


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["post"] = Post.objects.all()[:5]
        return context


class RedirectView(RedirectView):
    url = "https://amirhamidi.pythonanywhere.com/"


class PostListView(ListView):
    model = Post
    paginate_by = 3


class PostDetailView(DetailView):
    model = Post

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


# class ContactFormView(FormView):
#     template_name = "post_detail.html"
#     form_class = CommentForm
#     success_url = "/post/"

#     def form_valid(self, form):
#         # This method is called when valid form data has been POSTed.
#         # It should return an HttpResponse.
#         form.send_email()
#         return super().form_valid(form)


class PostCreateView(CreateView):
    model = Post
    form_class = PostForm
    success_url = "/post/"


class PostUpdateView(UpdateView):
    model = Post
    form_class = PostForm
    success_url = "/post/"
    template_name_suffix = "_update_form"



class PostDeleteView(DeleteView):
    model = Post
    success_url = "/post/"
