from django.contrib.auth import get_user_model
from django.db import models
from django.contrib.gis.db.models import PointField
from django.contrib.auth.models import AbstractUser
from django.utils.safestring import mark_safe
from phonenumber_field.modelfields import PhoneNumberField
from .templatetags.caim_helpers import image_resize


User = get_user_model()
# Change default User model so email is unique and main identifier
User._meta.get_field("email")._unique = True
User.USERNAME_FIELD = "email"
User.REQUIRED_FIELDS = ["username"]


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    description = models.TextField(blank=True)


class ZipCode(models.Model):
    zip_code = models.CharField(max_length=16, unique=True)
    geo_location = PointField()


class Awg(models.Model):
    class AwgType(models.TextChoices):
        CENTER_ONLY = "CENTER_ONLY", "Center only"
        FOSTER_ONLY = "FOSTER_ONLY", "Foster only"
        CENTER_AND_FOSTER = "CENTER_AND_FOSTER", "Both"

    name = models.CharField(max_length=100)
    petfinder_id = models.CharField(max_length=32, blank=True, null=True, default=None)

    description = models.TextField(blank=True)
    awg_type = models.CharField(
        max_length=32,
        choices=AwgType.choices,
        default=None,
        blank=True,
        null=True,
    )

    has_501c3_tax_exemption = models.BooleanField(default=False)
    company_ein = models.CharField(max_length=16, blank=True, null=True, default=None)

    workwith_dogs = models.BooleanField(default=False)
    workwith_cats = models.BooleanField(default=False)
    workwith_other = models.BooleanField(default=False)

    geo_location = PointField()
    zip_code = models.CharField(max_length=16, blank=True, null=True, default=None)
    city = models.CharField(max_length=32, blank=True, null=True, default=None)
    state = models.CharField(max_length=2)
    email = models.EmailField(max_length=32, blank=True, null=True, default=None)
    phone = PhoneNumberField(blank=True, null=True, default=None)
    website_url = models.URLField(max_length=255, blank=True, null=True, default=None)
    facebook_url = models.URLField(max_length=255, blank=True, null=True, default=None)
    instagram_url = models.URLField(max_length=255, blank=True, null=True, default=None)
    twitter_url = models.URLField(max_length=255, blank=True, null=True, default=None)
    tiktok_url = models.URLField(max_length=255, blank=True, null=True, default=None)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class AnimalType(models.TextChoices):
    DOG = "DOG", "Dog"
    CAT = "CAT", "Cat"


class Breed(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    animal_type = models.CharField(
        max_length=3,
        choices=AnimalType.choices,
        default=AnimalType.DOG,
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name} ({self.animal_type})"


class Animal(models.Model):
    class AnimalSex(models.TextChoices):
        F = "F", "Female"
        M = "M", "Male"

    class AnimalSize(models.TextChoices):
        XS = "XS", "X-Small"
        S = "S", "Small"
        M = "M", "Medium"
        L = "L", "Large"
        XL = "XL", "X-Large"

    class AnimalAge(models.TextChoices):
        BABY = "BABY", "Puppy/Kitten"
        YOUNG = "YOUNG", "Young"
        ADULT = "ADULT", "Adult"
        SENIOR = "SENIOR", "Senior"

    class AnimalBehaviourGrade(models.TextChoices):
        POOR = "POOR", "Poor"
        SELECTIVE = "SELECTIVE", "Selective"
        GOOD = "GOOD", "Good"
        NOT_TESTED = "NOT_TESTED", "Not tested"

    name = models.CharField(max_length=100)
    animal_type = models.CharField(
        max_length=3,
        choices=AnimalType.choices,
        default=AnimalType.DOG,
    )
    petfinder_id = models.CharField(
        max_length=32, blank=True, null=True, default=None, unique=True
    )
    awg = models.ForeignKey(Awg, on_delete=models.CASCADE)
    primary_breed = models.ForeignKey(
        Breed, on_delete=models.RESTRICT, related_name="primary_animal_set"
    )
    secondary_breed = models.ForeignKey(
        Breed,
        on_delete=models.RESTRICT,
        related_name="secondary_animal_set",
        blank=True,
        null=True,
        default=None,
    )
    is_mixed_breed = models.BooleanField()
    is_unknown_breed = models.BooleanField()
    sex = models.CharField(
        max_length=1,
        choices=AnimalSex.choices,
    )
    size = models.CharField(
        max_length=2,
        choices=AnimalSize.choices,
    )
    age = models.CharField(
        max_length=8,
        choices=AnimalAge.choices,
    )
    is_spayed_neutered = models.BooleanField()
    is_vaccinations_current = models.BooleanField()
    is_house_trained = models.BooleanField()
    special_needs = models.TextField(blank=True)
    vaccinations_notes = models.TextField(blank=True)
    description = models.TextField(blank=True)
    behaviour_dogs = models.CharField(
        max_length=10,
        choices=AnimalBehaviourGrade.choices,
        default=AnimalBehaviourGrade.NOT_TESTED,
    )
    behaviour_cats = models.CharField(
        max_length=10,
        choices=AnimalBehaviourGrade.choices,
        default=AnimalBehaviourGrade.NOT_TESTED,
    )
    behaviour_kids = models.CharField(
        max_length=10,
        choices=AnimalBehaviourGrade.choices,
        default=AnimalBehaviourGrade.NOT_TESTED,
    )
    is_euth_listed = models.BooleanField()
    euth_date = models.DateField(blank=True, null=True, default=None)
    primary_photo = models.ImageField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    def breedsText(self):
        if self.is_unknown_breed:
            return "Unknown breed"
        text = self.primary_breed.name
        if self.secondary_breed and self.secondary_breed != self.primary_breed:
            text = f"{self.primary_breed.name} / {self.secondary_breed.name}"
        if self.is_mixed_breed:
            text = f"{text} mix"
        return text

    def sexText(self):
        return Animal.AnimalSex[self.sex].label

    def ageText(self):
        return Animal.AnimalAge[self.age].label

    def sizeText(self):
        return Animal.AnimalSize[self.size].label

    def get_absolute_url(self):
        return f"/animal/{self.id}"

    def admin_image_tag(self):
        if self.primary_photo:
            resized_url = image_resize(self.primary_photo.url, "45x45")
            return mark_safe(
                '<img src="%s" style="max-width: 45px; max-height:45px;" />'
                % resized_url
            )
        else:
            return "No Photo"

    admin_image_tag.short_description = "Image"


class AnimalImage(models.Model):
    animal = models.ForeignKey(Animal, on_delete=models.CASCADE)
    photo = models.ImageField(blank=False)
    created_at = models.DateTimeField(auto_now_add=True)


class AnimalShortList(models.Model):
    animal = models.ForeignKey(Animal, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = (("animal", "user"),)


class AnimalComment(models.Model):
    animal = models.ForeignKey(Animal, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    edited_at = models.DateTimeField(blank=True, null=True)

    def can_be_deleted_by(self, user):
        return self.can_be_edited_by(user)

    def can_be_edited_by(self, user):
        return self.user == user or user.is_staff