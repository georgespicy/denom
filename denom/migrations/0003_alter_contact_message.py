# Generated by Django 4.1.5 on 2023-01-11 15:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("denom", "0002_contact"),
    ]

    operations = [
        migrations.AlterField(
            model_name="contact",
            name="message",
            field=models.CharField(max_length=1000),
        ),
    ]
