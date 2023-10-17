# 起動方法
```bash
#bash 

# mysqlの起動
make mysql

# 任意の方法でmysqlをマイグレーション

# サーバの起動
make run

```

## ページ構成

- index -> 初期画面
- create_user -> ユーザ登録フォーム
- users -> ユーザ一覧
  - 一括削除ができる
- users/:id　-> ユーザ単体表示
  - 単体削除ができる