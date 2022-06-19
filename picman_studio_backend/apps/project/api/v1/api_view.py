from rest_framework import viewsets

from picman_studio_backend.apps.project.api.v1.serializer import ProjectSerializer, ProjectUpdateSerializer, \
    ProjectListSerializer, ClientSerializer, EventSerializer, AlbumSerializer
from picman_studio_backend.apps.project.models import Project, Client, Event, Album
from picman_studio_backend.apps.utils import response_helper


class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.get_all_active()
    serializer_class = ProjectSerializer
    serializer_action_classes = {
        'list': ProjectListSerializer,
        'retrieve': ProjectListSerializer,
        'partial_update': ProjectUpdateSerializer,
        'update': ProjectUpdateSerializer,
        'create': ProjectSerializer
    }

    def get_serializer_class(self):
        try:
            return self.serializer_action_classes[self.action]
        except (KeyError, AttributeError):
            return super().get_serializer_class()

    def retrieve(self, request, pk=None, *args, **kwargs):
        obj = self.get_object()
        serializer = self.serializer_class(obj)
        return response_helper.http_200('Project details loaded', serializer.data)

    def partial_update(self, request, *args, **kwargs):
        obj = self.get_object()
        serializer = ProjectUpdateSerializer(obj, data=self.request.data, partial=True)
        if not serializer.is_valid():
            return response_helper.http_400('Invalid Data', serializer.errors)
        serializer.save(created_by=self.request.user)
        return response_helper.http_201('Project created successfully', serializer.data)

    def create(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        if not serializer.is_valid():
            return response_helper.http_400('Invalid Data', serializer.errors)
        serializer.save(created_by=self.request.user)
        return response_helper.http_201('Project created successfully', serializer.data)

    def destroy(self, request, pk=None, *args, **kwargs):
        if not pk:
            return response_helper.http_400_message('Please provide Project id')
        Project.objects.soft_delete(pk)
        return response_helper.http_200_message('Project deleted successfully')

    def list(self, request, *args, **kwargs):
        response = super(ProjectViewSet, self).list(request, *args, **kwargs)
        return response_helper.http_200('Projects list loaded successfully', response.data)

    def get_queryset(self):
        queryset = super().get_queryset()
        company_id = self.request.user.company
        if company_id:
            queryset = queryset.filter(company=company_id)
        return queryset.order_by('-name')


class ClientViewSet(viewsets.ModelViewSet):
    queryset = Client.objects.get_all_active()
    serializer_class = ClientSerializer
    serializer_action_classes = {
        'list': ClientSerializer,
        'retrieve': ClientSerializer,
        'partial_update': ClientSerializer,
        'update': ClientSerializer,
        'create': ClientSerializer
    }

    def get_serializer_class(self):
        try:
            return self.serializer_action_classes[self.action]
        except (KeyError, AttributeError):
            return super().get_serializer_class()

    def retrieve(self, request, pk=None, *args, **kwargs):
        obj = self.get_object()
        serializer = self.serializer_class(obj)
        return response_helper.http_200('Client details loaded', serializer.data)

    def partial_update(self, request, *args, **kwargs):
        obj = self.get_object()
        serializer = ClientSerializer(obj, data=self.request.data, partial=True)
        if not serializer.is_valid():
            return response_helper.http_400('Invalid Data', serializer.errors)
        serializer.save(created_by=self.request.user)
        return response_helper.http_201('Client created successfully', serializer.data)

    def create(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        if not serializer.is_valid():
            return response_helper.http_400('Invalid Data', serializer.errors)
        serializer.save(created_by=self.request.user, company=self.request.user.company)
        return response_helper.http_201('Client created successfully', serializer.data)

    def destroy(self, request, pk=None, *args, **kwargs):
        if not pk:
            return response_helper.http_400_message('Please provide Project id')
        Project.objects.soft_delete(pk)
        return response_helper.http_200_message('Client deleted successfully')

    def list(self, request, *args, **kwargs):
        response = super(ClientViewSet, self).list(request, *args, **kwargs)
        return response_helper.http_200('Client list loaded successfully', response.data)

    def get_queryset(self):
        queryset = super().get_queryset()
        company_id = self.request.user.company
        if company_id:
            queryset = queryset.filter(company=company_id)
        return queryset.order_by('-name')


class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.get_all_active()
    serializer_class = EventSerializer
    serializer_action_classes = {
        'list': EventSerializer,
        'retrieve': EventSerializer,
        'partial_update': EventSerializer,
        'update': EventSerializer,
        'create': EventSerializer
    }

    def get_serializer_class(self):
        try:
            return self.serializer_action_classes[self.action]
        except (KeyError, AttributeError):
            return super().get_serializer_class()

    def retrieve(self, request, pk=None, *args, **kwargs):
        obj = self.get_object()
        serializer = self.serializer_class(obj)
        return response_helper.http_200('Event details loaded', serializer.data)

    def partial_update(self, request, *args, **kwargs):
        obj = self.get_object()
        serializer = EventSerializer(obj, data=self.request.data, partial=True)
        if not serializer.is_valid():
            return response_helper.http_400('Invalid Data', serializer.errors)
        serializer.save(created_by=self.request.user)
        return response_helper.http_201('Event created successfully', serializer.data)

    def create(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        if not serializer.is_valid():
            return response_helper.http_400('Invalid Data', serializer.errors)
        serializer.save(created_by=self.request.user, company=self.request.user.company)
        return response_helper.http_201('Event created successfully', serializer.data)

    def destroy(self, request, pk=None, *args, **kwargs):
        if not pk:
            return response_helper.http_400_message('Please provide Project id')
        Event.objects.soft_delete(pk)
        return response_helper.http_200_message('Event deleted successfully')

    def list(self, request, *args, **kwargs):
        response = super(EventViewSet, self).list(request, *args, **kwargs)
        return response_helper.http_200('Event list loaded successfully', response.data)

    def get_queryset(self):
        queryset = super().get_queryset()
        company_id = self.request.user.company
        if company_id:
            queryset = queryset.filter(company=company_id)
        return queryset.order_by('-name')


class AlbumViewSet(viewsets.ModelViewSet):
    queryset = Album.objects.get_all_active()
    serializer_class = AlbumSerializer
    serializer_action_classes = {
        'list': AlbumSerializer,
        'retrieve': AlbumSerializer,
        'partial_update': AlbumSerializer,
        'update': AlbumSerializer,
        'create': AlbumSerializer
    }

    def get_serializer_class(self):
        try:
            return self.serializer_action_classes[self.action]
        except (KeyError, AttributeError):
            return super().get_serializer_class()

    def retrieve(self, request, pk=None, *args, **kwargs):
        obj = self.get_object()
        serializer = self.serializer_class(obj)
        return response_helper.http_200('Album details loaded', serializer.data)

    def partial_update(self, request, *args, **kwargs):
        obj = self.get_object()
        serializer = AlbumSerializer(obj, data=self.request.data, partial=True)
        if not serializer.is_valid():
            return response_helper.http_400('Invalid Data', serializer.errors)
        serializer.save(created_by=self.request.user)
        return response_helper.http_201('Album created successfully', serializer.data)

    def create(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        if not serializer.is_valid():
            return response_helper.http_400('Invalid Data', serializer.errors)
        serializer.save(created_by=self.request.user, company=self.request.user.company)
        return response_helper.http_201('Album created successfully', serializer.data)

    def destroy(self, request, pk=None, *args, **kwargs):
        if not pk:
            return response_helper.http_400_message('Please provide Album id')
        Album.objects.soft_delete(pk)
        return response_helper.http_200_message('Album deleted successfully')

    def list(self, request, *args, **kwargs):
        response = super(AlbumViewSet, self).list(request, *args, **kwargs)
        return response_helper.http_200('Album list loaded successfully', response.data)

    def get_queryset(self):
        queryset = super().get_queryset()
        company_id = self.request.user.company
        if company_id:
            queryset = queryset.filter(project__company=company_id)
        if self.request.query_params.get('project'):
            queryset = queryset.filter(project=self.request.query_params.get('project_id'))
        return queryset.order_by('-title')
