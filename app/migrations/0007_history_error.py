# Generated by Django 4.0.4 on 2022-06-23 17:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_alter_history_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='history',
            name='error',
            field=models.BooleanField(default=False),
        ),
    ]
