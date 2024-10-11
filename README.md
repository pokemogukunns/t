# YouTubeダウンローダー
YouTubeからのビデオとオーディオのダウンローダー

- これは、さまざまな解像度（360p、480p、720p）のビデオ、mp3形式のオーディオをダウンロードできるYouTubeのビデオおよびオーディオダウンローダーです。

- このプログラムには、ターミナルから直接ビデオやオーディオをダウンロードできるように、使いやすいコマンドラインインターフェイスがあります。

## インストール:
- このリポジトリを好きな場所に複製する
- ターミナルを開き、「youtube-downloader」ディレクトリに移動します。
- システムサイトパッケージを有効にして仮想環境を作成する
- 必要なすべてのパッケージをrequirements.txtから作成した仮想環境にインストールします。
```
pip install -r requirements.txt
```


- ボーナス: このスクリプトを実行するエイリアスを作成し、設定ファイルを変更することで「ydm」（YouTubeダウンロードマネージャー）のような派手な名前を付けることができます。 <a href="https://askubuntu.com/questions/17536/how-do-i-create-a-permanent-bash-alias"> もっと読む </a>

- スクリプトのエイリアスを作成するには、設定ファイルの最後に次の行を追加します（実際のスクリプトを実行する前に、スクリプトの仮想環境をアクティブにするコマンドを追加することを忘れないでください）
```
alias ydm="source /path/to/youtube-downloader/venv-name/bin/activate; python3 /path/to/youtube-downloader/main.py"
```
スクリプトのエイリアスを作成した後、次のようにダウンローダーを使用できます。
```
ydm -u URL
```


## 使う:
最高解像度のビデオをダウンロード、デフォルトは720p
```
$ python3 main.py -u URL
```
オーディオのみをダウンロードする
```
$ python3 main.py -a -u URL
```
クリップボードからURLを取得し、ビデオをダウンロードする
```
$ python3 main.py -c
```
クリップボードからURLを取得し、オーディオのみをダウンロードします。
```
$ python3 main.py -a -c
```
クリップボードからURLを取得し、480p解像度のビデオをダウンロードします。
```
$ python3 main.py -c -r 480p
```

ありがとうございました。
