from rest_framework import routers

from picman_studio_backend.apps.project.api.v1.api_view import (
    ProjectViewSet,
    ClientViewSet,
    EventViewSet,
    AlbumViewSet
)

project_router = routers.DefaultRouter()
project_router.register(r'projects', ProjectViewSet)
project_router.register(r'clients', ClientViewSet)
project_router.register(r'events', EventViewSet)
project_router.register(r'albums', AlbumViewSet)
