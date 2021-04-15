import setting
import tweepy
from time import sleep
import numpy as np
import matplotlib.pyplot as plt
import datetime

API_KEY = setting.API_KEY
API_SECRET = setting.API_SECRET
ACCESS_TOKEN = setting.ACCESS_TOKEN
ACCESS_TOKEN_SECRET = setting.ACCESS_TOKEN_SECRET

auth = tweepy.OAuthHandler(API_KEY, API_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)

class Hololive():
    def __init__(self,name,id,art_tag,live_tag,cut_tag,fan_name) -> None:
        self.name = name
        self.id = id
        self.art_tag = art_tag
        self.live_tag = live_tag
        self.cut_tag = cut_tag
        self.fan_name = fan_name

    def WriteTweet_id(self):
        """
        ユーザーのIDを参照してツイートを取得します
        """

        tweets = api.user_timeline(self.id, count=100, page=1)
        count = 0

        date = datetime.datetime.now().strftime('%Y:%m:%d: %H:%M:%S')
        with open(f"./TweetData/{self.id}-{date}.txt","w") as f:
        # with open("board.txt", 'w') as f:
            f.write(f"### @{self.id} さんのツイート ###\n")

            for tweet in tweets:
                count += 1                                          # ツイート数を計算
                f.write(f"\nTweetCount : {count}")                  # ツイート数
                f.write(f"\nTweetID    : {tweet.id}")                   # tweetのID
                f.write(f"\nUserID     : @{tweet.user.screen_name}")    # ユーザー名
                f.write(f"\nDate       : {tweet.created_at}")           # 呟いた日時
                f.write(f"\nRT         : {tweet.retweet_count}")        # ツイートのリツイート数
                f.write(f"\nFav        : {tweet.favorite_count}")       # ツイートのいいね数
                f.write(f"\n{tweet.text}\n")                            # ツイート内容
                f.write('#'*60)

        print(f"合計 {count}件 の処理が完了しました")

Aqua   = Hololive("湊あくあ","minatoaqua","#あくあーと","#湊あくあ生放送","あくあクルー","#切り抜きあくたん")

Marine = Hololive("宝鐘マリン","houshoumarine","#マリンのお宝","#マリン航海記","宝鐘の一味","#わかるマリン")
Pekora = Hololive("兎田ぺこら","usadapekora","#ぺこらーと","#ぺこらいぶ","野うさぎ","#ひとくちぺこら")
Flare  = Hololive("不知火フレア","shiranuiflare","#しらぬえ","#フレアストリーム","エルフレンド","#切りぬい")
Noel   = Hololive("白銀ノエル","shiroganenoel","#ノエラート","#ノエルーム","白銀聖騎士団","#クリ抜き太郎")
Rushia = Hololive("潤羽るしあ","uruharushia","#絵クロマンサー","#るしあらいぶ","ふぁんでっど","#きるしあ")

def main():
    Rushia.WriteTweet_id()
    Aqua.WriteTweet_id()

    


if __name__ == "__main__":
    main()

    # print(Rushia.name, Rushia.id, Rushia.art_tag, Rushia.live_tag, Rushia.fan_name, Rushia.cut_tag)
    # print(Aqua.name, Aqua.id, Aqua.art_tag, Aqua.live_tag, Aqua.fan_name, Aqua.cut_tag)
    # Miko = Hololive("さくらみこ"," sakuramiko35","#miko_art","#みこなま","みこぴー","#ミコミコ動画")
    # print(Miko.name, Miko.id, Miko.art_tag, Miko.live_tag, Miko.fan_name, Miko.cut_tag)