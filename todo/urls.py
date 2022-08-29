from django.urls import path, include
from . import views
from rest_framework import routers
from .views import TodoViewSet

router = routers.DefaultRouter()
router.register('todos', TodoViewSet)

urlpatterns = [
    path('', include(router.urls)),
    # 第二引数これでいいの？
    path('<int:pk>/', views.TodoDetail.as_view()),
]
