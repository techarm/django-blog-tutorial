from django.contrib import admin
from .models import Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    """記事の管理画面設定"""

    list_display = ["title", "is_featured", "is_published", "updated_at"]
    list_filter = ["is_published", "is_featured", "created_at"]
    search_fields = ["title", "content"]
    date_hierarchy = "created_at"
    ordering = ["-created_at"]
