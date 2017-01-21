# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-21 21:35
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='OpenTicket',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('guest_number', models.IntegerField()),
                ('guest_name', models.CharField(max_length=20)),
                ('guest_choice', models.ManyToManyField(to='app.Menu_Item')),
                ('server_is', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Employee')),
            ],
        ),
    ]