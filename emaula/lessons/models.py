from django.db import models
from django.utils import timezone
from embed_video.fields import EmbedVideoField

from school.models import Classroom


class Text(models.Model):
    """
    TODO: WYSIWYG
    """
    classroom = models.ForeignKey(Classroom,
                                  related_name='text',
                                  on_delete=models.SET_NULL,
                                  blank=True,
                                  null=True)

    title = models.CharField('Título', max_length=200)
    text = models.TextField('Texto', blank=True)
    source = models.URLField('Link para a fonte', blank=True)

    def __str__(self):
        return self.title


class Link(models.Model):

    classroom = models.ForeignKey(Classroom,
                                  related_name='link',
                                  on_delete=models.SET_NULL,
                                  blank=True,
                                  null=True)

    url = models.URLField(blank=True)
    name = models.CharField('Nome', max_length=600, blank=True)
    access_date = models.DateField('Data de acesso', default=timezone.now)

    def __str__(self):
        return '{0} - {1}'.format(self.name, self.url)


class Image(models.Model):

    classroom = models.ForeignKey(Classroom,
                                  related_name='image',
                                  on_delete=models.SET_NULL,
                                  blank=True,
                                  null=True)

    image_path = models.ImageField('Endereço da imagem',
                                   upload_to='media',
                                   default='pic_folder/user/no-img.jpg')
    alt = models.CharField('Texto alternativo',
                           max_length=1200,
                           blank=True)

    def __str__(self):
        return self.image_path.name


class Video(models.Model):

    classroom = models.ForeignKey(Classroom,
                                  related_name='video',
                                  on_delete=models.SET_NULL,
                                  blank=True,
                                  null=True)

    video = EmbedVideoField('Endereço do Youtube')
    title = models.CharField('Título do vídeo',
                             max_length=1200,
                             blank=True)

    def __str__(self):
        return '{0} - {1}'.format(self.title, self.video)


class Audio(models.Model):

    classroom = models.ForeignKey(Classroom,
                                  related_name='audio',
                                  on_delete=models.SET_NULL,
                                  blank=True,
                                  null=True)

    audio = EmbedVideoField('Endereço do SoundCloud')
    title = models.CharField('Título do áudio',
                             max_length=1200,
                             blank=True)

    def __str__(self):
        return '{0} - {1}'.format(self.title, self.audio)
