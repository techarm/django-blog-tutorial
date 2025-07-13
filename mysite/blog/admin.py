from django.contrib import admin
from .models import Post, Category


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ["name", "slug", "created_at"]
    prepopulated_fields = {"slug": ("name",)}


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ["title", "is_featured", "is_published", "category", "updated_at"]
    list_filter = ["is_published", "is_featured", "created_at"]
    search_fields = ["title", "content"]
    date_hierarchy = "created_at"
    ordering = ["-created_at"]
