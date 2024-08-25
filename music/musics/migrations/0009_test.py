# Generated by Django 5.0.1 on 2024-08-21 18:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('musics', '0008_alter_musics_slug'),
    ]

    operations = [
        migrations.CreateModel(
            name='Test',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('slug', models.SlugField(default='', unique=True)),
            ],
        ),
    ]
