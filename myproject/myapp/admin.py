from django.contrib import admin
from myapp.models import Forms
# Register your models here.

class FormsAdmin(admin.ModelAdmin):
    list_display = ('name','regno','email','year','phone',)

admin.site.register(Forms,FormsAdmin)