from time import sleep

from django.db import models
from django.forms import CharField
from django.core.validators import ValidationError, MaxValueValidator, MinValueValidator, FileExtensionValidator
from django.contrib.auth.models import User


class Category(models.Model):

    direction = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.direction

class Vacancies(models.Model):

    title = models.CharField(max_length=100)
    requirements = models.TextField(max_length=200)
    knowledge = models.TextField(max_length=200)
    known_languages = models.TextField(max_length=200)
    skills = models.TextField(max_length=200)
    company_image = models.ImageField(upload_to='images/', blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    work_of_experience = models.TextField(max_length=100)
    contacts = models.TextField(max_length=100)
    company_video = models.FileField(null=True, blank=True, validators=[FileExtensionValidator('mov, avi')])
    location = models.CharField(max_length=100, blank=True, null=True)
    salary = models.IntegerField(validators=[MinValueValidator(0)])
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.TimeField(auto_now=True)


    def __str__(self):
        return self.title

    # def clean(self):
    #     errors = {}
    #
    #     if self.salary <= 0:
    #         errors['salary'] = 'salary must be greater than 0'
    #
    #     if (not self.contacts[0] == "+" and not self.contacts[1::12].isdigit()
    #             or self.contacts[0] == "@"):
    #         errors['contacts'] = 'please enter yor contacts correctly'
    #
    #     if errors:
    #         raise ValidationError(errors)

class Comment(models.Model):
    comment = models.TextField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)
    vacancy = models.ForeignKey(Vacancies, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

    # def __str__(self):
    #     return self.comment

class FavoriteJobs(models.Model):
    job = models.ForeignKey(Vacancies, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.user}, {self.job}'

    










