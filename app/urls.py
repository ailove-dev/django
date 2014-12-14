# -*- coding: utf-8 -*-

from django.conf import settings
from django.conf.urls import patterns, include, url, static
from django.contrib import admin
from filebrowser.sites import site


urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^grappelli/', include('grappelli.urls')),
    url(r'^admin/filebrowser/', include(site.urls)),
    url(r'^ckeditor/', include('ckeditor.urls')),
)

if settings.DEBUG and settings.CONFIG.SETTINGS['ENV'] == 'local':
    urlpatterns += static.static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static.static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)