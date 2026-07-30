from django.contrib import admin

# Register your models here.
from .models import Project,Contact, Profile

@admin.register(Project)

class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'featured','created_at')

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ("name","email","created_at","is_read")
    list_editable = ("is_read",)

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ("name",)


