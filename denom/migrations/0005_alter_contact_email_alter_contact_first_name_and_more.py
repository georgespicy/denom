# Generated by Django 4.1.5 on 2023-01-11 21:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("denom", "0004_subcriber_date_subscribed_alter_contact_message"),
    ]

    operations = [
        migrations.AlterField(
            model_name="contact",
            name="email",
            field=models.EmailField(max_length=50),
        ),
        migrations.AlterField(
            model_name="contact",
            name="first_name",
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name="contact",
            name="phone_number",
            field=models.PositiveIntegerField(),
        ),
        migrations.AlterField(
            model_name="subcriber",
            name="email",
            field=models.EmailField(max_length=50),
        ),
    ]
