# Generated by Django 4.1 on 2022-09-02 20:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("caim_base", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="animalcomment",
            name="edited_at",
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
