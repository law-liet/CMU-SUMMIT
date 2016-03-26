# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Applicant',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=64)),
                ('email', models.EmailField(max_length=64)),
                ('major', models.CharField(max_length=64)),
                ('university', models.CharField(max_length=128)),
                ('graduate_time', models.DateField()),
                ('interested_company', models.CharField(max_length=128)),
                ('resume', models.FileField(default=None, upload_to=b'')),
            ],
        ),
        migrations.RemoveField(
            model_name='user',
            name='interested_company',
        ),
        migrations.AddField(
            model_name='user',
            name='degree',
            field=models.CharField(default=b'none', max_length=64),
        ),
        migrations.AddField(
            model_name='user',
            name='department',
            field=models.CharField(default=b'none', max_length=128),
        ),
        migrations.AddField(
            model_name='user',
            name='institution',
            field=models.CharField(default=b'none', max_length=128),
        ),
        migrations.AddField(
            model_name='user',
            name='major',
            field=models.CharField(default=b'none', max_length=64),
        ),
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(max_length=64),
        ),
        migrations.AlterField(
            model_name='user',
            name='phone',
            field=models.CharField(max_length=64),
        ),
    ]
