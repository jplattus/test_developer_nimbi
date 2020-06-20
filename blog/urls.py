from rest_framework.routers import SimpleRouter

from blog.views import PostViewSet

router = SimpleRouter()
router.register('post', PostViewSet)
urlpatterns = router.urls