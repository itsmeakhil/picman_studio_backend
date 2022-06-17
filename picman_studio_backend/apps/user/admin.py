from django.contrib import admin

from picman_studio_backend.apps.user.models import User, Role, UserInvite

admin.site.register(User)
admin.site.register(UserInvite)
admin.site.register(Role)
