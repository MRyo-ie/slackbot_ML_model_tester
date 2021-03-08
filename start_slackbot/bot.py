# ライブラリの読み込み
import os.path as osp
import dotenv
from utils.init_dotenv import input_env_vals


def main():
    # .env ファイル → 環境変数 （読み込む）
    dotenv_path = osp.join(osp.dirname(__file__), '.env')
    if not osp.isfile(dotenv_path):
        # .env ファイルがないので、初期設定する。
        input_env_vals(dotenv_path)
    dotenv.load_dotenv(dotenv_path)

    # ボットの起動
    from slackbot.bot import Bot
    bot = Bot()
    print("\n[Info] bot の呼び出しに成功しました！ 起動します...")
    bot.run()


if __name__ == "__main__":
    main()
