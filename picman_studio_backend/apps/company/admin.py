from django.contrib import admin

from picman_studio_backend.apps.company.models import Company, Contact

admin.site.register(Company)
admin.site.register(Contact)
