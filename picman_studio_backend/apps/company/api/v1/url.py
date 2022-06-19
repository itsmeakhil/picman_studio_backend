from rest_framework import routers

from picman_studio_backend.apps.company.api.v1.api_view import CompanyViewSet, ContactViewSet

company_router = routers.DefaultRouter()
company_router.register(r'company', CompanyViewSet)
company_router.register(r'contacts', ContactViewSet)
