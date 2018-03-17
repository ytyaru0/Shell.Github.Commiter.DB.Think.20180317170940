# 

## Events

リポジトリのイベントを取得する。commitの識別子が取得できたらOK。

/repos/:owner/:repo/events
/repos/ytyaru0/Shell.Github.Commiter.20180316160244/events
https://api.github.com/repos/ytyaru0/Shell.Github.Commiter.20180316160244/events

* CreateEvent
* PushEvent


```json
[
  {
    "id": "7390139132",
    "type": "PushEvent",
    "actor": {
      "id": 21254319,
      "login": "ytyaru0",
      "display_login": "ytyaru0",
      "gravatar_id": "",
      "url": "https://api.github.com/users/ytyaru0",
      "avatar_url": "https://avatars.githubusercontent.com/u/21254319?"
    },
    "repo": {
      "id": 125483162,
      "name": "ytyaru0/Shell.Github.Commiter.20180316160244",
      "url": "https://api.github.com/repos/ytyaru0/Shell.Github.Commiter.20180316160244"
    },
    "payload": {
      "push_id": 2408358803,
      "size": 1,
      "distinct_size": 1,
      "ref": "refs/heads/master",
      "head": "6f2e7b3285a77351c2aef063b2886c1a78c2e0b4",
      "before": "33cb894bb5c370e47cd053f5f80430cc4d4d1744",
      "commits": [
        {
          "sha": "6f2e7b3285a77351c2aef063b2886c1a78c2e0b4",
          "author": {
            "email": "ytyaru0@outlook.jp",
            "name": "ytyaru0"
          },
          "message": "パスワード取得関数の集約",
          "distinct": true,
          "url": "https://api.github.com/repos/ytyaru0/Shell.Github.Commiter.20180316160244/commits/6f2e7b3285a77351c2aef063b2886c1a78c2e0b4"
        }
      ]
    },
    "public": true,
    "created_at": "2018-03-16T11:13:30Z"
  },
  {
    "id": "7390067320",
    "type": "PushEvent",
    "actor": {
      "id": 21254319,
      "login": "ytyaru0",
      "display_login": "ytyaru0",
      "gravatar_id": "",
      "url": "https://api.github.com/users/ytyaru0",
      "avatar_url": "https://avatars.githubusercontent.com/u/21254319?"
    },
    "repo": {
      "id": 125483162,
      "name": "ytyaru0/Shell.Github.Commiter.20180316160244",
      "url": "https://api.github.com/repos/ytyaru0/Shell.Github.Commiter.20180316160244"
    },
    "payload": {
      "push_id": 2408319823,
      "size": 1,
      "distinct_size": 1,
      "ref": "refs/heads/master",
      "head": "33cb894bb5c370e47cd053f5f80430cc4d4d1744",
      "before": "f0626315202193accfbb74968b2a41a38bf3d375",
      "commits": [
        {
          "sha": "33cb894bb5c370e47cd053f5f80430cc4d4d1744",
          "author": {
            "email": "ytyaru0@outlook.jp",
            "name": "ytyaru0"
          },
          "message": "exit 1処理を一行で書いた",
          "distinct": true,
          "url": "https://api.github.com/repos/ytyaru0/Shell.Github.Commiter.20180316160244/commits/33cb894bb5c370e47cd053f5f80430cc4d4d1744"
        }
      ]
    },
    "public": true,
    "created_at": "2018-03-16T10:57:23Z"
  },
  {
    "id": "7390032569",
    "type": "PushEvent",
    "actor": {
      "id": 21254319,
      "login": "ytyaru0",
      "display_login": "ytyaru0",
      "gravatar_id": "",
      "url": "https://api.github.com/users/ytyaru0",
      "avatar_url": "https://avatars.githubusercontent.com/u/21254319?"
    },
    "repo": {
      "id": 125483162,
      "name": "ytyaru0/Shell.Github.Commiter.20180316160244",
      "url": "https://api.github.com/repos/ytyaru0/Shell.Github.Commiter.20180316160244"
    },
    "payload": {
      "push_id": 2408301223,
      "size": 1,
      "distinct_size": 1,
      "ref": "refs/heads/master",
      "head": "f0626315202193accfbb74968b2a41a38bf3d375",
      "before": "71ac542d157bc4a0b32d16d409d7c42f05f50452",
      "commits": [
        {
          "sha": "f0626315202193accfbb74968b2a41a38bf3d375",
          "author": {
            "email": "ytyaru0@outlook.jp",
            "name": "ytyaru0"
          },
          "message": "select, for, ifを一行で書いた",
          "distinct": true,
          "url": "https://api.github.com/repos/ytyaru0/Shell.Github.Commiter.20180316160244/commits/f0626315202193accfbb74968b2a41a38bf3d375"
        }
      ]
    },
    "public": true,
    "created_at": "2018-03-16T10:49:50Z"
  },
  {
    "id": "7389993021",
    "type": "PushEvent",
    "actor": {
      "id": 21254319,
      "login": "ytyaru0",
      "display_login": "ytyaru0",
      "gravatar_id": "",
      "url": "https://api.github.com/users/ytyaru0",
      "avatar_url": "https://avatars.githubusercontent.com/u/21254319?"
    },
    "repo": {
      "id": 125483162,
      "name": "ytyaru0/Shell.Github.Commiter.20180316160244",
      "url": "https://api.github.com/repos/ytyaru0/Shell.Github.Commiter.20180316160244"
    },
    "payload": {
      "push_id": 2408279777,
      "size": 1,
      "distinct_size": 1,
      "ref": "refs/heads/master",
      "head": "71ac542d157bc4a0b32d16d409d7c42f05f50452",
      "before": "8009a7df5366d2e34003e9fb2d2c7c544e459c6f",
      "commits": [
        {
          "sha": "71ac542d157bc4a0b32d16d409d7c42f05f50452",
          "author": {
            "email": "ytyaru0@outlook.jp",
            "name": "ytyaru0"
          },
          "message": "DBファイルパスを一箇所に集約した",
          "distinct": true,
          "url": "https://api.github.com/repos/ytyaru0/Shell.Github.Commiter.20180316160244/commits/71ac542d157bc4a0b32d16d409d7c42f05f50452"
        }
      ]
    },
    "public": true,
    "created_at": "2018-03-16T10:41:16Z"
  },
  {
    "id": "7389945948",
    "type": "PushEvent",
    "actor": {
      "id": 21254319,
      "login": "ytyaru0",
      "display_login": "ytyaru0",
      "gravatar_id": "",
      "url": "https://api.github.com/users/ytyaru0",
      "avatar_url": "https://avatars.githubusercontent.com/u/21254319?"
    },
    "repo": {
      "id": 125483162,
      "name": "ytyaru0/Shell.Github.Commiter.20180316160244",
      "url": "https://api.github.com/repos/ytyaru0/Shell.Github.Commiter.20180316160244"
    },
    "payload": {
      "push_id": 2408254350,
      "size": 1,
      "distinct_size": 1,
      "ref": "refs/heads/master",
      "head": "8009a7df5366d2e34003e9fb2d2c7c544e459c6f",
      "before": "28c4456d5756867543d1b0502c2f6e48d72ac1b7",
      "commits": [
        {
          "sha": "8009a7df5366d2e34003e9fb2d2c7c544e459c6f",
          "author": {
            "email": "ytyaru0@outlook.jp",
            "name": "ytyaru0"
          },
          "message": "シェバング行追加",
          "distinct": true,
          "url": "https://api.github.com/repos/ytyaru0/Shell.Github.Commiter.20180316160244/commits/8009a7df5366d2e34003e9fb2d2c7c544e459c6f"
        }
      ]
    },
    "public": true,
    "created_at": "2018-03-16T10:31:16Z"
  },
  {
    "id": "7389749014",
    "type": "PushEvent",
    "actor": {
      "id": 21254319,
      "login": "ytyaru0",
      "display_login": "ytyaru0",
      "gravatar_id": "",
      "url": "https://api.github.com/users/ytyaru0",
      "avatar_url": "https://avatars.githubusercontent.com/u/21254319?"
    },
    "repo": {
      "id": 125483162,
      "name": "ytyaru0/Shell.Github.Commiter.20180316160244",
      "url": "https://api.github.com/repos/ytyaru0/Shell.Github.Commiter.20180316160244"
    },
    "payload": {
      "push_id": 2408150288,
      "size": 1,
      "distinct_size": 1,
      "ref": "refs/heads/master",
      "head": "28c4456d5756867543d1b0502c2f6e48d72ac1b7",
      "before": "344e93b40b17920b2969534067ce22de3d21325e",
      "commits": [
        {
          "sha": "28c4456d5756867543d1b0502c2f6e48d72ac1b7",
          "author": {
            "email": "ytyaru0@outlook.jp",
            "name": "ytyaru0"
          },
          "message": "ユーザ名指定時のみ存在エラー",
          "distinct": true,
          "url": "https://api.github.com/repos/ytyaru0/Shell.Github.Commiter.20180316160244/commits/28c4456d5756867543d1b0502c2f6e48d72ac1b7"
        }
      ]
    },
    "public": true,
    "created_at": "2018-03-16T09:50:57Z"
  },
  {
    "id": "7389585084",
    "type": "PushEvent",
    "actor": {
      "id": 21254319,
      "login": "ytyaru0",
      "display_login": "ytyaru0",
      "gravatar_id": "",
      "url": "https://api.github.com/users/ytyaru0",
      "avatar_url": "https://avatars.githubusercontent.com/u/21254319?"
    },
    "repo": {
      "id": 125483162,
      "name": "ytyaru0/Shell.Github.Commiter.20180316160244",
      "url": "https://api.github.com/repos/ytyaru0/Shell.Github.Commiter.20180316160244"
    },
    "payload": {
      "push_id": 2408064016,
      "size": 1,
      "distinct_size": 1,
      "ref": "refs/heads/master",
      "head": "344e93b40b17920b2969534067ce22de3d21325e",
      "before": "43754c4f0bfb405590f95d47b8acf308edf3d9de",
      "commits": [
        {
          "sha": "344e93b40b17920b2969534067ce22de3d21325e",
          "author": {
            "email": "ytyaru0@outlook.jp",
            "name": "ytyaru0"
          },
          "message": "引数エラー確認の削除とReadMeファイル存在確認のリファクタリング",
          "distinct": true,
          "url": "https://api.github.com/repos/ytyaru0/Shell.Github.Commiter.20180316160244/commits/344e93b40b17920b2969534067ce22de3d21325e"
        }
      ]
    },
    "public": true,
    "created_at": "2018-03-16T09:16:21Z"
  },
  {
    "id": "7389500171",
    "type": "PushEvent",
    "actor": {
      "id": 21254319,
      "login": "ytyaru0",
      "display_login": "ytyaru0",
      "gravatar_id": "",
      "url": "https://api.github.com/users/ytyaru0",
      "avatar_url": "https://avatars.githubusercontent.com/u/21254319?"
    },
    "repo": {
      "id": 125483162,
      "name": "ytyaru0/Shell.Github.Commiter.20180316160244",
      "url": "https://api.github.com/repos/ytyaru0/Shell.Github.Commiter.20180316160244"
    },
    "payload": {
      "push_id": 2408019970,
      "size": 1,
      "distinct_size": 1,
      "ref": "refs/heads/master",
      "head": "43754c4f0bfb405590f95d47b8acf308edf3d9de",
      "before": "088476baccfa485e2a9fff92048ad7b6b8bf12fe",
      "commits": [
        {
          "sha": "43754c4f0bfb405590f95d47b8acf308edf3d9de",
          "author": {
            "email": "ytyaru0@outlook.jp",
            "name": "ytyaru0"
          },
          "message": "ReadMeファイル存在確認のリファクタリング",
          "distinct": true,
          "url": "https://api.github.com/repos/ytyaru0/Shell.Github.Commiter.20180316160244/commits/43754c4f0bfb405590f95d47b8acf308edf3d9de"
        }
      ]
    },
    "public": true,
    "created_at": "2018-03-16T08:57:24Z"
  },
  {
    "id": "7389449369",
    "type": "PushEvent",
    "actor": {
      "id": 21254319,
      "login": "ytyaru0",
      "display_login": "ytyaru0",
      "gravatar_id": "",
      "url": "https://api.github.com/users/ytyaru0",
      "avatar_url": "https://avatars.githubusercontent.com/u/21254319?"
    },
    "repo": {
      "id": 125483162,
      "name": "ytyaru0/Shell.Github.Commiter.20180316160244",
      "url": "https://api.github.com/repos/ytyaru0/Shell.Github.Commiter.20180316160244"
    },
    "payload": {
      "push_id": 2407993545,
      "size": 1,
      "distinct_size": 1,
      "ref": "refs/heads/master",
      "head": "088476baccfa485e2a9fff92048ad7b6b8bf12fe",
      "before": "f132792d261ea41134501b5696a0e4ceaf617657",
      "commits": [
        {
          "sha": "088476baccfa485e2a9fff92048ad7b6b8bf12fe",
          "author": {
            "email": "ytyaru0@outlook.jp",
            "name": "ytyaru0"
          },
          "message": "ユーザ選択を追加",
          "distinct": true,
          "url": "https://api.github.com/repos/ytyaru0/Shell.Github.Commiter.20180316160244/commits/088476baccfa485e2a9fff92048ad7b6b8bf12fe"
        }
      ]
    },
    "public": true,
    "created_at": "2018-03-16T08:45:21Z"
  },
  {
    "id": "7389279806",
    "type": "CreateEvent",
    "actor": {
      "id": 21254319,
      "login": "ytyaru0",
      "display_login": "ytyaru0",
      "gravatar_id": "",
      "url": "https://api.github.com/users/ytyaru0",
      "avatar_url": "https://avatars.githubusercontent.com/u/21254319?"
    },
    "repo": {
      "id": 125483162,
      "name": "ytyaru0/Shell.Github.Commiter.20180316160244",
      "url": "https://api.github.com/repos/ytyaru0/Shell.Github.Commiter.20180316160244"
    },
    "payload": {
      "ref": "master",
      "ref_type": "branch",
      "master_branch": "master",
      "description": null,
      "pusher_type": "user"
    },
    "public": true,
    "created_at": "2018-03-16T08:00:18Z"
  },
  {
    "id": "7389275241",
    "type": "CreateEvent",
    "actor": {
      "id": 21254319,
      "login": "ytyaru0",
      "display_login": "ytyaru0",
      "gravatar_id": "",
      "url": "https://api.github.com/users/ytyaru0",
      "avatar_url": "https://avatars.githubusercontent.com/u/21254319?"
    },
    "repo": {
      "id": 125483162,
      "name": "ytyaru0/Shell.Github.Commiter.20180316160244",
      "url": "https://api.github.com/repos/ytyaru0/Shell.Github.Commiter.20180316160244"
    },
    "payload": {
      "ref": null,
      "ref_type": "repository",
      "master_branch": "master",
      "description": null,
      "pusher_type": "user"
    },
    "public": true,
    "created_at": "2018-03-16T07:59:05Z"
  }
]
```



