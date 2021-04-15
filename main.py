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

def main():
    ####### 換装済 #################################################################
    
    create_graph_auto("sakuramiko35",100)

    # timeline_fav() # 自分のタイムラインにいいね

    # follow() # 検索したワードでフォローする

    # favorite() # 検索したワードにいいねをつける

    # user_fav() # 特定のユーザーにファボ爆
    
    # create_user_graph()  # ユーザーのツイートのRTといいねをグラフ化

    # get_user_tweet()

    # get_serch_tweet()

    ###############################################################################

    # remove_unfollower(自分のユーザー名, 解除する数)
    # remove_unfollower("@imperialmell", 50)

    # search_retweet_rt(検索ワード, リツイートする数, 対象のツイートのRT数)
    # search_retweet_rt("#miko_art" + " -filter:retweets", 10, 500)

def follow():
    query = input("検索ワードの入力 >> ")
    count = int(input("何件フォローしますか？ >> "))

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
        print(f"名前    ：{user}")
        print(f"ID     ：{user_name}")
        print(f"時間    ：{time}")
        print(f"【 内容 】\n{tweet}")
        try:
            api.create_friendship(user_name)
            print("をフォローしました")
            print(f"現在の実行数  {now_count}件")
        except:
            print("既にいいねかフォローしています")

        print("#"*60)
        sleep(10)
    print(f"合計 {now_count}件 の処理を完了しました")

def timeline_fav():
    timeline = api.home_timeline(count=30)
    hit_count = 0
    for tweet in timeline:
        if not "@" in tweet.text[0]:
        # if not tweet.text.startswith("@"):
            tweet_id = tweet.id
            user_name = tweet.user.name
            user_id = tweet.user.screen_name
            text = tweet.text
            time = tweet.created_at

            print(f"TweetID：{tweet_id}")
            print(f"Nama   ：{user_name}")
            print(f"ID     ：{user_id}")
            print(f"Time   ：{time}")
            print(f"【 内容 】\n{text}")

            try:
                api.create_favorite(tweet_id)
                print("いいねしました")
                hit_count += 1
            except:
                print("既にいいね済みです")

            print("#"*60)
            sleep(1)

    print("処理を終了しました")
    print(f"{hit_count}件のいいね")

def favorite():  # 特定のワードからツイート取得し、いいね
    query = input("検索ワードの入力 >> ")
    count = int(input("何件いいねしますか？ >> "))

    search_results = api.search(q=query + " -filter:retweets", count=count)
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
    print("処理を終了しました")
    print(f"実行件数：{now_count}件")

def user_fav():  # 特定のユーザーのツイート取得し書き込み
    account = input("ふぁぼ爆するユーザーのIDを入力 >> @")
    count = int(input("何件いいねしますか？  >> "))

    tweets = api.user_timeline("@" + account, count=count, page=1)
    now_count = 1

    for tweet in tweets:
        print('\nTweetID : ' + str(tweet.id))               # tweetのID
        print('\nUserID : @' + str(tweet.user.screen_name))  # ユーザー名
        print('\nDate : ' + str(tweet.created_at))      # 呟いた日時
        print("\n" + str(tweet.text))                  # ツイート内容
        print('\nRT : ' + str(tweet.retweet_count))  # ツイートのリツイート数
        print('\nFav : ' + str(tweet.favorite_count))  # ツイートのいいね数
        print('\nTweetCount : ' + str(now_count) + "\n")  # ツイート数
        try:
            api.create_favorite(tweet.id)
            print("いいねしました")
        except:
            print("いいねできませんでした")
        now_count += 1  # ツイート数を計算
    print("合計 {now_count}件 の処理が完了しました")

def get_user_tweet():  # 特定のユーザーのツイート取得し書き込み
    account = input("取得するユーザーのIDを入力 >> @")
    count = int(input("何件取得しますか？  >> "))


    tweets = api.user_timeline(account, count=count, page=1)
    now_count = 0
    with open("board.txt", 'w') as f:
        f.write(f"### @{account} さんのツイート ###")

        for tweet in tweets:
            now_count += 1                                          # ツイート数を計算
            f.write(f"\nTweetCount : {now_count}")                  # ツイート数
            f.write(f"\nTweetID    : {tweet.id}")                   # tweetのID
            f.write(f"\nUserID     : @{tweet.user.screen_name}")    # ユーザー名
            f.write(f"\nDate       : {tweet.created_at}")           # 呟いた日時
            f.write(f"\nRT         : {tweet.retweet_count}")        # ツイートのリツイート数
            f.write(f"\nFav        : {tweet.favorite_count}")       # ツイートのいいね数
            f.write(f"\n{tweet.text}\n")                            # ツイート内容
            f.write('#'*60)

    print(f"合計 {now_count}件 の処理が完了しました")

