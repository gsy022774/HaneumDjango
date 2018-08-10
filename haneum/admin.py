from django.contrib import admin

# Register your models here.
from .models import Company, Report

admin.site.register(Company)
admin.site.register(Report)