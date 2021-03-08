# サンプルコード説明
2019.01.30 miyabikno

## 動作環境
    - Windows/Mac/その他UNIX系OS
    - Python3

## ファイルの内容
- Slackボットのコード
    ```
    start_slackbot
    ┣　bot.py
    ┣　slackbot_settings.py
    ┗　botmodules
        ┣　__init__.py
        ┗　conversation.py
    ```
- README.txt(このファイル)
    - Pythonで作るSlackbotの基本構成のサンプルコードです。

## 準備
1. Hubotの作成とAPIトークンを取得
    取得方法はこちらの記事で説明しています。
    https://se.miyabikno-jobs.com/slackbot-api-token/
1. 「bot.py」と「salackbot_settings.py」を同じフォルダに置きます。
1. pip install
    - 基本的には、`slackbot` のみでOK。
    - それ以外のライブラリも使っているので、以下を実行する。
        ```
        pip install -r requirements.txt
        ```

## デプロイ
4. 起動方法
    1. Pythonを実行します。
        ```
        python bot.py
        ```
        - 初回起動時は、`.env` ファイルを作る必要がある。
        - 以下のようなメッセージが出るので、hubot の APIキーを入力する。
            ```
            [Info] .env ファイルが見つかりませんでした。
            [Info] 初期設定を実行します。
            [Q] BOT_API_TOKEN を入力してください。
            >> 
            ```

5. 終了
    - 「CTRL + C」で中断できる。

6. Slackで使う
    1. ボットを使いたいチャンネルにボットを招待します。
        -  (@huubot)は作成したボット名に置き換えてください。
        ```
        /invite @hubot
        ```
    3. 実行例
        「こんにちは」(メンションあり)と「もうかりまっか」(メンションなし)の2種類の単語を使用できます。
        ```
        @hubot こんにちは
        → こんにちは！

        もうかりまっか
        → ぼちぼちでんな
        ```
7. モジュールの追加
    1. 会話の追加
        「botmodules/conversation.py」に追記することで追加できます。
        (function名は何でもOK。同じ関数があっても動作します)
        ```
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
        ```

    2. モジュールを追加する
        会話以外のモジュールを実装したい場合は会話の種類によってモジュールを分けたい場合はモジュールの追加を行います。
      1. 「botmodules」直下にモジュールを格納します。

      2. 「slackbot_settings.py」の「PLUGINS」にモジュール名を追記します。
            ```
            PLUGINS = [
                        'slackbot.plugins',
                        'botmodules.conversation',
                        'botmodules.new_module_name'
                        # ここにカンマ区切りでプラグインを追加していくことで拡張できます。
            ]
            ```
    3. 新しいディレクトリを追加する
        1. ディレクトリを追加してその直下に作成したモジュールファイルを格納します。

        2. 作成したディレクトリに「__init__.py」を追加します。(ファイルの中身は空で大丈夫です)

        3. 「slackbot_settings.py」の「PLUGINS」にモジュール名を追記します。
            ```
            PLUGINS = [
                        'slackbot.plugins',
                        'botmodules.conversation',
                        'new_modules.new_module_name'
                        # ここにカンマ区切りでプラグインを追加していくことで拡張できます。
            ]
            ```


◆注意事項
当ドキュメントの文章を無断転載することを禁止します。

有料    - 無料問わずこのディレクトリに格納されているコードを改変なしに再配布することを禁止します。
何らかの改変を加えたものを再配布することは問題ありません。許可等も不要です。