## Commits

コミットの内容が欲しい。

いつ、何をしたか、どのくらい。（概要の把握、定量化による集計、コード確認。）

* git log
    * commit
        * date
        * message
        * sha
        * `2 files changed, 45 insertions(+), 9 deletions(-)`
            * Filename
                * line num

* commit message
* commit size
    * `Showing  1 changed file  with 3 additions and 14 deletions.`
        * ファイル数
            * 行数
                * Byte数
* commit content
    * diff


GET /repos/:owner/:repo/git/commits/:sha
https://api.github.com/repos/ytyaru0/Shell.Github.Commiter.20180316160244/git/commits/6f2e7b3285a77351c2aef063b2886c1a78c2e0b4
"message": "パスワード取得関数の集約",

```json
{
  "sha": "6f2e7b3285a77351c2aef063b2886c1a78c2e0b4",
  "url": "https://api.github.com/repos/ytyaru0/Shell.Github.Commiter.20180316160244/git/commits/6f2e7b3285a77351c2aef063b2886c1a78c2e0b4",
  "html_url": "https://github.com/ytyaru0/Shell.Github.Commiter.20180316160244/commit/6f2e7b3285a77351c2aef063b2886c1a78c2e0b4",
  "author": {
    "name": "ytyaru0",
    "email": "ytyaru0@outlook.jp",
    "date": "2018-03-16T11:13:26Z"
  },
  "committer": {
    "name": "ytyaru0",
    "email": "ytyaru0@outlook.jp",
    "date": "2018-03-16T11:13:26Z"
  },
  "tree": {
    "sha": "e3323c49808ef35c0b255224f1701fffffddd55e",
    "url": "https://api.github.com/repos/ytyaru0/Shell.Github.Commiter.20180316160244/git/trees/e3323c49808ef35c0b255224f1701fffffddd55e"
  },
  "message": "パスワード取得関数の集約",
  "parents": [
    {
      "sha": "33cb894bb5c370e47cd053f5f80430cc4d4d1744",
      "url": "https://api.github.com/repos/ytyaru0/Shell.Github.Commiter.20180316160244/git/commits/33cb894bb5c370e47cd053f5f80430cc4d4d1744",
      "html_url": "https://github.com/ytyaru0/Shell.Github.Commiter.20180316160244/commit/33cb894bb5c370e47cd053f5f80430cc4d4d1744"
    }
  ],
  "verification": {
    "verified": false,
    "reason": "unsigned",
    "signature": null,
    "payload": null
  }
}
```

