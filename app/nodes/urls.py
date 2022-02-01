from rest_framework.routers import DefaultRouter
from .views import NodeViewset

router = DefaultRouter()
router.register("", NodeViewset, basename="node")

urlpatterns = router.urls
