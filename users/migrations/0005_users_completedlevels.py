# Generated by Django 5.0.6 on 2024-06-24 14:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_alter_users_users_images'),
    ]

    operations = [
        migrations.AddField(
            model_name='users',
            name='completedLevels',
            field=models.CharField(blank=True, max_length=2000, null=True),
        ),
    ]
