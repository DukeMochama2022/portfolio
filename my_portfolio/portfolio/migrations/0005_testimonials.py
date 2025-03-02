# Generated by Django 5.1.6 on 2025-03-02 13:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0004_cv'),
    ]

    operations = [
        migrations.CreateModel(
            name='Testimonials',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('position', models.CharField(blank=True, max_length=100, null=True)),
                ('feedback', models.TextField()),
                ('image', models.ImageField(blank=True, null=True, upload_to='testmonials/')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
