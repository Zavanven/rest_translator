from django.contrib import admin
from .models import Translation

# Register your models here.
class TranslationAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'product', 'language')
    list_display_links = ('id', 'title', 'product', 'language')
    list_filter = ('language', )

admin.site.register(Translation, TranslationAdmin)
