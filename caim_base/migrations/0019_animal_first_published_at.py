# Generated by Django 4.1 on 2022-10-19 18:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("caim_base", "0018_alter_animal_age_alter_animal_behaviour_kids_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="animal",
            name="first_published_at",
            field=models.DateTimeField(blank=True, default=None, null=True),
        ),
    ]