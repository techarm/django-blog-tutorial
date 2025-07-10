from django import template
from datetime import datetime

register = template.Library()


@register.simple_tag
def current_year():
    """現在の年を返す"""
    return datetime.now().year


@register.simple_tag
def greeting():
    """時間帯に応じた挨拶を返す"""
    hour = datetime.now().hour
    if 5 <= hour < 12:
        return "おはようございます"
    elif 12 <= hour < 17:
        return "こんにちは"
    elif 17 <= hour < 21:
        return "こんばんは"
    else:
        return "おやすみなさい"


@register.filter
def add_mark(value, mark="！"):
    """文字列の最後にマークを追加"""
    return f"{value}{mark}"
