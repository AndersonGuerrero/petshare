# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-10-05 15:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='APP_Photo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nickname', models.CharField(help_text='nombre de usuario', max_length=1000)),
                ('pets_name', models.CharField(help_text='Nombre de la mascota', max_length=1000)),
                ('photo', models.CharField(help_text='foto de la mascota', max_length=1000)),
                ('likes', models.IntegerField(help_text='Votaciones de usuarios anonimos')),
            ],
            options={
                'db_table': 'app_photo',
            },
        ),
    ]