## Tree

ファイル全体の取得っぽい。

GET /repos/:owner/:repo/git/trees/:sha



https://api.github.com/repos/ytyaru0/Shell.Github.Commiter.20180316160244/git/trees/e3323c49808ef35c0b255224f1701fffffddd55e


"message": "パスワード取得関数の集約",

```json
{
  "sha": "e3323c49808ef35c0b255224f1701fffffddd55e",
  "url": "https://api.github.com/repos/ytyaru0/Shell.Github.Commiter.20180316160244/git/trees/e3323c49808ef35c0b255224f1701fffffddd55e",
  "tree": [
    {
      "path": ".gitignore",
      "mode": "100644",
      "type": "blob",
      "sha": "d14b76a2b0b7f91ecbba8871315f15222f266d93",
      "size": 243,
      "url": "https://api.github.com/repos/ytyaru0/Shell.Github.Commiter.20180316160244/git/blobs/d14b76a2b0b7f91ecbba8871315f15222f266d93"
    },
    {
      "path": "LICENSE.txt",
      "mode": "100644",
      "type": "blob",
      "sha": "72cdf27084d37498c0ff4fbd8c3cd3c7cea2e765",
      "size": 6671,
      "url": "https://api.github.com/repos/ytyaru0/Shell.Github.Commiter.20180316160244/git/blobs/72cdf27084d37498c0ff4fbd8c3cd3c7cea2e765"
    },
    {
      "path": "ReadMe.md",
      "mode": "100644",
      "type": "blob",
      "sha": "877cabed4515119cc63c18b8e390aa547843d5a8",
      "size": 2775,
      "url": "https://api.github.com/repos/ytyaru0/Shell.Github.Commiter.20180316160244/git/blobs/877cabed4515119cc63c18b8e390aa547843d5a8"
    },
    {
      "path": "src",
      "mode": "040000",
      "type": "tree",
      "sha": "c8bc02f1090f8baa5b086ef9e80f1f0dca77d524",
      "url": "https://api.github.com/repos/ytyaru0/Shell.Github.Commiter.20180316160244/git/trees/c8bc02f1090f8baa5b086ef9e80f1f0dca77d524"
    }
  ],
  "truncated": false
}
```













