# Generated by Django 4.2.8 on 2024-01-12 05:58

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("citizen", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="citizeninput",
            name="input_date",
            field=models.DateField(null=True),
        ),
    ]
