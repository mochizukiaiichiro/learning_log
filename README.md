# 概要

Django/Python を用いた WEB アプリケーションの学習のために作成したアプリケーションです。『[最短距離でゼロからしっかり学ぶ Python 入門
実践編](https://gihyo.jp/book/2020/978-4-297-11572-2)』の 学習ノートアプリを元に機能の追加や改善、技術の最新化、モジュール構成の最適化などを行っています。

---

## 特徴

- ユーザー登録・ログイン機能（Django 標準認証）
- トピックの追加・一覧表示・詳細表示
- 記事の追加・編集・表示（トピックごと）

## 変更点

- Django 2.2.x → Django 5.2.x
- django-bootstrap 4 → django-bootstrap 5

## 追加点

- 記事の削除

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
