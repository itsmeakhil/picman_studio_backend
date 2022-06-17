
from django.urls import include, path
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions
from rest_framework import routers

from picman_studio_backend.apps.company.api.v1.url import company_router
from picman_studio_backend.apps.project.api.v1.url import project_router
from picman_studio_backend.apps.user.api.v1.api_view import Logout, Login, Signup

schema_view = get_schema_view(
    openapi.Info(
        title="Pic-man Studio API Documentation.",
        default_version='v1',
        description="API Documentation",
        contact=openapi.Contact(email="info@wecodelife.com"),
        license=openapi.License(name="Proprietary Software"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

api_prefix = 'api/v1/'

router = routers.DefaultRouter()

router.registry.extend(project_router.registry)
router.registry.extend(company_router.registry)

urlpatterns = [

    path('api/v1/login/', Login.as_view(), name='login'),
    path('api/v1/logout/', Logout.as_view(), name='logout'),
    path('api/v1/logout/', Logout.as_view(), name='logout'),
    path('api/v1/signup/', Signup.as_view(), name='signup'),
    # apps
    path(api_prefix, include(router.urls)),

]

# Swagger API DOC
api_doc_url = [
    path(r'swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
