from django.contrib import admin

from blog.models import Note


@admin.register(Note)
class NoteAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "heading",
        "created_at",
        "is_published",
        "views",
        "updated_at",
    )
    list_filter = (
        "views",
        "is_published",
    )
    search_fields = ("heading", "content")
    ordering = ("-is_published", "-views", "-updated_at")
