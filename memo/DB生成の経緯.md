# DB生成の経緯

* DBファイル作成
    * DB出力先パスの作成
        * dir, filename, ext
    * DB生成メソッドのファイルパス作成
    * DB生成メソッド
        * Create table
            * sqlファイル
            * pyコード
        * Insert
            * sqlファイル
            * pyコード
            * tsvファイル
    * https://github.com/ytyaru0/GitHub.Uploader.Pi3.Https.201803020700/blob/master/src/database/init/DbInitializer.py
    * https://github.com/ytyaru0/GitHub.Uploader.Pi3.Https.201803020700/blob/master/src/database/init/DbInitializerByMultiUsers.py
* DBアクセサ
    * アクセサクラス生成
    * アクセサクラスのプロパティ生成
    * https://github.com/ytyaru0/GitHub.Uploader.Pi3.Https.201803020700/blob/master/src/database/DatabaseMeta.py
* DBトランザクタ
    * db.connect()インスタンス生成
    * db.begin()
    * db.commit()
    * https://github.com/ytyaru0/Python.Sqlite3.class.201803051700000/blob/master/src/8/db/service/MainService.py

# インタフェース

```
# DBファイル操作
Database().Initialize() # DBファイル作成とServices生成
Database().Upload() # DBファイルのアップロード

# ビジネスロジック（複合テーブル操作。トランザクション）
Database().Services.User.Gets()
Database().Services.User.IsExist(user)
Database().Services.User.Add(user)
Database().Services.User.Remove(user)
Database().Services.User.Rename(user, new)
Database().Services.Repository.Create(user, repo)
Database().Services.Repository.Delete(user, repo)
Database().Services.Repository.Commit(git_log)
Database().Services.Aggregate.CreateHtml()

# テーブル単位だと以下のようになる
Database().Repos[username]['Repositories'].find(Id=None, Name=None)
Database().Users['Users'].insert({...})
Database().Repositories['username']['tablename'].insert({...})
```

# 問題

* [SQLite3はDBファイル間の関係を定義できない](SQLite3はDBファイル間の関係を定義できない.md)

# 対策

定義する方法をつくりだす。

ファイル名|説明
----------|----
sqlite.names|DBの名前、出力パス、入力パス
sqlite.relate.contain|包含関係
sqlite.relate.list|前後関係（ファイルサイズによりやむなくファイル分割）

## sqlite.names

```
Name    OUT                                 IN
L   res/db/Languages.db                 src/db/Languages/
U   res/db/Users.db                     src/db/Users/
U   res/db/Repos/{U.Users.Id}{List}.db  src/db/Languages/
```

## sqlite.relate.contain

```
Parent          Child
U.Users.Id      R.Repositories.UserId
L.Languages.Id  R.EditingAmounts.LanguageId
```

