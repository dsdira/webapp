# Generated by Django 5.1.5 on 2025-02-01 16:52

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('times', '0017_wikiphoto'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cuaderno',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=200)),
                ('fecha_creacion', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Apunte',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contenido', models.TextField()),
                ('fecha_creacion', models.DateTimeField(auto_now=True)),
                ('subtitulo', models.CharField(blank=True, max_length=200, null=True)),
                ('cuaderno', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='times.cuaderno')),
            ],
        ),
    ]
