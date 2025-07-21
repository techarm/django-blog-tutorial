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


class Tag(models.Model):
    """タグモデル"""

    name = models.CharField(max_length=30, unique=True, verbose_name="タグ名")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="作成日時")

    class Meta:
        verbose_name = "タグ"
        verbose_name_plural = "タグ"
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
    tags = models.ManyToManyField(
        Tag, related_name="posts", verbose_name="タグ", blank=True
    )
    created_at = models.DateTimeField(default=timezone.now, verbose_name="作成日時")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="更新日時")

    class Meta:
        verbose_name = "記事"
        verbose_name_plural = "記事"
        ordering = ["-created_at"]  # 新しい記事から順に並べる

    def __str__(self):
        return self.title


class Comment(models.Model):
    """コメントモデル"""

    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name="comments", verbose_name="記事"
    )
    name = models.CharField(max_length=50, verbose_name="名前")
    email = models.EmailField(verbose_name="メールアドレス")
    content = models.TextField(verbose_name="コメント内容")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="投稿日時")
    is_approved = models.BooleanField(default=True, verbose_name="承認済み")

    class Meta:
        verbose_name = "コメント"
        verbose_name_plural = "コメント"
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.name}: {self.content[:20]}"
