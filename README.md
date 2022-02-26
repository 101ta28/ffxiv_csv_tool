# FFXIV_CSV_TOOL

FF14の公式プレイヤーズサイトの「[The Lodestone](https://jp.finalfantasyxiv.com/lodestone/)」のフレンドリストやFCメンバー一覧をCSVに書き出すプログラムです。

## 必要パッケージ

```
beautifulsoup4==4.10.0
certifi==2021.10.8
charset-normalizer==2.0.12
idna==3.3
pkg_resources==0.0.0
requests==2.27.1
soupsieve==2.3.1
urllib3==1.26.8
```

上記のパッケージは
```bash
$ pip install -r requirements.txt
```
でインストールできます。

## 使用方法

```bash
$ git clone https://github.com/101ta28/ffxiv_csv_tool.git
$ cd ffxiv_csv_tool
$ python friend_csv.py
```

## ファイルについて
CSVファイルはプログラムの配置場所に保存されます。

フレンドリストのCSVファイル名は friend_list.csv

CSVフォーマットは以下の通りです。

| 名前 | ワールド名 | FC名 |
|:-----|:---------|:-----|

FCに所属していない場合は、「FC not joined」が書き込まれます。

---

FCメンバー一覧のCSVフォーマットは以下の通りです。

フレンドリストのCSVファイル名は [FC名].csv

(例: 「github」というFCのCSVファイル名は github.csv)

| 名前 | ランク |
|:-----|:---------|

---

## **注意**

スクレイピングのプログラムが元なので、大量に実行するとLodestoneのサーバーに負荷がかかります。

**短時間に大量に実行しないでください。**

あくまでも非公式のプログラムだということをご理解ください。
