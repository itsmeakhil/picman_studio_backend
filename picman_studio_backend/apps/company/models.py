from django.db import models

from picman_studio_backend.apps.utils.base_manager import BaseManager
from picman_studio_backend.apps.utils.base_model import BaseModel
from picman_studio_backend.apps.utils.helpers import id_generator


class Company(BaseModel):
    name = models.CharField(max_length=100, null=True, blank=True, unique=True)
    company_id = models.CharField(max_length=20, default=id_generator('COMP_'), editable=False)
    location = models.CharField(max_length=20, null=True, blank=True)
    email = models.EmailField(max_length=100, null=True, blank=True)

    objects = BaseManager()

    def __str__(self):
        return self.id.__str__()

    class Meta:
        db_table = 'COMPANY'
