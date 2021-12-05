from django.contrib import admin
from .models import *
# Register your models here.
ob_list = [Intro, Coding_skils,
           Education_experience, Fetured_Work, Certificate]
admin.site.register(ob_list)
