# Generated by Django 5.1.2 on 2024-10-28 13:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user_model',
            name='age',
            field=models.PositiveIntegerField(default=0),
        ),
    ]