自分の成果の概要を取得したい。（commit単位）

```
$ git log --shortstat 
commit 6f2e7b3285a77351c2aef063b2886c1a78c2e0b4
Author: ytyaru0 <ytyaru0@outlook.jp>
Date:   Fri Mar 16 20:13:26 2018 +0900

    パスワード取得関数の集約

 1 file changed, 9 insertions(+), 11 deletions(-)

commit 33cb894bb5c370e47cd053f5f80430cc4d4d1744
Author: ytyaru0 <ytyaru0@outlook.jp>
Date:   Fri Mar 16 19:57:18 2018 +0900

    exit 1処理を一行で書いた

 1 file changed, 3 insertions(+), 14 deletions(-)

commit f0626315202193accfbb74968b2a41a38bf3d375
Author: ytyaru0 <ytyaru0@outlook.jp>
Date:   Fri Mar 16 19:49:44 2018 +0900

    select, for, ifを一行で書いた

 1 file changed, 1 insertion(+), 6 deletions(-)
```

* date
* sha
* message
* file change num
    * insert
    * delete

```
insert: 416
delete:  89
files:   16
commits: 10
date   : 3 day  2000-01-01..2000-01-04
```

```sh
$ git diff {old commit sha} {new commit sha}
```

以下だとファイル単位で変更量がわかる。拡張子によりプログラミング言語が特定できる。

