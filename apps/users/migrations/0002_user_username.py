# Generated by Django 5.1.4 on 2024-12-23 12:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='username',
            field=models.CharField(default='test user', max_length=255, unique=True),
            preserve_default=False,
        ),
    ]