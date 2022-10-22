# Generated by Django 4.1 on 2022-10-20 08:38

from django.conf import settings
import django.contrib.gis.db.models.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("caim_base", "0019_animal_first_published_at"),
    ]

    operations = [
        migrations.CreateModel(
            name="SavedSearch",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=64)),
                (
                    "animal_type",
                    models.CharField(
                        choices=[("DOG", "Dog"), ("CAT", "Cat")],
                        default="DOG",
                        max_length=3,
                    ),
                ),
                (
                    "zip_code",
                    models.CharField(
                        blank=True, default=None, max_length=16, null=True
                    ),
                ),
                (
                    "geo_location",
                    django.contrib.gis.db.models.fields.PointField(srid=4326),
                ),
                ("radius", models.IntegerField(blank=True, default=None, null=True)),
                (
                    "sex",
                    models.CharField(
                        blank=True,
                        choices=[("F", "Female"), ("M", "Male")],
                        default=None,
                        max_length=1,
                        null=True,
                    ),
                ),
                (
                    "size",
                    models.CharField(
                        blank=True,
                        choices=[
                            ("S", "Small (0-25 lbs)"),
                            ("M", "Medium (26-60 lbs)"),
                            ("L", "Large (61-100 lbs)"),
                            ("XL", "X-Large (101 lbs+)"),
                        ],
                        default=None,
                        max_length=2,
                        null=True,
                    ),
                ),
                (
                    "age",
                    models.CharField(
                        blank=True,
                        choices=[
                            ("BABY", "Puppy (< 1 year)"),
                            ("YOUNG", "Young (1-3 years)"),
                            ("ADULT", "Adult (3-8 years)"),
                            ("SENIOR", "Senior (8+ years)"),
                        ],
                        default=None,
                        max_length=8,
                        null=True,
                    ),
                ),
                (
                    "euth_date_within_days",
                    models.IntegerField(blank=True, default=None, null=True),
                ),
                (
                    "goodwith_cats",
                    models.BooleanField(blank=True, default=None, null=True),
                ),
                (
                    "goodwith_dogs",
                    models.BooleanField(blank=True, default=None, null=True),
                ),
                (
                    "goodwith_kids",
                    models.BooleanField(blank=True, default=None, null=True),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                (
                    "breed",
                    models.ForeignKey(
                        blank=True,
                        default=None,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="+",
                        to="caim_base.breed",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]