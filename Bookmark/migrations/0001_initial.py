# Generated by Django 3.2.5 on 2021-07-20 05:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Article', '0002_initial'),
        ('Profile', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Saved',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('article', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='saved', to='Article.article')),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='saved', to='Profile.userprofile')),
            ],
        ),
    ]
