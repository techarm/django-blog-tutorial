from django import template
from django.utils.safestring import mark_safe
import markdown

register = template.Library()


@register.filter(name="markdown_to_html")
def markdown_to_html(text):
    """MarkdownテキストをHTMLに変換"""

    # Markdown拡張機能の設定
    md = markdown.Markdown(
        extensions=[
            "extra",  # テーブル、脚注、定義リストなど
            "codehilite",  # コードブロックのシンタックスハイライト
            "toc",  # 目次生成（[TOC]タグ）
            "tables",  # テーブル記法
            "fenced_code",  # ```で囲むコードブロック
        ],
        extension_configs={
            "codehilite": {
                "noclasses": True,
                "pygments_style": "solarized-light",
            }
        },
    )

    html = md.convert(text)
    return mark_safe(html)
