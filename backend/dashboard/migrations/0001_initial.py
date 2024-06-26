# Generated by Django 5.0.6 on 2024-05-08 20:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Insight',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('end_year', models.CharField(blank=True, max_length=10)),
                ('intensity', models.IntegerField()),
                ('sector', models.CharField(blank=True, max_length=100)),
                ('topic', models.CharField(blank=True, max_length=100)),
                ('insight', models.TextField()),
                ('url', models.URLField()),
                ('region', models.CharField(max_length=100)),
                ('start_year', models.CharField(blank=True, max_length=10)),
                ('impact', models.CharField(blank=True, max_length=100)),
                ('added', models.DateTimeField()),
                ('published', models.DateTimeField()),
                ('country', models.CharField(blank=True, max_length=100)),
                ('relevance', models.IntegerField()),
                ('pestle', models.CharField(blank=True, max_length=100)),
                ('source', models.CharField(max_length=100)),
                ('title', models.CharField(max_length=255)),
                ('likelihood', models.IntegerField()),
            ],
        ),
    ]
