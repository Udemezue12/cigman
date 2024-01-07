from django.db import models
# from django.contrib import admin


from django.contrib.auth.models import User
from django.forms import ImageField

from .validators import validate_file_size


class Profile(models.Model):
    MALE = 1
    FEMALE = 2
    OTHER = 3

    GENDER_CHOICES = [
        (MALE, 'Male'),
        (FEMALE, 'Female'),
        (OTHER, 'Other'),
    ]

    gender = models.IntegerField(choices=GENDER_CHOICES)
    first_name = models.CharField(max_length=255, null=False)
    last_name = models.CharField(max_length=255, blank=True, null=False)
    phone = models.CharField(max_length=255)
    birth_date = models.DateField(null=False, blank=True)
    author = models.ForeignKey(
        'Author', on_delete=models.PROTECT, related_name="author_profile")

    # skill = models.ForeignKey(
    #     'Skill', on_delete=models.PROTECT, related_name='profile_skills')
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    bio = models.TextField(blank=True)

    image = models.ImageField(
        upload_to='portfolio/images',
        validators=[validate_file_size], default='default_image.jpg', blank=False)

    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name}"

    


class Skill(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)

    profile = models.ForeignKey(
        # Foreign key to Profile
        Profile, on_delete=models.CASCADE,  related_name='related_skills')

    def __str__(self) -> str:
        return self.name


class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    # project_url = models.URLField(verbose_name="Project URL")
    author = models.ForeignKey("Author", on_delete=models.CASCADE)
    skills = models.ManyToManyField("Skill")

    profile = models.ForeignKey(
        Profile, on_delete=models.CASCADE)  # Foreign key to Profile

    def __str__(self) -> str:
        return self.title


class Certification(models.Model):
    name = models.CharField(max_length=100)
    issuing_organization = models.CharField(max_length=200)

    date_issued = models.DateField(null=False, blank=False)
    # credential_id = models.URLField(verbose_name="Credential ID")

    profile = models.ForeignKey(
        Profile, on_delete=models.CASCADE)  # Foreign key to Profile

    def __str__(self) -> str:
        return self.name


class Author(models.Model):
    MEMBERSHIP_BRONZE = 'B'
    MEMBERSHIP_SILVER = 'S'
    MEMBERSHIP_GOLD = 'G'

    MEMBERSHIP_CHOICES = [
        (MEMBERSHIP_BRONZE, 'Bronze'),
        (MEMBERSHIP_SILVER, 'Silver'),
        (MEMBERSHIP_GOLD, 'Gold'),
    ]

    MALE = 'M'
    FEMALE = 'F'
    OTHER = 'O'

    GENDER_CHOICES = [
        (MALE, 'Male'),
        (FEMALE, 'Female'),
        (OTHER, 'Other'),
    ]

    gender = models.CharField(
        max_length=1, choices=GENDER_CHOICES, default=MALE)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    github_username = models.CharField(max_length=255)
    twitter_username = models.CharField(max_length=255)

    phone = models.CharField(max_length=255)
    birth_date = models.DateField(null=False, blank=False)

    membership = models.CharField(
        max_length=1, choices=MEMBERSHIP_CHOICES, default=MEMBERSHIP_BRONZE)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Award(models.Model):
    title = models.CharField(max_length=200)
    organization = models.CharField(max_length=200)
    description = models.TextField()
    year_awarded = models.IntegerField()

    author = models.ForeignKey(Author, on_delete=models.PROTECT)

    profile = models.ForeignKey(
        Profile, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f"{self.title} {self.description}"


class Publication(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()

    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    profile = models.ForeignKey(
        Profile, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f"{self.title} {self.description}"


class Experience(models.Model):
    title = models.CharField(max_length=200)
    company = models.CharField(max_length=200)
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    current_job = models.BooleanField(default=False)
    description = models.TextField()
    profile = models.ForeignKey(
        Profile, on_delete=models.CASCADE)
    
    def __str__(self) -> str:
        return f"{self.title} {self.description}"


class ProfileImage(models.Model):

    def default_image():
        with open('media/store/images', 'rb') as f:
            return ImageField(f)

    profile = models.ForeignKey(
        Profile, on_delete=models.CASCADE, related_name='images')


class Education(models.Model):
    degree = models.CharField(max_length=200)
    institution = models.CharField(max_length=200)
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    description = models.TextField()
    education_type = models.CharField(max_length=15)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f"{self.degree} {self.description}"
