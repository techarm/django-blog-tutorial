from django.contrib import admin
from markdownx.admin import MarkdownxModelAdmin
from .models import Post, Category, Tag


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ["name", "slug", "created_at"]
    prepopulated_fields = {"slug": ("name",)}


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ["name", "created_at"]
    search_fields = ["name"]


@admin.register(Post)
class PostAdmin(MarkdownxModelAdmin):
    """記事の管理画面"""

    list_display = [
        "title",
        "category",
        "author",
        "is_published",
        "is_featured",
        "created_at",
    ]
    list_filter = ["is_published", "is_featured", "category", "author", "created_at"]
    search_fields = ["title", "content", "author__username"]
    ordering = ["-created_at"]
    date_hierarchy = "created_at"

    fieldsets = [
        ("基本情報", {"fields": ["title", "content", "author"]}),
        ("分類", {"fields": ["category", "tags"]}),
        ("オプション", {"fields": ["is_published", "is_featured"]}),
    ]

    def save_model(self, request, obj, form, change):
        if not change:  # 新規作成時
            obj.author = request.user
        super().save_model(request, obj, form, change)
