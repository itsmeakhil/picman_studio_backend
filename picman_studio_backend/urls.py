from django.contrib import admin
from django.urls import path

from picman_studio_backend.api.v1.url import urlpatterns as api_urls, api_doc_url

urlpatterns = [path('admin/', admin.site.urls)] + api_urls + api_doc_url
