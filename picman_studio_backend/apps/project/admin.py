from django.contrib import admin

from picman_studio_backend.apps.project.models import Project, ProjectMedia

admin.site.register(Project)
admin.site.register(ProjectMedia)
