from .views import CategoryViewSets
from rest_framework.routers import DefaultRouter
from django.urls import path, include

router = DefaultRouter()
router.register(r'', CategoryViewSets)

urlpatterns = [
    path('', include(router.urls))
]