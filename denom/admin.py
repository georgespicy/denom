from django.contrib import admin
from .models import Subcriber, Contact
# Register your models here.

@admin.register(Subcriber)
class SubcribeAdmin(admin.ModelAdmin):
    pass

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    pass