# coding: UTF-8
import os
import os.path as osp
from dotenv import load_dotenv

def input_env_vals(dotenv_path):
    # .env ファイルがないので、初期設定する。
    print("[Info] .env ファイルが見つかりませんでした。")
    print("[Info] 初期設定を実行します。\n")
    env_dict = {}
    env_dict['BOT_API_TOKEN'] = input("[Q] BOT_API_TOKEN を入力してください。\n>> ")
    with open(dotenv_path, 'w') as envf:
        for k, v in env_dict.items():
            envf.write(f'{k} = "{v}"')

