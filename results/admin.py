from django.contrib import admin
from .models import Test

# Change the default admin site title
admin.site.site_header = "Smoke Test Experiments V2"

@admin.action(description='Mark selected stories as published')
def make_published(modeladmin, request, queryset):
    queryset.update(status='p')


# Register your models here.
# Show all field in admin page
class TestAdmin(admin.ModelAdmin):
    list_display = ('name', 'passTest', 'criterial', 'test', 'logs', 'idTest')
    list_filter = ('passTest', 'criterial', 'test', 'logs', 'idTest')
    search_fields = ('name', 'passTest', 'criterial', 'test', 'logs', 'idTest')
    ordering = ('name', 'passTest', 'criterial', 'test', 'logs', 'idTest')
    filter_horizontal = ()
    list_per_page = 25

    actions = [make_published]


# Create Admin configuration for django model. Import model and register it.
admin.site.register(Test, TestAdmin)

