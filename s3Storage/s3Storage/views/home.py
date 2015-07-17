from django.shortcuts import render
from django.conf import settings


def home_view(request):
    return render(request, "desktop/site/home.html", {
        'static_enabled': True if 'custom_storages' in settings.STATICFILES_STORAGE else False,
        'compress_enabled': settings.COMPRESS_ENABLED,
        'media_enabled': True if 'custom_storages' in settings.DEFAULT_FILE_STORAGE else False
    })