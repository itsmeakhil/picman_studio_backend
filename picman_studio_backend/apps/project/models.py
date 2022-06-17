from django.contrib.postgres.fields import ArrayField
from django.db import models

from picman_studio_backend.apps.company.models import Company
from picman_studio_backend.apps.user.models import User
from picman_studio_backend.apps.utils.base_manager import BaseManager
from picman_studio_backend.apps.utils.base_model import BaseModel
from picman_studio_backend.apps.utils.helpers import id_generator


class Project(BaseModel):
    name = models.CharField(max_length=100, null=True, blank=True, unique=True)
    project_id = models.CharField(max_length=20, default=id_generator('PROJ_'), editable=False)
    company = models.ForeignKey(Company, on_delete=models.SET_NULL, null=True, blank=True)
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True,
                                   related_name='project_created_by')
    updated_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True,
                                   related_name='project_updated_by')

    objects = BaseManager()

    def __str__(self):
        return self.id.__str__()

    class Meta:
        db_table = 'PROJECT'


class ProjectMedia(BaseModel):
    title = models.CharField(max_length=100, null=True, blank=True)
    project = models.ForeignKey(Project, on_delete=models.CASCADE, null=True, blank=True)
    images = ArrayField(models.JSONField(max_length=255, null=True, blank=True), null=True, blank=True)
    videos = ArrayField(models.URLField(max_length=255, null=True, blank=True), null=True, blank=True)
    files = ArrayField(models.URLField(max_length=255, null=True, blank=True), null=True, blank=True)

    selected_images = ArrayField(models.JSONField(max_length=255, null=True, blank=True), null=True, blank=True)
    selected_videos = ArrayField(models.URLField(max_length=255, null=True, blank=True), null=True, blank=True)
    selected_files = ArrayField(models.URLField(max_length=255, null=True, blank=True), null=True, blank=True)

    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True,
                                   related_name='media_created_by')
    updated_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True,
                                   related_name='media_updated_by')
    access_permissions = ArrayField(models.EmailField(max_length=30), null=True, blank=True)

    objects = BaseManager()

    def __str__(self):
        return self.id.__str__()

    class Meta:
        db_table = 'PROJECT_MEDIA'


class Client(BaseModel):
    name = models.CharField(max_length=100, null=True, blank=True, unique=True)
    phone = models.CharField(max_length=100, null=True, blank=True, unique=True)
    email = models.EmailField(max_length=100, null=True, blank=True)
    client_id = models.CharField(max_length=20, default=id_generator('CLI_'), editable=False)
    project = models.ForeignKey(Project, on_delete=models.CASCADE, null=True, blank=True)
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True,
                                   related_name='client_created_by')
    updated_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True,
                                   related_name='client_updated_by')

    objects = BaseManager()

    def __str__(self):
        return self.id.__str__()

    class Meta:
        db_table = 'CLIENT'
