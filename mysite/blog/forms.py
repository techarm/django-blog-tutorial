from django import forms
from .models import Category, Post


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


class CommentForm(forms.Form):
    """コメント投稿フォーム"""

    name = forms.CharField(
        label="お名前",
        max_length=50,
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "お名前を入力",
            }
        ),
    )

    email = forms.EmailField(
        label="メールアドレス",
        widget=forms.EmailInput(
            attrs={
                "class": "form-control",
                "placeholder": "your@email.com",
            }
        ),
    )

    content = forms.CharField(
        label="コメント",
        widget=forms.Textarea(
            attrs={
                "class": "form-control",
                "rows": 4,
                "placeholder": "コメントを入力してください",
            }
        ),
    )

    def clean_content(self):
        """コメント内容のバリデーション"""
        content = self.cleaned_data["content"]

        # 最小文字数チェック
        if len(content) < 5:
            raise forms.ValidationError("コメントは5文字以上で入力してください。")

        # NGワードチェック（例）
        ng_words = ["spam", "スパム"]
        for word in ng_words:
            if word in content.lower():
                raise forms.ValidationError("不適切な内容が含まれています。")

        return content


class PostForm(forms.ModelForm):
    """記事作成・編集フォーム"""

    class Meta:
        model = Post
        fields = ["title", "content", "category", "tags", "is_featured", "is_published"]
        widgets = {
            "title": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "記事のタイトルを入力"}
            ),
            "content": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "rows": 10,
                    "placeholder": "記事の本文を入力",
                }
            ),
            "category": forms.Select(attrs={"class": "form-control"}),
            "tags": forms.CheckboxSelectMultiple(attrs={"class": "form-check-input"}),
            "is_featured": forms.CheckboxInput(attrs={"class": "form-check-input"}),
            "is_published": forms.CheckboxInput(attrs={"class": "form-check-input"}),
        }
        labels = {
            "title": "タイトル",
            "content": "本文",
            "category": "カテゴリー",
            "tags": "タグ",
            "is_featured": "注目記事にする",
            "is_published": "公開する",
        }
        help_texts = {
            "title": "魅力的なタイトルを付けましょう",
            "tags": "複数選択できます",
            "is_published": "チェックを外すと下書きとして保存されます",
        }

    def clean_title(self):
        """タイトルのバリデーション"""
        title = self.cleaned_data.get("title")

        # 最小文字数チェック
        if len(title) < 5:
            raise forms.ValidationError("タイトルは5文字以上で入力してください。")

        # NGワードチェック
        ng_words = ["test", "テスト"]
        for word in ng_words:
            if word.lower() in title.lower():
                raise forms.ValidationError(
                    "タイトルに使用できない単語が含まれています。"
                )

        return title

    def clean(self):
        """フォーム全体のバリデーション"""
        cleaned_data = super().clean()
        is_published = cleaned_data.get("is_published")
        category = cleaned_data.get("category")

        # 公開する場合はカテゴリー必須
        if is_published and not category:
            raise forms.ValidationError(
                "公開する記事にはカテゴリーを設定してください。"
            )

        return cleaned_data
