# Generated by Django 3.2.8 on 2022-02-17 14:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('item_name', models.CharField(max_length=50)),
                ('date_perform', models.DateField()),
            ],
        ),
    ]