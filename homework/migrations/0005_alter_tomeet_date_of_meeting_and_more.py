# Generated by Django 4.0.3 on 2022-05-05 04:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homework', '0004_alter_todo_created_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tomeet',
            name='date_of_meeting',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='tomeet',
            name='phone_number',
            field=models.IntegerField(default=0),
        ),
    ]
