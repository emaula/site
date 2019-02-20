import uuid

from django.urls import reverse
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


# Ano ou série
class Year(models.Model):
    year = models.CharField(max_length=20,
                            help_text='Série ou ano. Ex: 1º ano',
                            blank=True)

    def __str__(self):
        return self.year


# Disciplina
class Subject(models.Model):
    subject = models.CharField(max_length=255,
                               help_text='Disciplina ou cadeira',
                               blank=True,
                               null=True)

    def __str__(self):
        return self.subject


# Aulas
class Classroom(models.Model):

    # TODO: Opção de deixar ou não pública a aula
    subject = models.ManyToManyField(Subject,
                                     help_text='Disciplina')
    title = models.CharField(max_length=255,
                             help_text='Tema ou título da aula',
                             blank=True)
    year = models.ManyToManyField(Year,
                                  help_text='Selecione \
                                  um ano ou série para esta aula')
    summary = models.TextField(max_length=1000,
                               help_text='Escreva um breve sumário da aula.',
                               blank=True)

    author = models.ForeignKey('Professor',
                               related_name='classroom',
                               blank=True,
                               on_delete=models.SET_NULL,
                               null=True)
    created_date = models.DateField(default=timezone.now,
                                    help_text='Data de criação')
    published_date = models.DateField(blank=True,
                                      null=True,
                                      help_text='Data de publicação')
    views = models.IntegerField(default=0, help_text='Visitas')

    def __str__(self):
        return '{0}'.format(self.title)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def get_absolute_url(self):
        return reverse('classroom_detail', args=[str(self.id)])

    def display_subject(self):
        return ', '.join(
            [subject.subject for subject in self.subject.all()])

    def display_year(self):
        return ', '.join(
            [year.year for year in self.year.all()[:3]])

    def display_author(self):
        return ', '.join(
            [author.author for author in self.author.all()[:3]])

    def display_text(self):
        object_texts = dict()
        for text in self.text.all():
            object_texts['title'] = text.title
            object_texts['text'] = text.text
            object_texts['source'] = text.source
        return object_texts

    def display_link(self):
        return ', '.join(
            [link.link for link in self.objects.link.all()])

    def display_image(self):
        object_images = dict()
        for image in self.image.all():
            object_images['image_path'] = image.image_path
            object_images['alt'] = image.alt
        return object_images

    display_author.short_description = 'Author'
    display_subject.short_description = 'Subject'
    display_year.short_description = 'Year'
    display_text.short_description = 'Text'
    display_link.short_description = 'Link'
    display_link.short_description = 'Image'


Classroom.objects.all().prefetch_related(
    'text', 'image', 'link', 'audio', 'video')


# Aula
class ClassroomInstance(models.Model):
    id = models.UUIDField(primary_key=True,
                          default=uuid.uuid4,
                          editable=False)
    classroom = models.ForeignKey('Classroom',
                                  on_delete=models.SET_NULL,
                                  null=True)

    def __str__(self):
        return '{0} - {1} - {2}'.format(self.id,
                                        self.classroom.title,
                                        self.classroom.year,
                                        self.classroom.subject)


# Professor
class Professor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    picture = models.ImageField(upload_to='media',
                                default='pic_folder/user/no-img.jpg')
    first_name = models.CharField(max_length=255,
                                  unique=False,
                                  help_text='Primeiro nome')
    last_name = models.CharField(max_length=255,
                                 unique=False,
                                 help_text='Último nome')

    def __str__(self):
        if self.user.first_name != '':
            return self.user.first_name.capitalize()
        else:
            return self.user.username.capitalize()

    def get_absolute_url(self):
        # Acessa uma professora específica
        return reverse('professor_detail', args=[str(self.id)])


Professor.objects.all().select_related('classroom').prefetch_related('user')
