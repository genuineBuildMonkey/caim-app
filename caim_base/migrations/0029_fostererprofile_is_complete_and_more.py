# Generated by Django 4.1 on 2023-02-20 16:01

import caim_base.models.fosterer
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("caim_base", "0028_fostererprofile_agree_share_details_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="fostererprofile",
            name="is_complete",
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name="fostererprofile",
            name="agree_share_details",
            field=models.CharField(
                choices=[("YES", "Yes"), ("NO", "No")],
                default=None,
                max_length=32,
                null=True,
                verbose_name="Do you agree that we can share the details you've provided with rescues in your area?",
            ),
        ),
        migrations.AlterField(
            model_name="fostererprofile",
            name="behavioural_attributes",
            field=caim_base.models.fosterer.ChoiceArrayField(
                base_field=models.CharField(
                    choices=[
                        ("GOOD_WITH_DOGS", "Good with dogs"),
                        ("GOOD_WITH_CATS", "Good with cats"),
                        ("GOOD_WITH_KIDS", "Good with children"),
                        ("NO_MEDICAL_ISSUES", "No medical issues"),
                        ("NO_SPECIAL_NEEDS", "No special needs"),
                        ("NO_BEHAVIOURAL_NEEDS", "No behavioral issues"),
                    ],
                    max_length=32,
                ),
                blank=True,
                default=None,
                null=True,
                size=None,
                verbose_name="Please check any of the requirements you have for a foster",
            ),
        ),
        migrations.AlterField(
            model_name="fostererprofile",
            name="category_of_animals",
            field=caim_base.models.fosterer.ChoiceArrayField(
                base_field=models.CharField(
                    choices=[
                        ("ADULT_FEMALE", "Adult female"),
                        ("ADULT_MALE", "Adult male"),
                        ("PREGNANT_MOTHER", "Pregnant mom"),
                        ("MOTHER_WITH_BABIES", "Mom with nursing babies"),
                        ("BABIES", "Puppies / kittens"),
                        ("PIT_BULLY_BREEDS", "Pit and/or Bully breeds"),
                    ],
                    max_length=32,
                ),
                blank=True,
                default=None,
                null=True,
                size=None,
                verbose_name="Please check any / all that you're interested in fostering?",
            ),
        ),
        migrations.AlterField(
            model_name="fostererprofile",
            name="ever_been_convicted_abuse",
            field=models.CharField(
                choices=[("YES", "Yes"), ("NO", "No")],
                default=None,
                max_length=32,
                null=True,
                verbose_name="Have you or a family / household member ever been convicted of an animal related crime (animal abuse, neglect, abandonment, etc.)?",
            ),
        ),
        migrations.AlterField(
            model_name="fostererprofile",
            name="existing_pets_details",
            field=models.TextField(
                blank=True,
                default=None,
                null=True,
                verbose_name="Please give details of your existing pets",
            ),
        ),
        migrations.AlterField(
            model_name="fostererprofile",
            name="experience_categories",
            field=caim_base.models.fosterer.ChoiceArrayField(
                base_field=models.CharField(
                    choices=[
                        ("YES", "House / potty training"),
                        ("CRATE", "Crate training"),
                        ("LEASH_WALKING", "Challenges with leash / walking"),
                        ("JUMPING", "Jumping"),
                        ("HIGH_ENERGY", "High energy"),
                        ("OBEDIENCE", "Basic obedience"),
                        ("PUPPIES", "Training puppies"),
                        ("SEPARATION_ANXIETY", "Separation anxiety"),
                        ("FEARS", "Fears / phobias"),
                        ("REACTIVITY", "Reactivity"),
                        ("FOOD_GUARDING", "Food guarding"),
                        ("MEDICAL_ISSUES", "Medical issues"),
                        ("GERIATRIC", "Geriatric concerns"),
                        ("NONE_OF_ABOVE", "None of the above"),
                    ],
                    max_length=32,
                ),
                blank=True,
                default=None,
                null=True,
                size=None,
                verbose_name="Do you have experience with any of the following? Check all that apply.",
            ),
        ),
        migrations.AlterField(
            model_name="fostererprofile",
            name="experience_description",
            field=models.TextField(
                blank=True,
                default=None,
                null=True,
                verbose_name="Please describe your experience with animals (personal pets, training, interactions, etc.)",
            ),
        ),
        migrations.AlterField(
            model_name="fostererprofile",
            name="experience_given_up_pet",
            field=models.TextField(
                blank=True,
                default=None,
                null=True,
                verbose_name="Have you ever given a pet up? If so, please describe the situation.",
            ),
        ),
        migrations.AlterField(
            model_name="fostererprofile",
            name="hours_alone_description",
            field=models.TextField(
                blank=True,
                default=None,
                null=True,
                verbose_name="How many hours / day will your foster animal be left alone?",
            ),
        ),
        migrations.AlterField(
            model_name="fostererprofile",
            name="hours_alone_location",
            field=models.TextField(
                blank=True,
                default=None,
                null=True,
                verbose_name="Where will your foster animal be when they're left alone?",
            ),
        ),
        migrations.AlterField(
            model_name="fostererprofile",
            name="num_existing_pets",
            field=models.IntegerField(
                blank=True,
                default=None,
                null=True,
                verbose_name="How many pets do you currently have in your home?",
            ),
        ),
        migrations.AlterField(
            model_name="fostererprofile",
            name="other_info",
            field=models.TextField(
                blank=True,
                default=None,
                null=True,
                verbose_name="Is there anything else you want us / rescues to know?",
            ),
        ),
        migrations.AlterField(
            model_name="fostererprofile",
            name="people_at_home",
            field=models.TextField(
                blank=True,
                default=None,
                null=True,
                verbose_name="Please list how many people live in your home and their ages",
            ),
        ),
        migrations.AlterField(
            model_name="fostererprofile",
            name="reference_1",
            field=models.TextField(
                blank=True, default=None, null=True, verbose_name="Reference #1"
            ),
        ),
        migrations.AlterField(
            model_name="fostererprofile",
            name="reference_2",
            field=models.TextField(
                blank=True, default=None, null=True, verbose_name="Reference #2"
            ),
        ),
        migrations.AlterField(
            model_name="fostererprofile",
            name="reference_3",
            field=models.TextField(
                blank=True, default=None, null=True, verbose_name="Reference #3"
            ),
        ),
        migrations.AlterField(
            model_name="fostererprofile",
            name="rent_ok_foster_pets",
            field=models.CharField(
                choices=[("YES", "Yes"), ("NO", "No")],
                default=None,
                max_length=32,
                null=True,
                verbose_name="If you rent, is your landlord ok with you having foster pets?",
            ),
        ),
        migrations.AlterField(
            model_name="fostererprofile",
            name="rent_own",
            field=models.CharField(
                choices=[("RENT", "Rent"), ("OWN", "Own")],
                default=None,
                max_length=32,
                null=True,
                verbose_name="Do you rent or own?",
            ),
        ),
        migrations.AlterField(
            model_name="fostererprofile",
            name="rent_restrictions",
            field=models.TextField(
                blank=True,
                default=None,
                null=True,
                verbose_name="If you rent, please describe any pet restrictions that are in place.",
            ),
        ),
        migrations.AlterField(
            model_name="fostererprofile",
            name="sleep_location",
            field=models.TextField(
                blank=True,
                default=None,
                null=True,
                verbose_name="Where will your foster animal sleep?",
            ),
        ),
        migrations.AlterField(
            model_name="fostererprofile",
            name="timeframe",
            field=models.CharField(
                choices=[
                    ("MAX_2_WEEKS", "Up to 2 weeks"),
                    ("MAX_3_MONTHS", "Up to 3 months"),
                    ("ANY_DURATION", "Any duration"),
                    ("OTHER", "Other (please specify)"),
                ],
                default=None,
                max_length=32,
                null=True,
                verbose_name="Please let us know which timeframe you're available for fostering",
            ),
        ),
        migrations.AlterField(
            model_name="fostererprofile",
            name="timeframe_other",
            field=models.TextField(
                blank=True,
                default=None,
                null=True,
                verbose_name="If 'other', please give details",
            ),
        ),
        migrations.AlterField(
            model_name="fostererprofile",
            name="type_of_animals",
            field=caim_base.models.fosterer.ChoiceArrayField(
                base_field=models.CharField(
                    choices=[("DOGS", "Dogs"), ("CATS", "Cats")], max_length=32
                ),
                blank=True,
                default=None,
                null=True,
                size=None,
                verbose_name="Which type of animal(s) are you wanting to foster?",
            ),
        ),
        migrations.AlterField(
            model_name="fostererprofile",
            name="yard_fence_over_5ft",
            field=models.CharField(
                choices=[("YES", "Yes"), ("NO", "No")],
                default=None,
                max_length=32,
                null=True,
                verbose_name="If your yard is fully fenced, is it all over 5 feet tall?",
            ),
        ),
        migrations.AlterField(
            model_name="fostererprofile",
            name="yard_type",
            field=models.CharField(
                choices=[
                    ("NO_YARD", "No yard"),
                    ("UNFENCED", "Unfenced yard"),
                    ("PARTIALLY_FENCED", "Partially fenced yard"),
                    ("FULLY_FENCED", "Fully fenced yard"),
                ],
                default=None,
                max_length=32,
                null=True,
                verbose_name="Describe your yard",
            ),
        ),
    ]
