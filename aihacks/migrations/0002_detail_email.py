# Generated by Django 3.0.3 on 2020-02-26 04:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aihacks', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='detail',
            name='Email',
            field=models.EmailField(default='', max_length=200),
        ),
    ]
