from django.contrib import admin
from .models import User
# Register your models here.

class AdminConfig(admin.ModelAdmin):
    exclude = ('password',)
    list_display = ('username', 'date_joined', 'is_staff', 'is_superuser')

admin.site.register(User, AdminConfig)