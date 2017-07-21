from django.contrib import admin

from lessons.models import Text, Link, Image, Video, Audio
from .models import Classroom, Professor, Subject, Year


class TextInline(admin.StackedInline):
    model = Text
    extra = 1


class LinkInline(admin.StackedInline):
    model = Link
    extra = 1


class ImageInline(admin.StackedInline):
    model = Image
    extra = 1


class VideoInline(admin.StackedInline):
    model = Video
    extra = 1


class AudioInline(admin.StackedInline):
    model = Audio
    extra = 1


@admin.register(Classroom)
class ClassroomAdmin(admin.ModelAdmin):
    list_display = ('title', 'display_subject', 'display_year')
    fieldsets = [
        ('Data: ', {'fields': ['subject', 'year']}),
        ('Content: ', {'fields': ['author', 'title', 'summary']}),
        ('Date:', {'fields': ['created_date', 'published_date']}),
    ]
    list_filter = ['title', 'subject', 'year', 'author']
    search_fields = ['title']
    inlines = [TextInline, LinkInline, ImageInline, VideoInline, AudioInline]


@admin.register(Professor)
class ProfessorAdmin(admin.ModelAdmin):
    pass


admin.site.register(Subject)
admin.site.register(Year)
