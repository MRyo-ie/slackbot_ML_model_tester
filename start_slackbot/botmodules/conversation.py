
import json
import os
import requests
import shutil
from slackbot.bot import respond_to
from slackbot.bot import listen_to
from slackbot.bot import default_reply
import slackbot_settings

from .fashion_mnist.predict import predict_fashion

# メンションあり応答
@respond_to('こんにちは')
def greeting_mention(message):
    # メンションして応答
    message.reply('こんにちは!')


# メンションなし応答
@listen_to('もうかりまっか')
def greeting_listen(message):
    # メンションなしで応答
    message.send('ぼちぼちでんな')


@listen_to("(.*)")
def img(message, params):
    if 'files' in message.body:
        # print(message.body['files'])
        file_0 = message.body['files'][0]
        url = file_0['url_private']
        flag = file_0['filetype']
        tmpfile_path = "./tmp." + flag

        token = os.environ.get("BOT_API_TOKEN")
        rst = requests.get(url, headers={'Authorization': 'Bearer %s' % token}, stream=True)
        fo = open(tmpfile_path, "wb")
        shutil.copyfileobj(rst.raw, fo)
        fo.close()

        # message.send(model.get_responce())
        # message.send("画像を受け取りました！")
        # message.send(json.dumps(message.body['files']))

        message.send(predict_fashion(tmpfile_path))
        


@default_reply
def my_default_handler(message):
    # デフォルトリプライをsendに変更する
    message.send(slackbot_settings.DEFAULT_REPLY)
