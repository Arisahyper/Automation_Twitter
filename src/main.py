import datetime
from time import sleep

import matplotlib.pyplot as plt
import numpy as np
import tweepy

import setting

import subprocess

API_KEY = setting.API_KEY
API_SECRET = setting.API_SECRET
ACCESS_TOKEN = setting.ACCESS_TOKEN
ACCESS_TOKEN_SECRET = setting.ACCESS_TOKEN_SECRET

auth = tweepy.OAuthHandler(API_KEY, API_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)

class User():
    """
    Timeline_favorite()
    Follow_by_query(query : str, count : int)
    Remove_of_unfollower(count : int)
    Writetweet_by_query(query : str, count : int)
    """
    def __init__(self,name,id) -> None:
        self.name = name
        self.id = id

    def Timeline_favorite(self):
        """
        自身のタイムラインの最新ツイートを40件取得しいいねをつけます
        """

        timeline = api.home_timeline(count=40)
        hit_count: int = 0

        for tweet in timeline:
            if not "@" in tweet.text[0]:
                tweet_id = tweet.id
                user_name = tweet.user.name
                user_id = tweet.user.screen_name
                text = tweet.text
                time = tweet.created_at

                print("#"*60 + "\n")
                print(f"TweetID：{tweet_id}")
                print(f"Name   ：{user_name}")
                print(f"ID     ：{user_id}")
                print(f"Time   ：{time}")
                print(f"\n【 本文 】\n{text}")

                try:
                    api.create_favorite(tweet_id)
                    print("\nこちらのツイートをいいねしました")
                    hit_count += 1
                except:
                    print("\nこちらのツイートは既にいいね済みです")

                print("\n" + "#"*60)
                sleep(5)
                subprocess.run('clear')

        print(f"合計 {hit_count}件 の処理を完了しました")
    
    def Timeline(self):
        timeline:list = api.home_timeline(count=1000)
        flg:bool = True

        while flg == True:
            for tweet in timeline:
                if not "@" in tweet.text[0]:
                    tweet_id = tweet.id
                    user_name = tweet.user.name
                    user_id = tweet.user.screen_name
                    text = tweet.text
                    time = tweet.created_at
                    
                    subprocess.run('clear')
                    print("#"*60 + "\n")
                    print(f"TweetID：{tweet_id}")
                    print(f"Name   ：{user_name}")
                    print(f"ID     ：{user_id}")
                    print(f"Time   ：{time}")
                    print(f"\n【 本文 】\n{text}")
                    print("#"*60 + "\n")

                    print("Next:Enter | Favorite:f | RT:r | End:e")
                    sleep(1)
                    a:str = input("command >> ")

                    try:
                        if a == "f":
                            api.create_favorite(tweet_id)
                            try:
                                print("このツイートにいいねしました")
                                sleep(2)
                                # subprocess.run('clear')
                            except:
                                print("既にいいね済みかいいねをつけることができませんでした")
                                sleep(2)
                                # subprocess.run('clear')

                        if a == "r":
                            api.retweet(tweet_id)
                            try:
                                print("このツイートをリツイートしました")
                                sleep(2)
                                # subprocess.run('clear')
                            except:
                                print("既にリツイート済みかリツイートをつけることができませんでした")
                                sleep(2)
                                # subprocess.run('clear')

                        if a == "e":
                            subprocess.run('clear')
                            print("終了するよ、またね")
                            sleep(2)
                            flg = False
                            break

                    except:
                        print("エラー")
                        sleep(2)
                        # subprocess.run('clear')
                    if flg == False:
                        break
                if flg == False:
                    break

    def Follow_by_query(self, query, count):
        """
        引数 queryに渡された値を参照して検索し count人のユーザーをフォローします
        """

        search_results = api.search(q=query + " -filter:retweets", count=count)
        now_count:int = 0

        for result in search_results:
            sleep(1)
            user_id = result.id
            user = result.user.name
            tweet = result.text
            user_name = result.user.screen_name
            time = result.created_at
            now_count += 1

            print(f"TweetID：{user_id}")
            print(f"Name   ：{user}")
            print(f"ID     ：{user_name}")
            print(f"Time   ：{time}")
            print(f"【 内容 】\n{tweet}")
            try:
                api.create_friendship(user_name)
                print("をフォローしました")
                print(f"現在の実行数  {now_count}件")
            except:
                print("既にフォローしています")

            print("#"*60)
            sleep(10)
        print(f"合計 {now_count}件 の処理を完了しました")

    def Remove_of_unfollower(self,count):
        """
        フォローバックされていないユーザーを count件リムーブします
        """
        unfollow_count: int = 0
        user_id = self.id
        followers_id = api.followers_ids(user_id)
        following_id = api.friends_ids(user_id)

        for follow in following_id:
            if follow not in followers_id:
                if unfollow_count < count:
                    username = api.get_user(follow).name
                    api.destroy_friendship(follow)
                    unfollow_count += 1

                    print(f"ユーザー名：{username}")
                    print(f"現在の解除数：{unfollow_count}件")
                    print("#"*60)
                    sleep(1)

        print(f"合計 {unfollow_count}件 の処理を完了しました")

    def Writetweet_by_query(self,query, count):  # 特定のワードを検索し書き込み
        """
        引数 queryに渡された値を参照して検索し テキストファイルを作成し count件書き込みます
        """
        tweets = api.search(q=query + " -filter:retweets", count=count)
        now_count: int = 0
        date:str = datetime.datetime.now().strftime('%Y:%m:%d: %H:%M:%S')
        
        with open(f"./Data/TweetData/{query}-{date}.txt", 'w') as f:
            for tweet in tweets:
                now_count += 1
                f.write(f"\nTweetCount : {now_count}")
                f.write(f"\nTweetID    : {tweet.id}")
                f.write(f"\nName       : {tweet.user.name}")
                f.write(f"\nUserID     : @{tweet.user.screen_name}")
                f.write(f"\nDate       : {tweet.created_at}")
                f.write(f"\nRT         : {tweet.retweet_count}")
                f.write(f"\nFav        : {tweet.favorite_count}")
                f.write(f"\n【 内容 】")
                f.write(f"\n{tweet.text}\n")
                f.write("#"*60)

        print(f"合計 {now_count}件 の処理が終了しました")


