# Generated by Django 5.1.1 on 2025-01-13 13:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('spotify', '0003_vote_previous'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='vote',
            name='previous',
        ),
    ]