from django import forms
from .models import Category


class PostSearchForm(forms.Form):
    """記事検索フォーム"""

    # 検索キーワード
    keyword = forms.CharField(
        label="検索キーワード",
        max_length=100,
        required=False,  # 必須ではない
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "タイトルや本文から検索...",
            }
        ),
    )

    # カテゴリ絞り込み
    category = forms.ModelChoiceField(
        label="カテゴリ",
        queryset=Category.objects.all(),
        required=False,
        empty_label="すべてのカテゴリ",
        widget=forms.Select(
            attrs={
                "class": "form-control",
            }
        ),
    )

    # 並び順
    order_by = forms.ChoiceField(
        label="並び順",
        choices=[
            ("-created_at", "新しい順"),
            ("created_at", "古い順"),
            ("title", "タイトル順"),
        ],
        required=False,
        initial="-created_at",
        widget=forms.Select(
            attrs={
                "class": "form-control",
            }
        ),
    )
