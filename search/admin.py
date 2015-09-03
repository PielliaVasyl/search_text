from django.contrib import admin
from .models import Search, TextSegment


class SearchAdmin(admin.ModelAdmin):
    list_display = ["__unicode__", "searching_text", "timestamp"]

    class Meta:
        model = Search


class TextSegmentAdmin(admin.ModelAdmin):
    list_display = ["__unicode__", "book", "chapter", "page"]

    class Meta:
        model = TextSegment

admin.site.register(Search, SearchAdmin)
admin.site.register(TextSegment, TextSegmentAdmin)
