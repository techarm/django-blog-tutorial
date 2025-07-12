from django.shortcuts import render, get_object_or_404
from .models import Post


def post_list(request):
    """記事一覧を表示"""

    # 公開されている記事のみ取得
    posts = Post.objects.filter(is_published=True).order_by("-created_at")

    # 注目記事を取得
    featured_posts = Post.objects.filter(is_published=True, is_featured=True).order_by(
        "-created_at"
    )[:2]

    context = {
        "posts": posts,
        "featured_posts": featured_posts,
        "total_posts": posts.count(),
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

    context = {
        "post": post,
        "posts": recent_posts,  # サイドバー用
    }
    return render(request, "blog/post_detail.html", context)
