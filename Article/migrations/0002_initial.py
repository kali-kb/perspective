# Generated by Django 3.2.5 on 2021-07-20 05:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Article', '0001_initial'),
        ('Profile', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='insightful',
            field=models.ManyToManyField(blank=True, related_name='_Article_article_insightful_+', to='Profile.UserProfile', verbose_name='Insightful'),
        ),
        migrations.AddField(
            model_name='article',
            name='publisher',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='article', to='Profile.userprofile', verbose_name='Publisher'),
        ),
    ]
