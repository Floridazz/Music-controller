# Generated by Django 5.1.1 on 2025-01-13 13:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('spotify', '0005_vote_previous_alter_vote_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vote',
            name='user',
            field=models.CharField(max_length=50),
        ),
    ]