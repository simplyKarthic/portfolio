from django.db import models
from django.db.models.fields import BooleanField


class Intro(models.Model):
    Intro_hi = models.TextField(null=True)
    Intro_descrption = models.TextField(null=True)
    Intro_img = models.ImageField(upload_to='pics', null=True)
    Intro_resume = models.FileField(upload_to='resume', null=True)


class Coding_skils(models.Model):
    skills = models.TextField(null=True)
    skills_per = models.IntegerField(null=True)


class Education_experience(models.Model):
    E_name = models.TextField(null=True)
    E_year = models.IntegerField(null=True)
    E_course = models.TextField(null=True)
    E_acquired = models.TextField(null=True)


class Fetured_Work(models.Model):
    F_image = models.ImageField(upload_to='pics', null=True)
    F_name = models.TextField(null=True)
    F_year = models.IntegerField(null=True)
    F_tech = models.TextField(null=True)
    F_description = models.TextField(null=True)


class Certificate(models.Model):
    Certificate_image = models.ImageField(upload_to='pics', null=True)
    Certificate_title = models.TextField(null=True)
    Certificate_description = models.TextField(null=True)


class Blog:
    title = str
    des = str
    dat = str
