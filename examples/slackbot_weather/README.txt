サンプルコード説明

2019.01.31 miyabikno

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
  ┣　weather.py
  ┗　conversation.py

・README.txt(このファイル)

Pythonで作るSlackbotの基本構成のサンプルコードです。

3.準備
3.1 Hubotの作成とAPIトークンを取得
取得方法はこちらの記事で説明しています。
https://se.miyabikno-jobs.com/slackbot-api-token/
3.2 ターミナルで以下のコマンドを実行します。
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
今日の天気または明日の天気を返します。

@hubot 今日の天気
→今日の天気は晴れです

@hubot 明日の天気
→明日の天気は雨です

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


7.2 モジュールを追加する
会話以外のモジュールを実装したい場合は会話の種類によってモジュールを分けたい場合はモジュールの追加を行います。

7.2.1 「botmodules」直下にモジュールを格納します。

7.2.2 「slackbot_settings.py」の「PLUGINS」にモジュール名を追記します。
PLUGINS = [
            'slackbot.plugins',
            'botmodules.conversation',
            'botmodules.weather',
            'botmodules.new_module_name'
            # ここにカンマ区切りでプラグインを追加していくことで拡張できます。
]

7.3 新しいディレクトリを追加する
7.3.1 ディレクトリを追加してその直下に作成したモジュールファイルを格納します。

7.3.2 作成したディレクトリに「__init__.py」を追加します。(ファイルの中身は空で大丈夫です)


7.3.3 「slackbot_settings.py」の「PLUGINS」にモジュール名を追記します。
PLUGINS = [
            'slackbot.plugins',
            'botmodules.conversation',
            'botmodules.weather',
            'new_modules.new_module_name'
            # ここにカンマ区切りでプラグインを追加していくことで拡張できます。
]


◆注意事項
当ドキュメントの文章を無断転載することを禁止します。

有料・無料問わずこのディレクトリに格納されているコードを改変なしに再配布することを禁止します。
何らかの改変を加えたものを再配布することは問題ありません。許可等も不要です。
