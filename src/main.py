from holotter import User, Hololive

Me = User("Ichigaya", "BIEIQ")

# # init
# def __init__(self, name, id, art_tag, live_tag, cut_tag, fan_name)
Sora = Hololive(
    "ときのそら", "tokino_sora", "soraArt", "ときのそら生放送", "ときのそら生放送", "そらとも"
)
Roboco = Hololive("ロボ子", "robocosan", "ロボ子Art", "ロボ子生放送", "ロボ子レクション", "ろぼさー")
Miko = Hololive("さくらみこ", "sakuramiko35", "miko_art", "みこなま", "ミコミコ動画", "みこぴー")
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
Aqua = Hololive("湊あくあ", "minatoaqua", "あくあーと", "湊あくあ生放送", "切り抜きあくたん", "あくあクルー")

# 3rdGeneration HololiveFantasy
Marine = Hololive(
    "宝鐘マリン", "houshoumarine", "マリンのお宝", "マリン航海記", "わかるマリン", "宝鐘の一味"
)
Pekora = Hololive("兎田ぺこら", "usadapekora", "ぺこらーと", "ぺこらいぶ", "野うさぎ", "ひとくちぺこら")
Flare = Hololive(
    "不知火フレア", "shiranuiflare", "しらぬえ", "フレアストリーム", "エルフレンド", "切りぬい"
)
Noel = Hololive("白銀ノエル", "shiroganenoel", "ノエラート", "ノエルーム", "白銀聖騎士団", "クリ抜き太郎")
Rushia = Hololive(
    "潤羽るしあ", "uruharushia", "絵クロマンサー", "るしあらいぶ", "ふぁんでっど", "きるしあ"
)

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
    # Me.Timeline()
    Me.Timeline_favorite()
    # Me.Writetweet_by_query("潤羽るしあ",100)
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
