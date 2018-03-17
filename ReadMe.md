# このソフトウェアについて

簡易アップローダのDBを作る。

Repositoryとそのcreate, commitを記録するためのDB。将来的には、そのDBをUploadしたり集計したい。

* [簡易アップローダ](https://github.com/ytyaru0/Shell.Github.Commiter.20180316160244)

# DB

DBファイル|概要
----------|----
Users.db|ユーザ名
Repositories.{UserId}.db|リポジトリ
languages.yml|プログラミング言語

公開しても問題ない内容のみ。以下のデータは含めない。

* Password
* TwoFactorSecret
* AccessToken
* ClientId, ClientSecret
* MailAddress
* SSH鍵(公開,秘密)

## Users.db

### Users

```sql
create table Users (
    Id          integer primary key autoincrement,
    Name        text unique
);
```

## Repositories.{UserId}.db

### Repositories

```sql
create table Repositories (
    Id          integer primary key autoincrement,
    Name        text unique,
    Created     text -- yyyy-MM-dd HH:mm:ss
);
```

### Commits

```sql
create table Commits (
    Id          integer primary key,
    RepoId      integer,
    Message     text,
    Datetime    text, -- yyyy-MM-dd HH:mm:ss +0900
    Sha         text,
    foreign key RepoId reference Repositories(Id)
);
```


* `git log --numstat --date=iso --author='username'`

```sh
commit 088476baccfa485e2a9fff92048ad7b6b8bf12fe
Author: ytyaru0 <ytyaru0@outlook.jp>
Date:   2018-03-16 17:45:16 +0900

    ユーザ選択を追加

12      2       ReadMe.md
33      7       src/push.sh
```

上記のうち、Sha, Date, Messageを取得する。

* 行数（追加、削除）、ファイル種別は、`EditCounts`テーブルで管理する
* git diff による変更箇所の確認は`Sha`によりURLを作成して参照させる
    * 例: `https://github.com/ytyaru0/Shell.Github.Commiter.20180316160244/commit/33cb894bb5c370e47cd053f5f80430cc4d4d1744`
        * `https://github.com/{user}/{repo}/commit/{sha}`
    * DBに変更箇所テキストは残さない
        * データ量が膨大になるため
    * `.git`は使わない
        * `.git`がローカルにあるとは限らないため
        * `.git`がローカルにあったら二重保存になるため

### EditingAmounts

```sql
create table EditingAmounts (
    Id          integer primary key,
    CommitId    integer,
    LanguageId  integer, -- Languages.db Languages.Id
    Insertions  integer,
    Deletions   integer,
    foreign key CommitId reference Commits(Id)
);
```

* `git log --numstat --date=iso --author='username'`
    * Insertions, Deletions, Filename の順

## languages.yml

DBにせずyamlファイルのまま利用すればいいかもしれない。

* https://raw.githubusercontent.com/github/linguist/master/lib/linguist/languages.yml
* https://github.com/ytyaru0/GitHub.Uploader.Pi3.Https.201803020700/blob/master/src/database/init/Languages/insert/py/LanguageSource.py

以下のように言語別の集計ができる。

```
{user}/{repo}
15 hour ago (2000-01-01 12:34:56)
{commit_message}
* programming  70%
    * .py 50 (+45, -5)  70%
    * .sh 20 (+15, -5)  30%
* markup 10%
    * .html: 20 (+15, -5)
* data 10%
    * .csv: 20 (+15, -5)
* prose 10%
    * .md: 20 (+15, -5)
```

5W1H|値
----|--
誰が|username
いつ|commit date
どこに|repo name
何をした|commit message
どのくらい|[{lang: line}, {lang: line}, ...]

### Repositories

# 開発環境

* [Raspberry Pi](https://ja.wikipedia.org/wiki/Raspberry_Pi) 3 Model B
    * [Raspbian](https://www.raspberrypi.org/downloads/raspbian/) GNU/Linux 8.0 (jessie)
        * bash 4.3.30

# ライセンス

このソフトウェアはCC0ライセンスである。

[![CC0](http://i.creativecommons.org/p/zero/1.0/88x31.png "CC0")](http://creativecommons.org/publicdomain/zero/1.0/deed.ja)

利用ライブラリは以下。

Library|License|Copyright
-------|-------|---------
[assert.sh](https://github.com/lehmannro/assert.sh)|[LGPL-3.0](https://github.com/lehmannro/assert.sh/blob/master/COPYING.LESSER)|[Copyright (C) 2007 Free Software Foundation, Inc. http://fsf.org/](https://github.com/lehmannro/assert.sh/blob/master/COPYING)

