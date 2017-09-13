# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-09-11 19:23
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Classroom',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, help_text='Tema ou título da aula', max_length=255)),
                ('summary', models.TextField(blank=True, help_text='Escreva um breve sumário da aula.', max_length=1000)),
                ('created_date', models.DateField(default=django.utils.timezone.now, help_text='Data de criação')),
                ('published_date', models.DateField(blank=True, help_text='Data de publicação', null=True)),
                ('views', models.IntegerField(default=0, help_text='Visitas')),
            ],
        ),
        migrations.CreateModel(
            name='ClassroomInstance',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('classroom', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='school.Classroom')),
            ],
        ),
        migrations.CreateModel(
            name='Professor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('picture', models.ImageField(default='pic_folder/user/no-img.jpg', upload_to='media')),
                ('first_name', models.CharField(help_text='Primeiro nome', max_length=255)),
                ('last_name', models.CharField(help_text='Último nome', max_length=255)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(blank=True, help_text='Disciplina ou cadeira', max_length=255, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Year',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.CharField(blank=True, help_text='Série ou ano', max_length=20)),
            ],
        ),
        migrations.AddField(
            model_name='classroom',
            name='author',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='classroom', to='school.Professor'),
        ),
        migrations.AddField(
            model_name='classroom',
            name='subject',
            field=models.ManyToManyField(help_text='Disciplina', to='school.Subject'),
        ),
        migrations.AddField(
            model_name='classroom',
            name='year',
            field=models.ManyToManyField(help_text='Selecione                                   um ano ou série para esta aula', to='school.Year'),
        ),
    ]