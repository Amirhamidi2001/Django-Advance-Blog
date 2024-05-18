from rest_framework.routers import DefaultRouter

from .views import *

app_name = "api-v3"

router = DefaultRouter()
router.register("post", PostViewSet, basename="post")
router.register("category", CategoryViewSet, basename="category")
urlpatterns = router.urls
