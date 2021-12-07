# Generated by Django 3.2.5 on 2021-07-20 05:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('body', models.TextField(max_length=500)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('edited', models.DateTimeField(auto_now=True)),
                ('readers', models.PositiveIntegerField(default=0)),
                ('slug', models.SlugField(blank=True, null=True, unique=True)),
                ('readtime', models.IntegerField(default=0)),
            ],
        ),
    ]
