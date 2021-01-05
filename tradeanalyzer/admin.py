from django.contrib import admin
from django.conf    import settings
from .models.dbsetting import DbSetting
import os

# Register your models here.
#class ChoiceInline(admin.StackedInline):
class ChoiceInline(admin.TabularInline):
    extra = 5

class DbSettingAdmin(admin.ModelAdmin):
    list_display = ('dbserver', 'dbport', 'dbuser', 'dbpassword', 'dbname')

    fieldsets = [
        ('dbserver',   {'fields':['dbserver']}),
        ('dbport',     {'fields':['dbport']}),
        ('dbuser',     {'fields':['dbuser']}),
        ('dbpassword', {'fields':['dbpassword']}),
        ('dbname',     {'fields':['dbname']})
    ]
    #inlines = [ChoiceInline]

    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request, obj=None):
        return False

admin.site.register(DbSetting, DbSettingAdmin)

