# 登録されている作者のイラストを閲覧することができるウェブアプリ

# 作成の動機
私の妹が、カテゴリーごとにイラストをコメントなどを添えてHTMLでサイト

https://kasanefunk.github.io/kasanesworks/kasaneworks.japanese/index.html

を作っていたのですが、管理画面からイラストやコメント等を登録できるようにしたいと言っていたことがきっかけで今回このようなウェブアプリを作ることになりました。私が作成したウェブアプリは下記URLになります。

https://kukanji.pythonanywhere.com/kasane/

サイト構成としては最初にそれぞれの管理者の名前が表示されるトップページがあり、表示されている管理者の名前をタップするとその管理者のホームページへ遷移するようにしました。ホームページではその管理者のコメントと、管理者の所有しているカテゴリーページへのURLが表示されます。カテゴリーページでは管理者のコメントとカテゴリーごとのイラストが表示されます。

・トップページ

<img width="960" alt="top_page" src="https://user-images.githubusercontent.com/111495470/221399256-af3d1c0e-1226-4edf-b12e-21d8c8de3037.png">

・マイページ

<img width="944" alt="HomePage1" src="https://user-images.githubusercontent.com/111495470/221401845-a2f20ad1-f517-4ea1-b56f-f9059813b51e.png">
<img width="938" alt="HomePage2" src="https://user-images.githubusercontent.com/111495470/221401849-d618f855-1288-46c4-a89a-3003c3de0c9f.png">

・カテゴリーページ

<img width="935" alt="CategoryPage1" src="https://user-images.githubusercontent.com/111495470/221401919-e094a78a-0bc0-4ffd-83e9-233842fd80b4.png">
<img width="938" alt="CategoryPage2" src="https://user-images.githubusercontent.com/111495470/221401924-12cfeab4-7417-46c6-81e6-8f29ea177c19.png">
<img width="946" alt="CategoryPage3" src="https://user-images.githubusercontent.com/111495470/221401927-2a55240f-7ebf-4f33-a1cb-c26fe83c6f56.png">

・管理画面

<img width="959" alt="image" src="https://github.com/kukanji/webproject/assets/111495470/ad80dd09-0896-4552-8e54-59597deb31ed">

# システム構成
<img width="614" alt="system_structure" src="https://user-images.githubusercontent.com/111495470/221402042-84a54075-fd98-4862-8d82-ffb5369bfee3.png">

使用言語はPythonでフレームワークにはDjangoを使いました。デプロイにはPythonanywhereを使いしました。開発時にはPostgreSQLを使っていましたが、PythonanywhereではPostgreSQLを使うことができなかったためPythonanywhere上ではMySQLを使っています。サイト管理画面にはDjangoのadminを使いました。

# 使用技術
・Python

・Django

・PostgreSQL

・MySQL

・Git

・HTML＆CSS

