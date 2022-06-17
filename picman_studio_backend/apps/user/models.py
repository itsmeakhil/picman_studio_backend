from django.contrib.auth.models import AbstractUser
from django.db import models

from picman_studio_backend.apps.company.models import Company
from picman_studio_backend.apps.user.manager import UserManager
from picman_studio_backend.apps.utils.base_manager import BaseManager
from picman_studio_backend.apps.utils.base_model import BaseModel
from picman_studio_backend.apps.utils.constants import INVITE_INVITED, INVITE_PENDING, INVITE_ACCEPTED


class Role(models.Model):
    CUSTOMER = 3
    ADMIN = 0
    STUDIO_ADMIN = 1
    STUDIO_MANAGER = 2

    ROLE_CHOICES = (
        (CUSTOMER, 'Customer'),
        (ADMIN, 'Admin'),
        (STUDIO_MANAGER, 'Studio Manager'),
        (STUDIO_ADMIN, 'Studio Admin'),
    )
    id = models.PositiveSmallIntegerField(choices=ROLE_CHOICES, primary_key=True)

    def __str__(self):
        return self.get_id_display()


class User(AbstractUser):
    username = models.CharField(max_length=100, null=True, blank=True, unique=True)
    uid = models.CharField(max_length=100, null=True, blank=True, unique=True)
    company = models.ForeignKey(Company, on_delete=models.CASCADE, null=True, blank=True)
    email = models.CharField(max_length=255, unique=True, null=True, blank=True)
    password = models.CharField(max_length=255, null=True, blank=True)
    phone_number = models.CharField(max_length=255, null=True, blank=True)
    profile_image = models.ImageField(upload_to='images/profile', null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    is_active = models.BooleanField(default=True)
    is_phone_verified = models.BooleanField(default=False)
    is_terms_and_conditions_accepted = models.BooleanField(default=False)
    allow_multiple_sessions = models.BooleanField(default=False)
    role = models.ForeignKey(Role, on_delete=models.SET_DEFAULT, default=2)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()

    def __str__(self):
        return self.id.__str__()

    class Meta:
        db_table = 'USER'


class Team(BaseModel):
    company = models.ForeignKey(Company, on_delete=models.SET_NULL, null=True, blank=True)
    users = models.ManyToManyField(User, null=True)

    objects = BaseManager()

    def __str__(self):
        return self.id.__str__()

    class Meta:
        db_table = 'TEAM'


class UserInvite(BaseModel):

    INVITE_STATUS = (
        (INVITE_INVITED, 'Invited'),
        (INVITE_PENDING, 'Pending'),
        (INVITE_ACCEPTED, 'Accepted'),
    )

    company = models.ForeignKey(Company, on_delete=models.SET_NULL, null=True, blank=True)
    email = models.EmailField(max_length=100, null=True, blank=True, unique=True)
    status = models.PositiveSmallIntegerField(choices=INVITE_STATUS, default=1, null=True, blank=True)
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)

    objects = BaseManager()

    def __str__(self):
        return self.id.__str__()

    class Meta:
        db_table = 'USER_INVITES'
