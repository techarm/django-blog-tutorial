from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.db.models import Q, Count
from django.db.models.functions import TruncMonth
from django.core.paginator import Paginator
from django.views.generic import TemplateView, ListView, DetailView

from .models import Post, Category, Comment
from .forms import PostSearchForm, CommentForm
from .mixins import CategoryListMixin, SidebarMixin


def post_list(request):
    """記事一覧を表示"""

    # 公開されている記事のみ取得
    posts = Post.objects.filter(is_published=True).order_by("-created_at")

    # 注目記事を取得
    featured_posts = Post.objects.filter(is_published=True, is_featured=True).order_by(
        "-created_at"
    )[:2]

    # カテゴリー一覧を取得（サイドバー用）
    categories = Category.objects.all().order_by("name")

    # 月別アーカイブを取得（サイドバー用）
    archives = (
        Post.objects.filter(is_published=True)
        .annotate(month=TruncMonth("created_at"))
        .values("month")
        .annotate(count=Count("id"))
        .order_by("-month")[:12]
    )

    context = {
        "posts": posts,
        "featured_posts": featured_posts,
        "total_posts": posts.count(),
        "categories": categories,  # カテゴリーを追加
        "archives": archives,  # 追加
    }
    return render(request, "blog/post_list.html", context)


def post_detail(request, post_id):
    """記事詳細とコメント投稿"""
    post = get_object_or_404(Post, pk=post_id, is_published=True)
    comments = post.comments.filter(is_approved=True)

    # コメントフォームの処理
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            # コメントを保存
            comment = Comment(
                post=post,
                name=form.cleaned_data["name"],
                email=form.cleaned_data["email"],
                content=form.cleaned_data["content"],
            )
            comment.save()

            messages.success(request, "コメントを投稿しました！")
            # PRGパターン（Post-Redirect-Get）でリダイレクト
            return redirect("post_detail", post_id=post.id)
    else:
        form = CommentForm()

    # サイドバー用に最新記事を取得
    recent_posts = (
        Post.objects.filter(is_published=True)
        .exclude(id=post_id)
        .order_by("-created_at")[:5]
    )

    # カテゴリー一覧を取得
    categories = Category.objects.all().order_by("name")

    # 月別アーカイブを取得
    archives = (
        Post.objects.filter(is_published=True)
        .annotate(month=TruncMonth("created_at"))
        .values("month")
        .annotate(count=Count("id"))
        .order_by("-month")[:12]
    )

    context = {
        "post": post,
        "posts": recent_posts,  # サイドバー用
        "categories": categories,  # サイドバー用
        "archives": archives,  # 追加
        "comments": comments,
        "comment_form": form,
        "comment_count": comments.count(),
    }
    return render(request, "blog/post_detail.html", context)


def category_posts(request, slug):
    """カテゴリー別の記事一覧を表示"""

    # スラッグからカテゴリーを取得
    category = get_object_or_404(Category, slug=slug)

    # そのカテゴリーの公開記事を取得
    posts = Post.objects.filter(category=category, is_published=True).order_by(
        "-created_at"
    )

    # すべてのカテゴリー（サイドバー用）
    categories = Category.objects.all().order_by("name")

    # 月別アーカイブを取得（サイドバー用）
    archives = (
        Post.objects.filter(is_published=True)
        .annotate(month=TruncMonth("created_at"))
        .values("month")
        .annotate(count=Count("id"))
        .order_by("-month")[:12]
    )

    context = {
        "category": category,
        "posts": posts,
        "categories": categories,
        "archives": archives,
        "total_posts": posts.count(),
    }
    return render(request, "blog/category_posts.html", context)


