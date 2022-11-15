from django.urls import path, include
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r"todos", views.TodoViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('todos/', include('rest_framework.urls'), name='rest_framework')
]