```sh
$ git log --stat
commit f132792d261ea41134501b5696a0e4ceaf617657
Author: ytyaru0 <ytyaru0@outlook.jp>
Date:   Fri Mar 16 17:00:13 2018 +0900

    初回コミット

 .gitignore  |  20 +++++++++++
 LICENSE.txt | 116 ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
 ReadMe.md   |  65 ++++++++++++++++++++++++++++++++++
 src/push.sh |  97 ++++++++++++++++++++++++++++++++++++++++++++++++++
 4 files changed, 298 insertions(+)
```


git log --oneline 
git log --short 
git log --medium 
git log --full 
git log --fuller 
git log --oneline 
git log --oneline 

git log --help > git_log_help.txt

format:"%H\n%h%T%t"

git log --pretty=format:"{%nCommitHash:%H,%nTreeHash:%T%n}"

%H|CommitHash
%T|TreeHash
%ai|auther date 2018-03-16 20:13:26 +0900
%ci|commiter date 2018-03-16 20:13:26 +0900
%s|CommitMessage

format では insertion などの行数が取得できない。

```sh
$ git log --numstat
commit 6f2e7b3285a77351c2aef063b2886c1a78c2e0b4
Author: ytyaru0 <ytyaru0@outlook.jp>
Date:   Fri Mar 16 20:13:26 2018 +0900

    パスワード取得関数の集約

9       11      src/push.sh

commit 33cb894bb5c370e47cd053f5f80430cc4d4d1744
Author: ytyaru0 <ytyaru0@outlook.jp>
Date:   Fri Mar 16 19:57:18 2018 +0900

    exit 1処理を一行で書いた

3       14      src/push.sh
```

