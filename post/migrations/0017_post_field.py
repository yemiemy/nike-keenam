# Generated by Django 2.2.2 on 2019-06-22 13:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0016_remove_post_field'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='field',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
