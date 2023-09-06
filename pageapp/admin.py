from django.contrib import admin
from .models import postclass,imageupload,User
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin


# useradmin-------------------------



class UserAdmin(BaseUserAdmin):

    list_display = ["id","email", "name", "is_admin"]
    list_filter = ["is_admin"]
    fieldsets = [
        (None, {"fields": ["email", "password"]}),
        ("Personal info", {"fields": ["name"]}),
        ("Permissions", {"fields": ["is_admin"]}),
    ]
  
    add_fieldsets = [
        (
            None,
            {
                "classes": ["wide"],
                "fields": ["email", "name", "password", "password2"],
            },
        ),
    ]
    search_fields = ["email"]
    ordering = ["email","id"]
    filter_horizontal = []
    
admin.site.register(User, UserAdmin)

#-------------------------------------------------------------------------------------------------------------------------
# Register your models here.
@admin.register(postclass)
class postclassadmin(admin.ModelAdmin):
    list_display = ('id','name', 'course','date','fileup','sign')
    
@admin.register(imageupload)
class imageuploadadmin(admin.ModelAdmin):
    list_display = ('id','file')

