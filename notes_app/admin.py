from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

from .models import Document, Folder

admin.site.register(Document)
admin.site.register(Folder)

class CustomUserAdmin(UserAdmin):
    list_display = ('username', 'email', 'first_name', 'last_name', 'password')

admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)