def post_search(request):
    """記事検索ビュー"""
    form = PostSearchForm(request.GET or None)
    posts = Post.objects.filter(is_published=True)
    keyword = ""  # 初期値を設定

    if form.is_valid():
        # キーワード検索
        keyword = form.cleaned_data.get("keyword")
        if keyword:
            # Q オブジェクトを使った OR 検索
            posts = posts.filter(
                Q(title__icontains=keyword) | Q(content__icontains=keyword)
            )

        # カテゴリ絞り込み
        category = form.cleaned_data.get("category")
        if category:
            posts = posts.filter(category=category)

        # 並び順
        order_by = form.cleaned_data.get("order_by")
        if order_by:
            posts = posts.order_by(order_by)

    # ページネーション
    paginator = Paginator(posts, 10)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    context = {
        "form": form,
        "page_obj": page_obj,
        "keyword": keyword,
        "result_count": posts.count(),
    }

    return render(request, "blog/post_search.html", context)


class AboutView(TemplateView):
    """Aboutページ"""

    template_name = "blog/about.html"  # 使うテンプレートを指定

    def get_context_data(self, **kwargs):
        # 親クラスのメソッドを呼ぶ（おまじないのようなもの）
        context = super().get_context_data(**kwargs)

        # テンプレートに渡したいデータを追加
        context["title"] = "このブログについて"
        context["author"] = "techarm"
        context["created_year"] = 2025

        return context


class MonthArchiveView(SidebarMixin, ListView):
    """月別アーカイブ"""

    model = Post  # どのモデルを表示するか
    template_name = "blog/archive_month.html"  # 使うテンプレート
    context_object_name = "posts"  # テンプレートで使う変数名
    paginate_by = 10  # 1ページに表示する件数

    def get_queryset(self):
        """表示するデータを取得"""
        # URLから年月を取得
        year = self.kwargs.get("year")
        month = self.kwargs.get("month")

        # 該当月の公開記事を取得
        return Post.objects.filter(
            is_published=True, created_at__year=year, created_at__month=month
        ).order_by("-created_at")

    def get_context_data(self, **kwargs):
        """テンプレートに渡すデータを追加"""
        context = super().get_context_data(**kwargs)

        # 年月の情報を追加
        context["year"] = self.kwargs.get("year")
        context["month"] = self.kwargs.get("month")

        return context


class PostDetailView(SidebarMixin, DetailView):
    """記事詳細とコメント（CBV版）"""

    model = Post
    template_name = "blog/post_detail.html"
    context_object_name = "post"
    pk_url_kwarg = "post_id"  # URLのパラメータ名を指定

    def get_queryset(self):
        """公開記事のみ表示"""
        return super().get_queryset().filter(is_published=True)

    def get_context_data(self, **kwargs):
        """テンプレートに渡すデータを準備"""
        context = super().get_context_data(**kwargs)

        # コメント関連
        comments = self.object.comments.filter(is_approved=True)
        context["comments"] = comments
        context["comment_count"] = comments.count()
        context["comment_form"] = CommentForm()

        # サイドバー用
        context["posts"] = (
            Post.objects.filter(is_published=True)
            .exclude(id=self.object.id)
            .order_by("-created_at")[:5]
        )

        return context

    def post(self, request, *args, **kwargs):
        """コメント投稿の処理"""
        self.object = self.get_object()
        form = CommentForm(request.POST)

        if form.is_valid():
            comment = Comment(
                post=self.object,
                name=form.cleaned_data["name"],
                email=form.cleaned_data["email"],
                content=form.cleaned_data["content"],
            )
            comment.save()

            messages.success(request, "コメントを投稿しました！")
            return redirect("post_detail", post_id=self.object.id)

        # エラーがある場合
        context = self.get_context_data()
        context["comment_form"] = form
        return self.render_to_response(context)


class PostListView(SidebarMixin, ListView):
    """記事一覧（CBV版）"""

    model = Post
    template_name = "blog/post_list.html"
    context_object_name = "posts"
    paginate_by = 10

    def get_queryset(self):
        # 公開記事のみ、新しい順
        return Post.objects.filter(is_published=True).order_by("-created_at")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # 注目記事
        context["featured_posts"] = Post.objects.filter(
            is_published=True, is_featured=True
        ).order_by("-created_at")[:2]

        # 総記事数
        context["total_posts"] = self.get_queryset().count()

        return context
