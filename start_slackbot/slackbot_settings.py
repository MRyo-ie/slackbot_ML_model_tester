# ライブラリのインポート
import os


API_TOKEN = os.environ['BOT_API_TOKEN']

# デフォルトの応答
DEFAULT_REPLY = "すみません。よくわかりません"

PLUGINS = [
    'slackbot.plugins',
    'botmodules.conversation',
    # ここにカンマ区切りでプラグインを追加していくことで拡張できます。
]
