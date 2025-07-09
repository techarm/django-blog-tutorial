from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime


# Create your views here.
def hello_world(request):
    return HttpResponse("Hello Django!")


def current_time(request):
    now = datetime.now()
    html = f"<html><body><h1>現在時刻は {now} です！</h1></body></html>"
    return HttpResponse(html)


def show_request_info(request):
    info = f"""
    <html>
    <body>
        <h1>リクエスト情報</h1>
        <p>メソッド: {request.method}</p>
        <p>パス: {request.path}</p>
        <p>ユーザーエージェント: {request.META.get('HTTP_USER_AGENT', 'なし')}</p>
    </body>
    </html>
    """
    return HttpResponse(info)


def hello_template(request):
    return render(request, "practice/hello_template.html")


def greeting(request):
    context = {
        "name": "太郎",
        "age": 25,
        "hobbies": ["プログラミング", "読書", "散歩"],
    }
    return render(request, "practice/greeting.html", context)


def greet_user(request, username):
    context = {
        "username": username,
    }
    return render(request, "practice/greet_user.html", context)
