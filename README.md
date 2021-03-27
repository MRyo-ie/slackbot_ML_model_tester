# slackbot ML Model tester
- 最もシンプルな形の、Slackbotのサンプルコード。
- 参考資料
  - [SlackbotをPythonで作成しよう](https://miyabikno-jobs.com/entrance-labotlatori/ )

## Install
### Slackbot
1. SlackのAPIトークンの取得して、.emv ファイルに保存する。
    ```
    cd start_slackbot
    echo BOT_API_TOKEN = "【SlackのAPIトークン】" > .env
    ```

2. Slackbotライブラリをインストールする。  
    ``
    pip install  -r requirements.txt
    ``

3. bot.pyを実行してBotを起動します。
    ```
    python bot.py
    ```
    - 実行すると、Slack上でbotが起動するはず。
    - systemd などで自動起動がオススメ。


### DeepLearning モデル
1. fashion_mnist (keras 画像分類チュートリアルモデル)
    1. 学習
        ```
        cd ./start_slackbot/botmodules/fashion_mnist
        pip install  -r requirements.txt
        python train.py 
        ```
    2. テストデータを用意
        ```
        cd ../../
        python botmodules/fashion_mnist/predict.py
        ```
        - `botmodules/fashion_mnist/test_imgs/` に10枚ほど、
            テスト用の画像が生成されているはず。
    3. Slackbot を起動
        ```
        python bot.py
        ```
    4. slack で、bot に画像を送りつける！
        - ![](./README/fashion_mnist.png)

