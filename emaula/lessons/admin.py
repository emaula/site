from django.contrib import admin
from embed_video.admin import AdminVideoMixin

from .models import Text, Link, Image, Video, Audio


class TextAdmin(admin.ModelAdmin):
    list_display = ('title', 'text', 'source')
    list_filter = ['title']
    search_fields = ['title', 'source']


class LinkAdmin(admin.ModelAdmin):
    list_display = ['name', 'url', 'access_date']
    search_fields = ['name', 'url']


class ImageAdmin(admin.ModelAdmin):
    list_display = ('alt', 'image_path')
    search_fields = ['alt', 'image_path']


class VideoAdmin(AdminVideoMixin, admin.ModelAdmin):
    list_display = ('title', 'video')
    search_fields = ['title', 'video']


class AudioAdmin(AdminVideoMixin, admin.ModelAdmin):
    list_display = ('title', 'audio')
    search_fields = ['title', 'audio']


# Uncomment this to show objects in the admin
"""
admin.site.register(Text, TextAdmin)
admin.site.register(Link, LinkAdmin)
admin.site.register(Image, ImageAdmin)
admin.site.register(Video, VideoAdmin)
admin.site.register(Audio, AudioAdmin)
"""
