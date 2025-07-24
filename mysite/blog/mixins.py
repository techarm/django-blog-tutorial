from django.db.models import Count
from django.db.models.functions import TruncMonth
from .models import Category, Post


class CategoryListMixin:
    """カテゴリ一覧を自動的に追加するMixin"""

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # すべてのビューにカテゴリ一覧を追加
        context["categories"] = Category.objects.all().order_by("name")
        return context


class ArchiveListMixin:
    """アーカイブ一覧を自動的に追加するMixin"""

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # 月別アーカイブを追加
        context["archives"] = (
            Post.objects.filter(is_published=True)
            .annotate(month=TruncMonth("created_at"))
            .values("month")
            .annotate(count=Count("id"))
            .order_by("-month")[:12]
        )

        return context


class SidebarMixin(CategoryListMixin, ArchiveListMixin):
    """サイドバー用のデータをまとめたMixin"""

    # CategoryListMixinとArchiveListMixinの機能を合体！
    pass
