# Generated by Django 4.0.3 on 2022-04-08 18:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='user',
            field=models.TextField(blank=True, null=True),
        ),
    ]
