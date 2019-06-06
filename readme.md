# 調査結果記載

## ツール作成
- Pythonでツール作成する
- ポイント：インストールするとき、環境変数追加のCheckBoxをチェックON
- VSCodeでツールのフォルダを開き、F5 押下でデバッグできる
> ただし、他ライブラリ利用する場合、開発環境でインストールが必要
- Pythonダウンロード/インストール：https://www.python.org/downloads/

## 利用するライブラリ/パッケージ
- 正規表現でマッチするため、「re」
- Excel操作用
  - [.xls]ファイル： xlutils(xlrd、xlwt): Excel2003
  - Excel2003 で列数は最大256、Table数は407個あり、上記NG (行数制限65536に達していない)
  - Excel2007 以降は256列の制限はなし（16384列まで追加可能）
  - [.xlsx]ファイル： openpyxl	=> 採用
- パッケージインストールでのポイント：cmdを管理者で実行し、pip install xxxxxx
    ```bat
    pip install openpyxl
    ```

## データ読み込み時のTXTファイルについて
- 必ず、「UTF-8 without Signature」で保存（でないと、UTF-8指定の読み込みでエラーになる）
- 「UTF-8 with Signature」で保存した場合、UTF-8指定の読み込みでエラーになるため、NG
- 読み込みファイル名などは、固定指定で、パラメータにしていない（run.bat でパラメータなし。可能と思いますが、一回だけ使うので）

## 出力
- テンプレート不要、直接出力
- データ書き込みだけ、Excel上スタイルまだ未設定

## 実行方法：cmdでも呼び出し可
- [run.bat] ファイルを作成し、以下に編集：
```bat
python xxxxx.py
pause
```
- batファイルをダブルクリックで出力処理を実行開始

## ツール構成
- Execute.py  
  メインファイル、処理の入口、提供されたtxtを読み込み、データ作成に用意しておく
- preparedata.py  
  出力対象レコードを定義  
  読み込んだデータを分析し（正式表現利用）、出力データを取りまとめる  
- writeexcel.py  
  出力データを受け渡し、excelに書き込んで出力する

- db-access-grep-result.txt  
  PHP上「$DB→」を使用するため、SVNのdevelop配下でGrepを行ったファイル
- table-name-list.txt  
  テーブル一覧の407件テーブル名