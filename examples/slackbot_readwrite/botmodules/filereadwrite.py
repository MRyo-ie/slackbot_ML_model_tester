import codecs
import csv
from slackbot.bot import respond_to


class FileReadWrite:

    # ファイルを読み込むメソッド
    def file_read(self, path):
        try:
            # ファイルを開く
            target_file = codecs.open(path, "r", "utf_8")
            # ファイルを読み込む
            text = target_file.read()
            target_file.close()
        except:
            # エラーが出た時の例外処理
            text = "ng"

        return text

    # ファイルを書き込むメソッド
    def file_write(self, path, text, mode="a"):
        try:
            target_file = codecs.open(path, mode, "utf_8")
            target_file.write(text)
            result = "ok"
            target_file.close()
        except:
            # エラーが出た時の例外処理
            result = "ng"
        return result

    def csv_read(self, path):
        try:
            target_file = open(path, encoding="utf_8")
            text_lines = csv.reader(target_file)
            text = list(text_lines)
            target_file.close()
        except:
            text = "ng"

        return text

    def csv_write(self, path, text, mode="w"):
        try:
            target_file = open(path, mode, encoding="utf_8")
            dataWriter = csv.writer(target_file, lineterminator='\n')
            dataWriter.writerows(text)
            result = "ok"
            target_file.close()
        except:
            result = "ng"

        return result

    def sort_priority(self, target_list):
        target_list.sort(key=lambda x: x[2])
        return target_list


def main():
    c = FileReadWrite()
#    answer =  c.file_write("./test1.txt", "かきくけこ\n")
#    print(answer)
#    text = c.file_read("./test1.txt")
#    print(text)
#    texts = [[1,"かきくけこ"],[2,"さしすせそ"]]

#    answer = c.csv_write("./test2.csv", texts, "a")
#    print(answer)
    texts = c.csv_read("./test2.csv")

    print(texts)


if __name__ == "__main__":
    main()


@respond_to('^ファイル書き込みテスト$')
def write_test(message):
    # クラスのインスタンスを生成
    f = FileReadWrite()
    # ファイルに書き込む
    action = f.file_write("./test1.txt", "あいうえお\n")
    # 結果をリアクションする
    message.react(action)


@respond_to('^ファイル読み込みテスト$')
def read_test(message):
    # クラスのインスタンスを生成
    f = FileReadWrite()
    # ファイルからテキストを読み込む
    text = f.file_read("./test1.txt")

    # 失敗した時はNGをリアクションで返す
    if text == "ng":
        message.react(text)
    else:
        # 成功した場合はテキストを返す
        message.send(text)
