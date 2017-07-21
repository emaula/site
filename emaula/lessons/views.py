from django.shortcuts import render, get_object_or_404
from django.views import generic

from .models import Text, Link, Image, Video, Audio


class IndexView(generic.ListView):
    template_name = 'lessons/index.html'
    context_object_name = 'all_lessons_objects'

    text_list = Text.objects.all()
    link_list = Link.objects.all()
    image_list = Image.objects.all()
    video_list = Video.objects.all()
    audio_list = Audio.objects.all()

    context = {
        'text_list': text_list,
        'link_list': link_list,
        'image_list': image_list,
        'video_list': video_list,
        'audio_list': audio_list,
    }

    def get_queryset(self):
        return self.context


class TextListView(generic.ListView):
    model = Text

    def get_queryset(self):
        return Text.objects.all()


class LinkListView(generic.ListView):
    model = Link

    def get_queryset(self):
        return Link.objects.all()


class ImageListView(generic.ListView):
    model = Image

    def get_queryset(self):
        return Image.objects.all()


class AudioListView(generic.ListView):
    model = Audio

    def get_queryset(self):
        return Audio.objects.all()


class VideoListView(generic.ListView):
    model = Video

    def get_queryset(self):
        return Video.objects.all()


class TextDetailView(generic.DetailView):
    model = Text

    def text_detail(request, pk):
        text = get_object_or_404(Text, pk=pk)
        return render(request, 'lessons/detail.html', {
            'text': text,
        })


class LinkDetailView(generic.DetailView):
    model = Link

    def Link_detail(request, pk):
        link = get_object_or_404(Link, pk=pk)
        return render(request, 'lessons/detail.html', {
            'link': link.url,
        })


class ImageDetailView(generic.DetailView):
    model = Image

    def image_detail(request, pk):
        image = get_object_or_404(Image, pk=pk)
        return render(request, 'lessons/detail.html', {
            'image': image,
        })


class VideoDetailView(generic.DetailView):
    model = Video

    def video_detail(request, pk):
        video = get_object_or_404(Video, pk=pk)
        return render(request, 'lessons/detail.html', {
            'video': video,
        })


class AudioDetailView(generic.DetailView):
    model = Audio

    def audio_detail(request, pk):
        audio = get_object_or_404(Audio, pk=pk)
        return render(request, 'lessons/detail.html', {
            'audio': audio,
        })
