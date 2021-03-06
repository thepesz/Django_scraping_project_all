# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-09-09 11:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Stat',
            fields=[
                ('word', models.CharField(max_length=40, primary_key=True, serialize=False)),
                ('author', models.CharField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='User1',
            fields=[
                ('word', models.CharField(max_length=40, primary_key=True, serialize=False)),
                ('quantity', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='User10',
            fields=[
                ('word', models.CharField(max_length=40, primary_key=True, serialize=False)),
                ('quantity', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='User2',
            fields=[
                ('word', models.CharField(max_length=40, primary_key=True, serialize=False)),
                ('quantity', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='User3',
            fields=[
                ('word', models.CharField(max_length=40, primary_key=True, serialize=False)),
                ('quantity', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='User4',
            fields=[
                ('word', models.CharField(max_length=40, primary_key=True, serialize=False)),
                ('quantity', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='User5',
            fields=[
                ('word', models.CharField(max_length=40, primary_key=True, serialize=False)),
                ('quantity', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='User6',
            fields=[
                ('word', models.CharField(max_length=40, primary_key=True, serialize=False)),
                ('quantity', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='User7',
            fields=[
                ('word', models.CharField(max_length=40, primary_key=True, serialize=False)),
                ('quantity', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='User8',
            fields=[
                ('word', models.CharField(max_length=40, primary_key=True, serialize=False)),
                ('quantity', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='User9',
            fields=[
                ('word', models.CharField(max_length=40, primary_key=True, serialize=False)),
                ('quantity', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Word_freq',
            fields=[
                ('word', models.CharField(max_length=40, primary_key=True, serialize=False)),
                ('quantity', models.IntegerField()),
            ],
        ),
    ]
