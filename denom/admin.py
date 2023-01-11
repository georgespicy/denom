from django.contrib import admin
from .models import Subcriber
# Register your models here.

@admin.register(Subcriber)
class SubcribeAdmin(admin.ModelAdmin):
    pass