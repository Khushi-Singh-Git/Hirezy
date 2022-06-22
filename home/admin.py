from django.contrib import admin

# Register your models here.
from . import models
# Register your models here.

admin.site.register(models.Job)

admin.site.register(models.JobApplication)

admin.site.register(models.Questions)

