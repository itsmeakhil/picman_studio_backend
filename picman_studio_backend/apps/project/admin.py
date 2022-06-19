from django.contrib import admin

from picman_studio_backend.apps.project.models import Project, ProjectMedia, Album, Event, Client

admin.site.register(Project)
admin.site.register(ProjectMedia)
admin.site.register(Album)
admin.site.register(Event)
admin.site.register(Client)
