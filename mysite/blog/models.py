from django.db import models
from django.utils import timezone


class Category(models.Model):
    """カテゴリーモデル"""

    name = models.CharField(max_length=50, unique=True, verbose_name="カテゴリー名")
    slug = models.SlugField(unique=True, verbose_name="スラッグ")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="作成日時")

    class Meta:
        verbose_name = "カテゴリー"
        verbose_name_plural = "カテゴリー"
        ordering = ["name"]

    def __str__(self):
        return self.name


class Post(models.Model):
    """ブログ記事のモデル"""

    title = models.CharField(max_length=200, verbose_name="タイトル")
    content = models.TextField(verbose_name="本文")
    is_featured = models.BooleanField(default=False, verbose_name="注目記事")
    is_published = models.BooleanField(default=False, verbose_name="公開状態")
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        related_name="posts",
        verbose_name="カテゴリー",
        null=True,
        blank=True,
    )
    created_at = models.DateTimeField(default=timezone.now, verbose_name="作成日時")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="更新日時")

    class Meta:
        verbose_name = "記事"
        verbose_name_plural = "記事"
        ordering = ["-created_at"]  # 新しい記事から順に並べる

    def __str__(self):
        return self.title