`insertion, deletion, filename` の順に取得できる。


       --date=(relative|local|default|iso|rfc|short|raw)
--date

```sh
$ git log --numstat --date=iso --author='ytyaru0'

commit 088476baccfa485e2a9fff92048ad7b6b8bf12fe
Author: ytyaru0 <ytyaru0@outlook.jp>
Date:   2018-03-16 17:45:16 +0900

    ユーザ選択を追加

12      2       ReadMe.md
33      7       src/push.sh

commit f132792d261ea41134501b5696a0e4ceaf617657
Author: ytyaru0 <ytyaru0@outlook.jp>
Date:   2018-03-16 17:00:13 +0900

    初回コミット

20      0       .gitignore
116     0       LICENSE.txt
65      0       ReadMe.md
97      0       src/push.sh
```

拡張子ごとに集計する。

ファイル名は残す必要ない。それなら commit sha で変更箇所ごと見せたほうが意味がある。

.sh| 50,0
.md| 30,7
.py|  9,2

CommitId
FileType
Insertion
Deletion

いつ、何の言語を、何行、実装（削除）したか判明する。

特殊なファイルもある。

.gitignore|ファイル名がない隠しファイル。設定ファイル。ツールごとに存在するため膨大。集計外か単一集計か悩む。
LICENSE.txt|ライセンス。拡張子に無関係で"LICENSE"として集計すべきか
ReadMe.md|README。拡張子に無関係で"README"として集計すべきか
a.tsv|tsv,json,xml,png,zip,などプログラミング言語以外の拡張子。

集計したいのはプログラミング言語。.html, .css, あたりが微妙。

対象言語

https://github.com/ytyaru0/GitHub.Uploader.Pi3.Https.201803020700/blob/master/src/database/init/Languages/insert/py/LanguageSource.py

GitHubが認識する言語一覧。

https://raw.githubusercontent.com/github/linguist/master/lib/linguist/languages.yml

type: data, markup, programming

タイプ別に集計できる。

* programming
    * .py: 000 line
* markup
    * .html: 000 line
* data
    * .csv: 000 line
* prose
    * .md: 000 line







# こういうツールをいつか作りたい

## すべてのデータを取得する

* ユーザを指定する
    * 全リポジトリを git clone
        * `git log` で commit データ取得
            * DB登録
        * リポジトリ削除して次のリポジトリへ

## 見える化

GithubのContribution activityみたいなやつ。

日々の活動を俯瞰でき、コードにアクセスできる。

## バックアップ

* ユーザを指定する
    * 全リポジトリのzipをダウンロード
    * 全リポジトリを他のサービスにuploadする

## 拡散

* Mastodon
* Hatena Blog

