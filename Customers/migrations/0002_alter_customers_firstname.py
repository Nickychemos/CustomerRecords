# Generated by Django 5.1.7 on 2025-04-04 13:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Customers', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customers',
            name='FirstName',
            field=models.TextField(max_length=255),
        ),
    ]
