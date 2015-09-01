from django.contrib import admin

# Register your models here.
from .models import Search

class SearchAdmin(admin.ModelAdmin):
    list_display = ["__unicode__", "searching_text", "timestamp"]

    class Meta:
        model = Search

admin.site.register(Search, SearchAdmin)
