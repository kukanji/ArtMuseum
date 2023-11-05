# 使い方
サーバーを起動するには以下のコマンドを実行する
```gitbash
python3 manage.py runserver
```

マイグレーションファイルを作成するには以下のコマンドを実行する
```gitbash
python manage.py makemigrations
```

作成したマイグレーションファイルをデータベースに追加するには以下のコマンドを実行する
```gitbash
python manage.py migrate
```

データベースに接続した状態で対話シェルを立ち上げるには次のコマンドを実行する
```gitbash
python manage.py shell
```