def create_user_graph():  # 特定のユーザーのツイート取得しツイート
    Rtlist:list = []
    Favlist:list = []
    countlist:list = []
    now_count = 1

    account = input("ユーザーのIDを入力 >> @")
    count = int(input("何件取得しますか？  >> "))

    tweets = api.user_timeline(account, count=count, page=1)
    for tweet in tweets:
        if not "RT @" in tweet.text[0:4]:
            try: 
                print('TweetID : ' + str(tweet.id))                   # tweetのID
                print('UserID  : @' + str(tweet.user.screen_name))    # ユーザー名
                print('Date    : ' + str(tweet.created_at))           # 呟いた日時
                print("" + str(tweet.text))                           # ツイート内容
                print('RT      : ' + str(tweet.retweet_count))        # ツイートのリツイート数
                print(f"Fav    : {tweet.favorite_count}")             # ツイートのいいね数
                print(f"{str(now_count)}件目")                         # ツイート数
                Rtlist.append(tweet.retweet_count)
                Favlist.append(tweet.favorite_count)
                countlist.append(now_count)
                print(f"{Rtlist}\n{Favlist}")
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

    imgname = (f"{account}-tweet.png")
    fig.savefig(imgname)

    api.update_with_media(status = (f"@ {account} ReactionChart"), filename = imgname)

def get_serch_tweet():  # 特定のワードを検索し書き込み
    query = input("検索するワードの入力 >> ")
    count = int(input("何件取得しますか？  >> "))

    tweets = api.search(q=query + " -filter:retweets", count=count)
    now_count = 0

    with open('board.txt', 'w') as f:
        for tweet in tweets:
            now_count += 1
            f.write(f"\nTweetCount : {now_count}")
            f.write(f"\nTweetID    : {tweet.id}")
            f.write(f"\nUserID     : @{tweet.user.screen_name}")
            f.write(f"\nDate       : {tweet.created_at}")
            f.write(f"\nRT         : {tweet.retweet_count}")
            f.write(f"\nFav        : {tweet.favorite_count}")
            f.write(f"\n【 内容 】")
            f.write(f"\n{tweet.text}\n")
            f.write("#")

    print(f"合計 {now_count}件 の処理が終了しました")

def search_retweet_rt(query, count, rtcount):  # 特定のRT数以上のツイートをRT
    serch_results = api.search(q=query, count=1000)  # 1000件検索
    nowcount = 0

    for result in serch_results:
        RTcount = result.retweet_count
        if RTcount >= rtcount:  # RT数
            if nowcount < count:
                user_name = result.user.screen_name
                user_id = result.id
                user = result.user.name
                tweet = result.text
                time = result.created_at

                print(f"UserID：{user_name}")
                print(f"ツイートID：{user_id}")
                print(f"名前：{user}")
                print(f"ツイート内容\n{tweet}")
                print(f"RT数：{RTcount}")
                print(f"日時：{time}")
                try:
                    api.retweet(user_id)
                    print("リツイートしました")
                    nowcount += 1
                except:
                    print("既にRT済みです")

                print(f"現在のRT数：{nowcount}")
                print("#"*60)
                sleep(1)
    print("処理を終了しました")

def remove_unfollower(userid, count):  # フォローされていないユーザーをリムーブ
    unfollow_count = 0
    user_id = userid
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

    print("処理を終了しました")

def get_user_tweet():  # 特定のユーザーのツイート取得し書き込み
    account = input("取得するユーザーのIDを入力 >> @")
    count = int(input("何件取得しますか？  >> "))


    tweets = api.user_timeline(account, count=count, page=1)
    now_count = 0
    with open("board.txt", 'w') as f:
        f.write(f"### @{account} さんのツイート ###")

        for tweet in tweets:
            now_count += 1                                          # ツイート数を計算
            f.write(f"\nTweetCount : {now_count}")                  # ツイート数
            f.write(f"\nTweetID    : {tweet.id}")                   # tweetのID
            f.write(f"\nUserID     : @{tweet.user.screen_name}")    # ユーザー名
            f.write(f"\nDate       : {tweet.created_at}")           # 呟いた日時
            f.write(f"\nRT         : {tweet.retweet_count}")        # ツイートのリツイート数
            f.write(f"\nFav        : {tweet.favorite_count}")       # ツイートのいいね数
            f.write(f"\n{tweet.text}\n")                            # ツイート内容
            f.write('#'*60)

    print(f"合計 {now_count}件 の処理が完了しました")

def create_graph_auto(account,count):
    Rtlist:list = []
    Favlist:list = []
    countlist:list = []
    now_count = 1

    tweets = api.user_timeline(account, count=count, page=1)
    for tweet in tweets:
        if not "RT @" in tweet.text[0:4]:
            try: 
                print('TweetID : ' + str(tweet.id))                   # tweetのID
                print('UserID  : @' + str(tweet.user.screen_name))    # ユーザー名
                print('Date    : ' + str(tweet.created_at))           # 呟いた日時
                print("" + str(tweet.text))                           # ツイート内容
                print('RT      : ' + str(tweet.retweet_count))        # ツイートのリツイート数
                print(f"Fav    : {tweet.favorite_count}")             # ツイートのいいね数
                print(f"{str(now_count)}件目")                         # ツイート数
                Rtlist.append(tweet.retweet_count)
                Favlist.append(tweet.favorite_count)
                countlist.append(now_count)
                print(f"{Rtlist}\n{Favlist}")
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

    dt_now = datetime.datetime.now()
    dt_now = dt_now.strftime('%Y:%m:%d: %H:%M:%S')
    imgname = (f"./ReactionChartData/{account}-{dt_now}-tweet.png")
    fig.savefig(imgname)

    # api.update_with_media(status = (f"@ {account} ReactionChart"), filename = imgname)






if __name__ == "__main__":
    main()
