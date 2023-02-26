# 登録されている作者のイラストを閲覧することができるウェブアプリ

# 作成の動機
私の妹が、カテゴリーごとにイラストをコメントなどを添えてHTMLでサイト

https://kasanefunk.github.io/kasanesworks/kasaneworks.japanese/index.html

を作っていたのですが、管理画面からイラストやコメント等を登録できるようにしたいと言っていたことがきっかけで今回このようなウェブアプリを作ることになりました。私が作成したウェブアプリは下記URLになります。

https://kukanji.pythonanywhere.com/

サイト構成としては最初にそれぞれの管理者の名前が表示されるトップページがあり、表示されている管理者の名前をタップするとその管理者のホームページへ遷移するようにしました。ホームページではその管理者のコメントと、管理者の所有しているカテゴリーページへのURLが表示されます。カテゴリーページでは管理者のコメントとカテゴリーごとのイラストが表示されます。

# システム構成
<img width="563" alt="system_structure2" src="https://user-images.githubusercontent.com/111495470/221393168-586b1c2d-af11-4e28-a766-969b1f77dcf2.png">

使用言語はPythonでフレームワークにはDjangoを使いました。デプロイにはPythonanywhereを使いしました。開発時にはPostgreSQLを使っていましたが、PythonanywhereではPostgreSQLを使うことができなかったためPythonanywhere上ではMySQLを使っています。サイト管理画面にはDjangoのadminを使いました。

# 使用技術
・Python

・Django

・PostgreSQL

・MySQL

・Git

・HTML＆CSS

