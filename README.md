# Django ブログチュートリアル

このリポジトリは、**[techarm.dev](https://techarm.dev)** の Django チュートリアルシリーズで作成されたブログアプリケーションのソースコードです。

## 📚 完全なチュートリアルシリーズ

このプロジェクトは以下のステップバイステップチュートリアルで詳しく解説されています：

### **[🔗 Django チュートリアルシリーズ全記事はこちら](https://techarm.dev/series/django)**

---

## 📖 各記事とブランチ対応表

| 記事                                                                                      | ブランチ                    | 内容                                     |
| ----------------------------------------------------------------------------------------- | --------------------------- | ---------------------------------------- |
| **[第 1 回：Django とは？](https://techarm.dev/series/django/01-what-is-django)**         | `-`                      | Django の基本概念・MVT パターン解説      |
| **[第 2 回：環境構築](https://techarm.dev/series/django/02-python-vscode-setup)**         | `02-environment-setup`      | Python・VSCode・Django のインストール    |
| **[第 3 回：プロジェクト構造](https://techarm.dev/series/django/03-project-structure)**   | `03-project-structure`      | プロジェクトとアプリの違い・フォルダ構成 |
| **[第 4 回：初めての View](https://techarm.dev/series/django/04-first-view)**             | `04-first-view`             | 関数ベースビューで Hello World           |
| **[第 5 回：テンプレート](https://techarm.dev/series/django/05-templates)**               | `05-templates`              | テンプレート継承・静的ファイル           |
| **[第 6 回：モデル・DB](https://techarm.dev/series/django/06-models-database)**           | `06-models-database`        | モデルでデータベース操作                 |
| **[第 7 回：フォーム](https://techarm.dev/series/django/07-forms)**                       | `07-forms`                  | フォームクラスでユーザー入力処理         |
| **[第 8 回：クラスベースビュー](https://techarm.dev/series/django/08-class-based-views)** | `08-class-based-views`      | ListView・DetailView の活用              |
| **[第 9 回：CRUD 操作](https://techarm.dev/series/django/09-modelform-crud)**             | `09-modelform-crud`         | ModelForm で記事の作成・編集・削除       |
| **[第 10 回：認証・最終回](https://techarm.dev/series/django/10-markdown-auth-complete)** | `10-markdown-auth-complete` | ユーザー認証・Markdown エディター        |

## 🚀 プロジェクトの実行方法

### 前提条件

- Python 3.8 以上
- pip または pipenv

### セットアップ

```bash
# リポジトリのクローン
git clone <このリポジトリのURL>
cd mysite

# 仮想環境の作成と有効化
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# 依存関係のインストール
pip install -r requirements.txt

# データベースのマイグレーション
python manage.py migrate

# 開発サーバーの起動
python manage.py runserver
```

### 管理ユーザーの作成

```bash
python manage.py createsuperuser
```

## 📂 ブランチ別学習方法

各記事に対応するブランチをチェックアウトして、段階的に学習できます：

```bash
# 特定の記事のコードを確認
git checkout 05-templates

# 最新の完成版を確認
git checkout main
```

## ✨ このチュートリアルで学べること

- ✅ Django の基本概念（MVT パターン）
- ✅ プロジェクトとアプリの構造理解
- ✅ テンプレートエンジンの活用
- ✅ モデルによるデータベース操作
- ✅ フォームによる入力検証
- ✅ クラスベースビューの実装
- ✅ CRUD 操作の完全実装
- ✅ ユーザー認証システム
- ✅ Markdown エディターの導入

## 🎯 対象読者

- Python を少し触ったことがある方
- Web アプリケーション開発に興味がある方
- Django を体系的に学びたい方
- 実際に動くアプリを作りながら学びたい方

## 🔥 **さらに詳しく学びたい方へ**

### **[📝 techarm.dev ブログで完全解説を読む](https://techarm.dev/series/django)**

- 🎯 **図解豊富で初心者にも分かりやすい**
- 💡 **実際のコードと一緒に詳しく解説**
- ⚡ **躓きやすいポイントも丁寧にフォロー**
- 🚀 **実践的なテクニックも多数紹介**

---

**[🔗 最新記事をチェック](https://techarm.dev)**

## 📞 質問・フィードバック

チュートリアルについて質問がありましたら、各記事のコメント欄でお気軽にどうぞ！

---

<div align="center">

**⭐ このリポジトリが役に立ったら Star をお願いします！⭐**

**[🚀 Django マスターへの道のりはここから](https://techarm.dev/series/django)**

</div>
