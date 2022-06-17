from rest_framework import routers

from picman_studio_backend.apps.project.api.v1.api_view import ProjectViewSet

project_router = routers.DefaultRouter()
project_router.register(r'projects', ProjectViewSet)