class Hololive(User):
    """
    WriteTweet_by_id()
    Follow_by_fanname(count:int)
    RT_by_arttag(count:int)
    create_user_graph(count:int)
    """
    def __init__(self, name, id, art_tag, live_tag, cut_tag, fan_name) -> None:
        super().__init__(name, id)
        self.art_tag = art_tag
        self.live_tag = live_tag
        self.cut_tag = cut_tag
        self.fan_name = fan_name

    def WriteTweet_by_id(self):
        """
        ユーザーのIDを参照し、そのツイートを取得しテキストファイルとして保存します。
        """

        tweets = api.user_timeline(self.id, count=100, page=1)
        count = 0

        date = datetime.datetime.now().strftime('%Y:%m:%d: %H:%M:%S')
        with open(f"./Data/TweetData/{self.id}-{date}.txt","w") as f:
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

    def Follow_by_fanname(self,count):
        """
        fan_nameを参照しツイートを取得しフォローします
        """

        query = self.fan_name

        search_results = api.search(q=query + " -filter:retweets", count=count)
        now_count = 0

        for result in search_results:
            sleep(1)
            user_id = result.id
            user = result.user.name
            tweet = result.text
            user_name = result.user.screen_name
            time = result.created_at
            now_count += 1

            print(f"TweetID ： {user_id}")
            print(f"Name    ： {user}")
            print(f"ID      ： {user_name}")
            print(f"Time    ： {time}")
            print(f"【 Tweet 】\n{tweet}")
            try:
                api.create_friendship(user_name)
                print(f"{user_name} をフォローしました")
                print(f"現在の実行数  {now_count}件")
            except:
                print("既にフォローしています")

            print("#"*60)
            sleep(10)
        print(f"合計 {now_count}件 の処理を完了しました")

    def RT_by_arttag(self, count):
        """
        arttagを参照しツイートをリツイートします
        """
        serch_results: list = api.search(q="#"+self.art_tag, count=1000)
        now_count: int = 0
        rtcount :int = 200

        for result in serch_results:
            RTcount = result.retweet_count
            if RTcount >= rtcount:
                if now_count < count:
                    # if not "RT @" in result.text[0:4]:
                    user_name = result.user.screen_name
                    user_id = result.id
                    user = result.user.name
                    tweet = result.text
                    time = result.created_at
                    print(f"UserID ：{user_name}")
                    print(f"TweetID：{user_id}")
                    print(f"Name   ：{user}")
                    print(f"RT     ：{RTcount}")
                    print(f"Time   ：{time}")
                    print(f"【ツイート内容】\n{tweet}")
                    try:
                        api.retweet(user_id)
                        print("リツイートしました")
                        now_count += 1
                        sleep(1)
                    except:
                        print("既にRT済みです")
                    print(f"現在のRT数：{now_count}")
                    print("#"*60)
                    sleep(1)
        print(f"合計 {now_count}件 の処理を完了しました")

    def create_user_graph(self,count):  # 特定のユーザーのツイート取得しツイート
        """
        ユーザーのidを参照しツーとを取得しRT数とFavorite数の動向グラフを作成します
        """
        
        Rtlist: list = []
        Favlist: list = []
        countlist: list = []
        now_count: int = 1

        account = self.id

        tweets = api.user_timeline(account, count=count, page=1)
        for tweet in tweets:
            if not "RT @" in tweet.text[0:4]:
                try: 
                    print(f"TweetID : {tweet.id}")                   # tweetのID
                    print(f"UserID  : @{tweet.user.screen_name}")    # ユーザー名
                    print(f"Date    : {tweet.created_at}")           # 呟いた日時
                    print("【内容】")
                    print(tweet.text)                           # ツイート内容
                    print(f"RT      : {tweet.retweet_count}")        # ツイートのリツイート数
                    print(f"Fav     : {tweet.favorite_count}")             # ツイートのいいね数
                    print(f"{str(now_count)}件目")                         # ツイート数
                    Rtlist.append(tweet.retweet_count)
                    Favlist.append(tweet.favorite_count)
                    countlist.append(now_count)
                    # print(f"{Rtlist}\n{Favlist}")
                    print("#" * 60)

                    now_count += 1   # ツイート数を計算
                except:
                    print("エラー")

        x:list = np.array(countlist)
        rt_y:list = np.array(Rtlist)
        fav_y:list = np.array(Favlist)


        fig = plt.figure(figsize=(10.0,6.0))
        plt.title(f"@{account} ReactionChart")
        plt.xlabel("Tweetcount")

        plt.plot(x, rt_y, label = "RT", color = "#00ff00")
        plt.plot(x, fav_y, label = "Favorite", color = "#f781bf")
        plt.legend()
        plt.grid(True)

        dt = datetime.datetime.now().strftime('%Y:%m:%d: %H:%M:%S')
        imgname = (f"./Data/ReactionChartData/{account}-{dt}-tweet.png")
        fig.savefig(imgname)

        # ツイート
        # api.update_with_media(status = (f"@ {account} ReactionChart"), filename = imgname)

    def favorite_by_fanname(self,count):
        search_results = api.search(q = self.fan_name+ " -filter:retweets", count=count)
        now_count: int = 0

        for result in search_results:
            if not "@" in result.text[0]:
                user_name = result.user.screen_name
                user_id = result.id
                user = result.user.name
                tweet = result.text
                time = result.created_at
                print(f"TweetID : {user_id}")
                print(f"ID      : {user_name}")
                print(f"Name    : {user}")
                print(f"Time    :{time}")
                print(f"【Tweet】 \n{tweet}")
                try:
                    api.create_favorite(user_id)  # ファヴォる
                    print(f"\n{user}をいいねしました")
                    now_count += 1
                except:
                    print("\n既にいいねしています")

                print("#"*60)
                sleep(1)

        print(f"合計 {now_count}件 の処理を完了しました")

    def favorite_by_livetag (self,count):
        search_results = api.search(q = self.live_tag+ " -filter:retweets", count=count)
        now_count: int = 0

        for result in search_results:
            if not "@" in result.text[0]:
                user_name = result.user.screen_name
                user_id = result.id
                user = result.user.name
                tweet = result.text
                time = result.created_at
                print(f"TweetID : {user_id}")
                print(f"ID      : {user_name}")
                print(f"Name    : {user}")
                print(f"Time    :{time}")
                print(f"【Tweet】 \n{tweet}")
                try:
                    api.create_favorite(user_id)  # ファヴォる
                    print(f"\n{user}をいいねしました")
                    now_count += 1
                except:
                    print("\n既にいいねしています")

                print("#"*60)
                sleep(1)

        print(f"合計 {now_count}件 の処理を完了しました")

    def favorite_by_cuttag(self,count):
        search_results = api.search(q = self.cut_tag+ " -filter:retweets", count=count)
        now_count: int = 0

        for result in search_results:
            if not "@" in result.text[0]:
                user_name = result.user.screen_name
                user_id = result.id
                user = result.user.name
                tweet = result.text
                time = result.created_at
                print(f"TweetID : {user_id}")
                print(f"ID      : {user_name}")
                print(f"Name    : {user}")
                print(f"Time    :{time}")
                print(f"【Tweet】 \n{tweet}")
                try:
                    api.create_favorite(user_id)  # ファヴォる
                    print(f"\n{user}をいいねしました")
                    now_count += 1
                except:
                    print("\n既にいいねしています")

                print("#"*60)
                sleep(1)

        print(f"合計 {now_count}件 の処理を完了しました")

