from django.urls import include, path
from rest_framework import routers
from todo.views import ToDoViewSet

router = routers.DefaultRouter()
router.register(r'tasks', ToDoViewSet)

urlpatterns = [
    path('api/v1/today', include(router.urls)),
]
