# Generated by Django 3.2.4 on 2021-11-22 22:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tests', '0034_alter_questionsdata_user_answer'),
    ]

    operations = [
        migrations.AddField(
            model_name='questionsdata',
            name='point',
            field=models.IntegerField(default=0),
        ),
    ]