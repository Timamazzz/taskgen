# Generated by Django 3.0.8 on 2021-02-01 20:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tests', '0008_auto_20210201_2239'),
    ]

    operations = [
        migrations.RenameField(
            model_name='pattern',
            old_name='topic_number',
            new_name='topic',
        ),
    ]