Me = User("Ichigaya","Imperialmell")

# # init
# def __init__(self, name, id, art_tag, live_tag, cut_tag, fan_name)
Sora    = Hololive("ときのそら", "tokino_sora", "soraArt", "ときのそら生放送", "ときのそら生放送", "そらとも")
Roboco  = Hololive("ロボ子", "robocosan", "ロボ子Art", "ロボ子生放送", "ロボ子レクション", "ろぼさー")
Miko    = Hololive("さくらみこ", "sakuramiko35", "miko_art", "みこなま", "ミコミコ動画", "みこぴー")
# Suisei  = Hololive("星街すいせい")

# # 1stGeneration
# Mel     = Hololive("夜空メル")
# Matsuri = Hololive("夏色まつり")
# Fubuki  = Hololive("白上フブキ")
# Aki     = Hololive("アキ・ローゼンタール")
# Haato   = Hololive("赤井はあと")

# # Gamers
# Mio     = Hololive("大神ミオ")
# Okayu   = Hololive("猫又おかゆ")
# Korone  = Hololive("戌神ころね")

# # 2ndGeneration
# Choco   = Hololive("")
# Shion   = Hololive("")
# Ayame   = Hololive("")
# Subaru  = Hololive("大空スバル")
Aqua    = Hololive("湊あくあ","minatoaqua","あくあーと","湊あくあ生放送","切り抜きあくたん","あくあクルー")

