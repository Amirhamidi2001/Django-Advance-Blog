from django.views.generic.base import TemplateView, RedirectView
from django.urls import path, include

from .views import *

app_name = "blog"

urlpatterns = [
    # path("", TemplateView.as_view(template_name="index.html"), name="index"),
    # path(
    #     "go-to-amirhamidi/",
    #     RedirectView.as_view(url="https://amirhamidi.pythonanywhere.com/"),
    #     name="go-to-amirhamidi",
    # ),
    path("", TemplateView.as_view(), name="index"),
    path("amirhamidi/", RedirectView.as_view(), name="amirhamidi"),
    path("post/", PostListView.as_view(), name="post-list"),
    path("post/<int:pk>/", PostDetailView.as_view(), name="post-detail"),
    path("post/create/", PostCreateView.as_view(), name="post-create"),
    path("post/<int:pk>/edit/", PostUpdateView.as_view(), name="post-edit"),
    path("post/<int:pk>/delete/", PostDeleteView.as_view(), name="post-delete"),
    path("api/v1/", include("blog.api.v1.urls")),
    path("api/v2/", include("blog.api.v2.urls")),
]
