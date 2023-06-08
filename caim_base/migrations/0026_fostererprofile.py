# Generated by Django 4.1 on 2023-02-20 10:58

from django.conf import settings
import django.contrib.postgres.fields
from django.db import migrations, models
import django.db.models.deletion
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("caim_base", "0025_alter_animal_age_alter_savedsearch_age"),
    ]

    operations = [
        migrations.CreateModel(
            name="FostererProfile",
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
                ("description", models.TextField(blank=True)),
                (
                    "firstname",
                    models.CharField(
                        blank=True, default=None, max_length=64, null=True
                    ),
                ),
                (
                    "lastname",
                    models.CharField(
                        blank=True, default=None, max_length=64, null=True
                    ),
                ),
                (
                    "email",
                    models.EmailField(
                        blank=True, default=None, max_length=255, null=True
                    ),
                ),
                (
                    "phone",
                    phonenumber_field.modelfields.PhoneNumberField(
                        blank=True, default=None, max_length=128, null=True, region=None
                    ),
                ),
                (
                    "street_address",
                    models.CharField(
                        blank=True, default=None, max_length=244, null=True
                    ),
                ),
                (
                    "city",
                    models.CharField(
                        blank=True, default=None, max_length=32, null=True
                    ),
                ),
                (
                    "state",
                    models.CharField(
                        blank=True,
                        choices=[
                            ("AK", "Alaska"),
                            ("AL", "Alabama"),
                            ("AR", "Arkansas"),
                            ("AZ", "Arizona"),
                            ("CA", "California"),
                            ("CO", "Colorado"),
                            ("CT", "Connecticut"),
                            ("DC", "District of Columbia"),
                            ("DE", "Delaware"),
                            ("FL", "Florida"),
                            ("GA", "Georgia"),
                            ("HI", "Hawaii"),
                            ("IA", "Iowa"),
                            ("ID", "Idaho"),
                            ("IL", "Illinois"),
                            ("IN", "Indiana"),
                            ("KS", "Kansas"),
                            ("KY", "Kentucky"),
                            ("LA", "Louisiana"),
                            ("MA", "Massachusetts"),
                            ("MD", "Maryland"),
                            ("ME", "Maine"),
                            ("MI", "Michigan"),
                            ("MN", "Minnesota"),
                            ("MO", "Missouri"),
                            ("MS", "Mississippi"),
                            ("MT", "Montana"),
                            ("NC", "North Carolina"),
                            ("ND", "North Dakota"),
                            ("NE", "Nebraska"),
                            ("NH", "New Hampshire"),
                            ("NJ", "New Jersey"),
                            ("NM", "New Mexico"),
                            ("NV", "Nevada"),
                            ("NY", "New York"),
                            ("OH", "Ohio"),
                            ("OK", "Oklahoma"),
                            ("OR", "Oregon"),
                            ("PA", "Pennsylvania"),
                            ("RI", "Rhode Island"),
                            ("SC", "South Carolina"),
                            ("SD", "South Dakota"),
                            ("TN", "Tennessee"),
                            ("TX", "Texas"),
                            ("UT", "Utah"),
                            ("VA", "Virginia"),
                            ("VT", "Vermont"),
                            ("WA", "Washington"),
                            ("WI", "Wisconsin"),
                            ("WV", "West Virginia"),
                            ("WY", "Wyoming"),
                        ],
                        default=None,
                        max_length=2,
                        null=True,
                    ),
                ),
                (
                    "zip_code",
                    models.CharField(
                        blank=True, default=None, max_length=16, null=True
                    ),
                ),
                (
                    "type_of_animals",
                    django.contrib.postgres.fields.ArrayField(
                        base_field=models.CharField(max_length=32),
                        blank=True,
                        default=[],
                        size=None,
                    ),
                ),
                (
                    "user",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]