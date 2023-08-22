from django.contrib import admin

from apps.blogs.models import Blog


# Register your models here.
@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    model = Blog
    list_display = [
        "title",
        "created_at",
    ]
