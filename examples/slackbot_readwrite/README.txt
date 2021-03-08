サンプルコード説明

2019.01.30 miyabikno

1.動作環境
・Windows/Mac/その他UNIX系OS
・Python3

2.ファイルの内容
・Slackボットのコード

start_slackbot
┣　bot.py
┣　slackbot_settings.py
┗　botmodules
  ┣　__init__.py
  ┣　filereadwrite.py
  ┗　conversation.py

・README.txt(このファイル)

Pythonで作るSlackbotの基本構成のサンプルコードです。

3.準備
3.1 Hubotの作成とAPIトークンを取得
取得方法はこちらの記事で説明しています。
https://se.miyabikno-jobs.com/slackbot-api-token/
3.2 ターミナルで以下のコマンドを実行
>pip install slackbot

4.起動方法
4.1ターミナルを開いて環境変数に取得したトークンを設定します。(Macの例)
>export BOT_API_TOKEN="xxxxxxxxxxxxxxxxxxx"

4.2Pythonを実行します。
>python bot.py

5.終了
「CTRL + C」で中断してください。

6.Slackで使う
6.1 ボットを使いたいチャンネルにボットを招待します。(@huubot)は作成したボット名に置き換えてください。
/invite @hubot

6.2 実行例
書き込みテストと読み込みテストを行えます。


@hubot 書き込みテスト
→成功するとOKリアクションを返します。

@hubot 読み込みテスト
→成功するとファイルテキストを返します。

7.モジュールの追加
7.1 会話の追加
「botmodules/conversation.py」に追記することで追加できます。
(function名は何でもOK。同じ関数があっても動作します)

# メンションあり
@respond_to('こんにちは')
def function(message):
    # メンションあり応答
    message.reply('こんにちは!')
    # メンションなし応答
    # message.send('こんにちは!')
    # リアクション
    # message.react('+1')

# メンションなし
@listen_to('こんにちは')
def function(message):
    message.reply('こんにちは!')

7.2 書き込みモジュール・読み込みモジュールの使い方


7.2.1 書き込み

◆記述例

# クラスのインスタンスを生成
f = FileReadWrite()

# 出力するテキスト。改行コードが必要です。
text = 'abcdef' + '\n'

# ファイルに書き込む。リターン値は'ok'または'ng'です。
action = f.file_write("sample.txt", text)


# リアクションを返します。
message.react(action)

7.2.2 読み込み

◆記述例

# クラスのインスタンスを生成
f = FileReadWrite()
# ファイルからテキストを読み込む
text = f.file_read("sample.txt")

# 失敗した時はNGをリアクションで返す
if text == "ng":
   message.react(text)
else:
   # 成功した場合はテキストを返す
   message.send(text)


7.3 モジュールを追加する
会話以外のモジュールを実装したい場合は会話の種類によってモジュールを分けたい場合はモジュールの追加を行います。

7.3.1 「botmodules」直下にモジュールを格納します。

7.3.2 「slackbot_settings.py」の「PLUGINS」にモジュール名を追記します。
PLUGINS = [
            'slackbot.plugins',
            'botmodules.conversation',
            'botmodules.filereadwrite',
            'botmodules.new_module_name'
            # ここにカンマ区切りでプラグインを追加していくことで拡張できます。
]

7.4 新しいディレクトリを追加する
7.4.1 ディレクトリを追加してその直下に作成したモジュールファイルを格納します。

7.4.2 作成したディレクトリに「__init__.py」を追加します。(ファイルの中身は空で大丈夫です)


7.4.3 「slackbot_settings.py」の「PLUGINS」にモジュール名を追記します。
PLUGINS = [
            'slackbot.plugins',
            'botmodules.conversation',
            'botmodules.filereadwrite',
            'new_modules.new_module_name'
            # ここにカンマ区切りでプラグインを追加していくことで拡張できます。
]


◆注意事項
当ドキュメントの文章を無断転載することを禁止します。

有料・無料問わずこのディレクトリに格納されているコードを改変なしに再配布することを禁止します。
何らかの改変を加えたものを再配布することは問題ありません。許可等も不要です。
