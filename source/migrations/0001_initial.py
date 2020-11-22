# Generated by Django 3.1.3 on 2020-11-20 06:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FeaturedArticle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('posted_by', models.CharField(max_length=30)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('text', models.TextField()),
                ('image', models.ImageField(default='test.jpg', null=True, upload_to='media/')),
                ('slug', models.SlugField(default='test-podcast')),
            ],
        ),
        migrations.CreateModel(
            name='FeaturedPodcast',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('posted_by', models.CharField(max_length=30)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('text', models.TextField()),
                ('image', models.ImageField(default='test.jpg', null=True, upload_to='media/')),
                ('audio_div', models.CharField(max_length=200, null=True)),
                ('script', models.CharField(max_length=200, null=True)),
                ('slug', models.SlugField(default='test-podcast')),
            ],
        ),
        migrations.CreateModel(
            name='Podcast',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('posted_by', models.CharField(max_length=30)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('text', models.TextField()),
                ('image', models.ImageField(default='test.jpg', null=True, upload_to='media/')),
                ('audio_div', models.CharField(max_length=200, null=True)),
                ('script', models.CharField(max_length=200, null=True)),
                ('slug', models.SlugField(default='test-podcast')),
            ],
        ),
        migrations.CreateModel(
            name='TopStories',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('posted_by', models.CharField(max_length=30)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('text', models.TextField()),
                ('image', models.ImageField(default='test.jpg', null=True, upload_to='media/')),
                ('slug', models.SlugField(default='test-podcast')),
            ],
        ),
    ]