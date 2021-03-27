# -*- coding: utf-8 -*-
# ライブラリの読み込み
import os
import os.path as osp
import dotenv
import time
from slacker import Slacker
from utils.init_dotenv import input_env_vals


def init_env():
    # .env ファイル → 環境変数 （読み込む）
    dotenv_path = osp.join(osp.dirname(__file__), '.env')
    if not osp.isfile(dotenv_path):
        # .env ファイルがないので、初期設定する。
        input_env_vals(dotenv_path)
    dotenv.load_dotenv(dotenv_path)

    return os.environ['BOT_API_TOKEN']


def main():
    # ボットの起動
    from slackbot.bot import Bot
    bot = Bot()
    print("\n[Info] bot の呼び出しに成功しました！ 起動します...")
    bot.run()


if __name__ == "__main__":
    API_TOKEN = init_env()
    slack = Slacker(API_TOKEN)

    time.sleep(1) # 'Start request repeated too quickly.' についての対策
    slack.chat.post_message("#bot-テスト場_public", "おはよう〜", as_user=True) # 起動時にメッセージを投稿
    
    main()
