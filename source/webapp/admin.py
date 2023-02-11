from django.contrib import admin
from webapp.models import Ad, Category


# Register your models here.

class AdAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'created_at']
    list_display_links = ['title']
    search_fields = ['title', 'content']


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']


admin.site.register(Ad, AdAdmin)
admin.site.register(Category, CategoryAdmin)

