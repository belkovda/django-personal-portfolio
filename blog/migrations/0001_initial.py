# Generated by Django 4.0.4 on 2022-04-19 08:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('post_title', models.CharField(max_length=200)),
                ('date', models.DateField()),
                ('blog_text', models.TextField(max_length=250)),
            ],
        ),
    ]
