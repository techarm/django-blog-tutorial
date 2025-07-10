from django.shortcuts import render

# 共通の記事データ
POSTS = [
    {
        "id": 1,
        "title": "Djangoを始めました",
        "content": "Djangoの学習を始めました。楽しいです！",
        "created_at": "2025-07-01",
        "category": "Django",
        "tags": ["Python", "Django", "初心者"],
        "is_featured": True,
        "body": """今日からDjangoの学習を始めました。
Pythonは少し触ったことがあったけど、Webフレームワークは初めてです。
最初は難しそうだと思ったけど、チュートリアルが分かりやすくて助かります。
これからブログアプリを作っていきたいと思います！""",
    },
    {
        "id": 2,
        "title": "ビューについて学んだこと",
        "content": "今日はビューについて学びました。MVTパターンの理解が深まりました。",
        "created_at": "2025-07-02",
        "category": "Django",
        "tags": ["Django", "View", "MVT"],
        "is_featured": False,
        "body": """Djangoのビューは、リクエストを受け取ってレスポンスを返す関数です。
MVTパターンのVに当たる部分で、ビジネスロジックを担当します。
テンプレートにデータを渡す方法も学びました。
contextという辞書を使うのが面白いです。""",
    },
    {
        "id": 3,
        "title": "テンプレートは便利",
        "content": "テンプレートを使うとHTMLが書きやすいです。継承システムが特に便利！",
        "created_at": "2025-07-03",
        "category": "Django",
        "tags": ["Django", "Template"],
        "is_featured": True,
        "body": """今日はテンプレートについて学習しました。
変数の表示、forループ、if文など、基本的な機能を試しました。
特に継承システムが素晴らしいです！
共通部分を一箇所にまとめられるのは、とても効率的ですね。""",
    },
]


def post_list(request):
    # 注目記事を抽出
    featured_posts = [p for p in POSTS if p.get("is_featured", False)]

    context = {
        "posts": POSTS,
        "featured_posts": featured_posts,
        "total_posts": len(POSTS),
    }
    return render(request, "blog/post_list.html", context)


def post_detail(request, post_id):
    # 指定されたIDの記事を探す
    post = None
    for p in POSTS:
        if p["id"] == post_id:
            post = p
            break

    context = {"post": post, "posts": POSTS}
    return render(request, "blog/post_detail.html", context)
