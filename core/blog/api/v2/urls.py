from django.urls import path, include

from .views import *

app_name = "api-v2"

urlpatterns = [
    path("", PostList.as_view(), name="post-list"),
    # path("<int:id>/", PostDetail.as_view(), name="post-detail"),
    path("<int:pk>/", PostDetail.as_view(), name="post-detail"),
]
