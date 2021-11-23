# Generated by Django 3.2.4 on 2021-11-21 23:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tests', '0022_question_user_answer'),
    ]

    operations = [
        migrations.CreateModel(
            name='Questions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('difficulty', models.BooleanField(default=False)),
                ('correct_answer', models.IntegerField()),
                ('heading', models.CharField(max_length=128)),
                ('body', models.TextField()),
                ('answers', models.TextField()),
                ('user_answer', models.TextField(default=0)),
            ],
        ),
        migrations.RemoveField(
            model_name='question',
            name='user_answer',
        ),
    ]