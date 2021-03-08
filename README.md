# slackbot-py
- 最もシンプルな形の、Slackbotのサンプルコード。
- 参考資料
  - [SlackbotをPythonで作成しよう](https://miyabikno-jobs.com/entrance-labotlatori/ )

## 使い方
1. SlackのAPIトークンの取得して、.emv ファイルに保存する。
    ```
    cd start_slackbot
    echo BOT_API_TOKEN = "【SlackのAPIトークン】" > .env
    ```

2. Slackbotライブラリをインストールします。  
    ``
    pip install  slackbot python-dotenv
    ``

3. bot.pyを実行してBotを起動します。
    ```
    python bot.py
    ```
    - 実行すると、Slack上でbotが起動するはず。
