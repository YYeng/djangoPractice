# Generated by Django 3.2.8 on 2022-02-18 15:03

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('ToDo_App', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False),
        ),
    ]
