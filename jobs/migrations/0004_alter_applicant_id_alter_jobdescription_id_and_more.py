# Generated by Django 4.1.7 on 2023-04-07 05:34

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("jobs", "0003_alter_portal_id"),
    ]

    operations = [
        migrations.AlterField(
            model_name="applicant",
            name="id",
            field=models.BigAutoField(
                auto_created=True, primary_key=True, serialize=False, verbose_name="ID"
            ),
        ),
        migrations.AlterField(
            model_name="jobdescription",
            name="id",
            field=models.BigAutoField(
                auto_created=True, primary_key=True, serialize=False, verbose_name="ID"
            ),
        ),
        migrations.AlterField(
            model_name="jobdescription",
            name="role",
            field=models.CharField(max_length=250),
        ),
    ]
