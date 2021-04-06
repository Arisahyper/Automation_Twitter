import tweepy
from time import sleep

API_KEY = "XXXXXXXXXXXXXXXXXXXX"
API_SECRET = 'XXXXXXXXXXXXXXXXXXXX'
ACCESS_TOKEN = 'XXXXXXXXXXXXXXXXXXXX-XXXXXXXXXXXXXXXXXXXX'
ACCESS_TOKEN_SECRET = 'XXXXXXXXXXXXXXXXXXXX'

auth = tweepy.OAuthHandler(API_KEY, API_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)


def get_user_tweet(textfile, account, count):  # 特定のユーザーのツイート取得し書き込み

    tweets = api.user_timeline(account, count=count, page=1)
    now_count = 1
    f = open(textfile, 'w')

    for tweet in tweets:
        f.write('\nTweetID : ' + str(tweet.id))               # tweetのID
        f.write('\nUserID : @' + str(tweet.user.screen_name))  # ユーザー名
        f.write('\nDate : ' + str(tweet.created_at))      # 呟いた日時
        f.write("\n" + str(tweet.text))                  # ツイート内容
        f.write('\nRT : ' + str(tweet.retweet_count))  # ツイートのリツイート数
        f.write('\nFav : ' + str(tweet.favorite_count))  # ツイートのいいね数
        f.write('\nTweetCount : ' + str(now_count))  # ツイート数
        f.write(
            '\n====================================================================')
        now_count += 1  # ツイート数を計算

    f.close()


def get_serch_tweet(textfile, query, cnt):  # 特定のワードを検索し書き込み

    tweets = api.search(q=query, count=cnt)
    now_count = 1
    f = open(textfile, 'w')

    for tweet in tweets:
        f.write('\nTweetID    : ' + str(tweet.id))
        f.write('\nUserID     : @' + str(tweet.user.screen_name))
        f.write('\nDate       : ' + str(tweet.created_at))
        f.write("\n【 内容 】")
        f.write("\n" + str(tweet.text))
        f.write('\nRT         : ' + str(tweet.retweet_count))
        f.write('\nFav        : ' + str(tweet.favorite_count))
        f.write('\nTweetCount : ' + str(now_count))
        f.write(
            '\n====================================================================')
        now_count += 1

    print("処理が終了しました")
    f.close()


def follow(query, count):  # 特定のワードからツイート取得し、いいねしてフォロー
    search_results = api.search(q=query, count=count)

    for result in search_results:
        sleep(1)
        user_id = result.id
        user = result.user.name
        tweet = result.text
        user_name = result.user.screen_name
        time = result.created_at

        print(f"TweetID：{user_id}")
        print(f"名前：{user}")
        print(f"ID：{user_name}")
        print(f"【 内容 】\n{tweet}")
        print(f"時間：{time}")
        try:
            api.create_friendship(user_name)
            print("をフォローしました")
        except:
            print("もう既にいいねかフォローしています")

        print("#"*60)
        sleep(10)
    print("処理を終了しました")


def favorite(query, count):  # 特定のワードからツイート取得し、いいねしてフォロー
    search_results = api.search(q=query, count=count)

    for result in search_results:
        # username = result.user._json['screen_name']
        user_name = result.user.screen_name
        print(user_name)
        user_id = result.id  # ツイートのstatusオブジェクトから、ツイートidを取得
        print(user_id)
        user = result.user.name  # ツイートのstatusオブジェクトから、userオブジェクトを取り出し、名前を取得する
        print(user)
        tweet = result.text
        print(tweet)
        time = result.created_at
        print(time)
        try:
            api.create_favorite(user_id)  # ファヴォる
            print(user)
            print("をいいねしました")
        except:
            print("もう既にいいねかフォローしています")

        print("##################")
        sleep(1)
    print("処理を終了しました")


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


def search_retweet_fav(query, count, favcount):  # 特定のFAV数以上のツイートをRT
    serch_results = api.search(q=query, count=5000)  # 5000件検索
    nowcount = 0

    for result in serch_results:
        FAVcount = result.favorite_count
        if FAVcount >= favcount:  # ファボ数
            if nowcount < count:
                user_name = result.user.screen_name
                user_id = result.id
                user = result.user.name
                tweet = result.text
                time = result.created_at

                print(f"ツイートID：{user_id}")
                print(f"名前：{user}")
                print(f"UserID：{user_name}")
                print(f"ツイート内容\n{tweet}")
                print(f"RT数：{FAVcount}")
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
                sleep(10)

    print("処理を終了しました")


def timeline_fav():
    timeline = api.home_timeline()
    hit_count = 0
    for tweet in timeline:
        sleep(1)
        userid = tweet.id

        user_name = tweet.user.name
        user_id = tweet.user.screen_name
        text = tweet.text
        time = tweet.created_at

        print("#"*60)
        print(f"名前：{user_name}")
        print(f"ID：{user_id}")
        print(f"【 内容 】\n{text}")
        print(f"投稿日時：{time}")

        try:
            api.create_favorite(userid)
            print("いいねしました")
            hit_count += 1
        except:
            print("既にいいね済みです")

    print("処理を終了しました")
    print(f"{hit_count}件のいいね")


def main():
    # get_user_tweet(書き込むファイル, ユーザー名, 取得数)
    get_user_tweet('board.txt', "@Python", 200)

    # follow(特定のワード,フォローする数)
    follow("#Python", 100)

    # remove_unfollower(自分のユーザー名, 解除する数)
    remove_unfollower("@username", 50)

    # get_serch_tweet(書き込むファイル, 特定のワード, 取得したい数)
    get_serch_tweet('board.txt', "Python", 100)

    # search_retweet_rt(検索ワード, リツイートする数, 対象のツイートのRT数)
    search_retweet_rt("Python", 10, 500)

    # search_retweet_fav(検索ワード, リツイートする数, 対象のツイートのFAV数)
    search_retweet_fav("Python", 5, 5000)

    # favorite(検索ワード, ふぁぼする数)
    favorite("Python", 100)

    timeline_fav()


if __name__ == "__main__":
    main()
