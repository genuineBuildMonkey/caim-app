# Generated by Django 4.1 on 2022-09-02 20:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("caim_base", "0002_alter_animalcomment_edited_at"),
    ]

    operations = [
        migrations.RenameField(
            model_name="animalimage",
            old_name="primary_photo",
            new_name="photo",
        ),
    ]
