from django.shortcuts import render


# Create your views here.
def post_list(request):
    # 仮のデータ（後でデータベースから取得するようになります）
    posts = [
        {
            "id": 1,
            "title": "Djangoを始めました",
            "content": "Djangoの学習を始めました。楽しいです！",
            "created_at": "2025-07-01",
        },
        {
            "id": 2,
            "title": "ビューについて学んだこと",
            "content": "今日はビューについて学びました。",
            "created_at": "2025-07-02",
        },
        {
            "id": 3,
            "title": "テンプレートは便利",
            "content": "テンプレートを使うとHTMLが書きやすいです。",
            "created_at": "2025-07-03",
        },
    ]

    context = {
        "posts": posts,
    }
    return render(request, "blog/post_list.html", context)
