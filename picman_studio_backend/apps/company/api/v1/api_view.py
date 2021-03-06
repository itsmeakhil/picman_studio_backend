from rest_framework import viewsets

from picman_studio_backend.apps.company.api.v1.serializer import (
    CompanySerializer,
    CompanyUpdateSerializer,
    CompanyListSerializer, ContactSerializer
)
from picman_studio_backend.apps.company.models import Company, Contact
from picman_studio_backend.apps.utils import response_helper


class CompanyViewSet(viewsets.ModelViewSet):
    queryset = Company.objects.get_all_active()
    serializer_class = CompanySerializer
    serializer_action_classes = {
        'list': CompanyListSerializer,
        'retrieve': CompanyListSerializer,
        'partial_update': CompanyUpdateSerializer,
        'update': CompanyUpdateSerializer,
        'create': CompanySerializer
    }

    def get_serializer_class(self):
        try:
            return self.serializer_action_classes[self.action]
        except (KeyError, AttributeError):
            return super().get_serializer_class()

    def retrieve(self, request, pk=None, *args, **kwargs):
        obj = self.get_object()
        serializer = self.serializer_class(obj)
        return response_helper.http_200('Company details loaded', serializer.data)

    def partial_update(self, request, *args, **kwargs):
        obj = self.get_object()
        serializer = CompanyUpdateSerializer(obj, data=self.request.data, partial=True)
        if not serializer.is_valid():
            return response_helper.http_400('Invalid Data', serializer.errors)
        serializer.save(created_by=self.request.user)
        return response_helper.http_201('Company created successfully', serializer.data)

    def create(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        if not serializer.is_valid():
            return response_helper.http_400('Invalid Data', serializer.errors)
        serializer.save(created_by=self.request.user)
        return response_helper.http_201('Company created successfully', serializer.data)

    def destroy(self, request, pk=None, *args, **kwargs):
        if not pk:
            return response_helper.http_400_message('Please provide Project id')
        Company.objects.soft_delete(pk)
        return response_helper.http_200_message('Company deleted successfully')

    def list(self, request, *args, **kwargs):
        response = super(CompanyViewSet, self).list(request, *args, **kwargs)
        return response_helper.http_200('Company list loaded successfully', response.data)


class ContactViewSet(viewsets.ModelViewSet):
    queryset = Contact.objects.get_all_active()
    serializer_class = ContactSerializer
    serializer_action_classes = {
        'list': ContactSerializer,
        'retrieve': ContactSerializer,
        'partial_update': ContactSerializer,
        'update': ContactSerializer,
        'create': ContactSerializer
    }

    def get_serializer_class(self):
        try:
            return self.serializer_action_classes[self.action]
        except (KeyError, AttributeError):
            return super().get_serializer_class()

    def retrieve(self, request, pk=None, *args, **kwargs):
        obj = self.get_object()
        serializer = self.serializer_class(obj)
        return response_helper.http_200('Contact details loaded', serializer.data)

    def partial_update(self, request, *args, **kwargs):
        obj = self.get_object()
        serializer = CompanyUpdateSerializer(obj, data=self.request.data, partial=True)
        if not serializer.is_valid():
            return response_helper.http_400('Invalid Data', serializer.errors)
        serializer.save(created_by=self.request.user)
        return response_helper.http_201('Contact created successfully', serializer.data)

    def create(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        if not serializer.is_valid():
            return response_helper.http_400('Invalid Data', serializer.errors)
        serializer.save(created_by=self.request.user)
        return response_helper.http_201('Contact created successfully', serializer.data)

    def destroy(self, request, pk=None, *args, **kwargs):
        if not pk:
            return response_helper.http_400_message('Please provide Project id')
        Contact.objects.soft_delete(pk)
        return response_helper.http_200_message('Contact deleted successfully')

    def list(self, request, *args, **kwargs):
        response = super(ContactViewSet, self).list(request, *args, **kwargs)
        return response_helper.http_200('Contact list loaded successfully', response.data)

    def get_queryset(self):
        queryset = super(ContactViewSet, self).get_queryset()
        company_id = self.request.user.company
        if company_id:
            queryset = queryset.filter(company=company_id)
        return queryset
