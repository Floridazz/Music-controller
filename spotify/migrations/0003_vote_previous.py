# Generated by Django 5.1.1 on 2025-01-13 12:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('spotify', '0002_vote'),
    ]

    operations = [
        migrations.AddField(
            model_name='vote',
            name='previous',
            field=models.BooleanField(default=False),
        ),
    ]
