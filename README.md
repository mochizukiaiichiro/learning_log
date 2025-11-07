# 学習ノートアプリ（Learning Log）

Django を使って構築した「学習ノート」アプリです。  
ユーザーが自分の学習トピックを登録し、それに関連する記事を記録・編集・閲覧できる Web アプリケーションです。

---

## 特徴

- ユーザー登録・ログイン機能（Django 標準認証）
- トピックの追加・一覧表示・詳細表示
- 記事の追加・編集・表示（トピックごと）
- Bootstrap 5 によるレスポンシブな UI
- Django のクラスベースではなく関数ベースビューで構成

---

## 使用技術

| 技術              | バージョン |
| ----------------- | ---------- |
| Python            | 3.14.0     |
| Django            | 5.2.7      |
| django-bootstrap5 | 25.2       |
| SQLite            | 標準       |

---

## ディレクトリ構成

```text
learning_log/
        ├── learning_logs/  # メインアプリ（トピック・記事管理）
        ├── users/          # 認証関連（ログイン・登録）
        ├── templates/      # HTMLテンプレート
        ├── static/         # 静的ファイル（CSS/JS）
        └── manage.py       # Django管理コマンド
```

---

## セットアップ手順

1. 依存パッケージをインストール

```bash
pip install -r requirements.txt
```

2. マイグレーションと起動

```bash
python manage.py migrate
python manage.py runserver
```
