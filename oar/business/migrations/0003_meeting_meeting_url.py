# Generated by Django 5.0.9 on 2024-10-02 18:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('business', '0002_feedback'),
    ]

    operations = [
        migrations.AddField(
            model_name='meeting',
            name='meeting_url',
            field=models.URLField(default='example.com'),
        ),
    ]
