from django.urls import path, include

from .views import *

app_name = "api-v1"

urlpatterns = [
    path("", post_list, name="post-list"),
    path("<int:id>/", post_detail, name="post-detail"),
]