# 3rdGeneration HololiveFantasy
Marine  = Hololive("宝鐘マリン","houshoumarine","マリンのお宝","マリン航海記","わかるマリン","宝鐘の一味")
Pekora  = Hololive("兎田ぺこら","usadapekora","ぺこらーと","ぺこらいぶ","野うさぎ","ひとくちぺこら")
Flare   = Hololive("不知火フレア","shiranuiflare","しらぬえ","フレアストリーム","エルフレンド","切りぬい")
Noel    = Hololive("白銀ノエル","shiroganenoel","ノエラート","ノエルーム","白銀聖騎士団","クリ抜き太郎")
Rushia  = Hololive("潤羽るしあ","uruharushia","絵クロマンサー","るしあらいぶ","ふぁんでっど","きるしあ")

# # 4thGeneration
# Kanata  = Hololive("")
# Towa    = Hololive("")
# Coco    = Hololive("")
# Watame  = Hololive("")
# Luna    = Hololive("")

# # 5thGeneration
# Lamy    = Hololive("")
# Nene    = Hololive("")
# Botan   = Hololive("")
# Polka   = Hololive("")

def main():
    Me.Timeline()
    # Me.Timeline_favorite()
    # Me.Writetweet_by_query("#Python 学習",100)
    # Me.Follow_by_query()

    # Me.Follow_by_query("湊あくあ",2)
    # Aqua.Follow_by_fanname(10)
    # Marine.RT_by_arttag(10)
    # Aqua.RT_by_arttag(10)
    # Rushia.RT_by_arttag(10)
    # Miko.favorite_by_fanname(20)
    # Aqua.favorite_by_fanname(20)
    # Aqua.favorite_by_livetag(20)
    # Aqua.favorite_by_cuttag(20)



if __name__ == "__main__":
    main()
