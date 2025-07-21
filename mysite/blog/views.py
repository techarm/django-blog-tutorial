from django.shortcuts import render, get_object_or_404
from django.db.models import Q
from django.core.paginator import Paginator

from blog.forms import PostSearchForm
from .models import Post, Category


def post_list(request):
    """記事一覧を表示"""

    # 公開されている記事のみ取得
    posts = Post.objects.filter(is_published=True).order_by("-created_at")

    # 注目記事を取得
    featured_posts = Post.objects.filter(is_published=True, is_featured=True).order_by(
        "-created_at"
    )[:2]

    # カテゴリー一覧を取得
    categories = Category.objects.all().order_by("name")

    context = {
        "posts": posts,
        "featured_posts": featured_posts,
        "total_posts": posts.count(),
        "categories": categories,  # カテゴリーを追加
    }
    return render(request, "blog/post_list.html", context)


def post_detail(request, post_id):
    """記事詳細を表示"""

    # 指定されたIDの記事を取得（なければ404エラー）
    post = get_object_or_404(Post, id=post_id, is_published=True)

    # サイドバー用に最新記事を取得
    recent_posts = (
        Post.objects.filter(is_published=True)
        .exclude(id=post_id)
        .order_by("-created_at")[:5]
    )

    # カテゴリー一覧を取得
    categories = Category.objects.all().order_by("name")

    context = {
        "post": post,
        "posts": recent_posts,  # サイドバー用
        "categories": categories,  # カテゴリーを追加
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

    context = {
        "category": category,
        "posts": posts,
        "categories": categories,
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
