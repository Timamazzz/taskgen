# Generated by Django 3.2.4 on 2021-11-22 05:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tests', '0025_rename_questions_questionsdata'),
    ]

    operations = [
        migrations.AddField(
            model_name='questionsdata',
            name='patterns',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='tests.pattern'),
        ),
    ]
