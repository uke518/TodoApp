from django.urls import path, include
# from . import views
from rest_framework import routers
from .views import TodoViewSet

router = routers.DefaultRouter()
router.register('todos', TodoViewSet)


urlpatterns = [
    # この2行いるの？
    path('', include(router.urls)),
]
