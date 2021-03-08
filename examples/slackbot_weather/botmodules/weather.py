import json
import requests
from slackbot.bot import respond_to


def get_weather(city_number):
    # 天気のURL設定 city_numberには都市の番号を指定
    url = "http://weather.livedoor.com/forecast/webservice/json/v1?city=%s" % city_number

    # URLを取得
    response = requests.get(url)
    # URL取得結果のチェック
    response.raise_for_status()
    # 天気データを読み込む
    weather_data = json.loads(response.text)

    return(weather_data)


# テストコード
def main():
    w = get_weather(130010)
    t = w['forecasts'][0]

    print(t['dateLabel']) # 今日
    print(t['date']) # 日付
    print(t['telop']) # 天気


if __name__ == "__main__":
    main()


@respond_to('^(今日|明日|明後日)の天気$')
def whether_1(message, group):
    # 絵文字リストを作る
    dic_weather = {
        '晴れ': 'sunny',
        '曇り': 'cloud',
        '雨': 'rain_cloud',
        '雪': 'snow_cloud',
        '曇時々晴': 'barely_sunny',
    }

    dic_date = {
        '今日': 0,
        '明日': 1,
    }

    w = get_weather(130010)
    t = w['forecasts'][dic_date[group]]
    telop = t['telop']

    # 辞書にない天気が来たら絵文字に空文字を設定する
    if telop in dic_weather:
        emoji = ':' + dic_weather[telop] + ':'
    else:
        emoji = ""

    message.reply('%sの天気は%sです%s' % (group, telop, emoji))
