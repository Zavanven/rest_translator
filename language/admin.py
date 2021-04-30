from django.contrib import admin
from .models import Language

# Register your models here.
class LanguageAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'shop')
    list_display_links = ('id', 'title', 'shop')

admin.site.register(Language, LanguageAdmin)