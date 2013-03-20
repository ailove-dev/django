from django.contrib import admin
from django.conf import settings

def imageable_field(object):
    path = object.attachment.folder
    file = object.attachment.version_name(settings.FILEBROWSER_ADMIN_THUMBNAIL)
    return '<img src="' + settings.MEDIA_URL + path + '/' + file + '" />'

imageable_field.allow_tags = True

class OrderableAdmin(admin.ModelAdmin):
    list_display = list_editable = exclude = ('position',)

    class Meta:
        abstract = True

    class Media:
        js = (
            'capable/js/orderable.js',
        )
