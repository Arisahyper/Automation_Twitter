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
# Mel     = HoloManager("夜空メル")
# Matsuri = HoloManager("夏色まつり")
# Fubuki  = HoloManager("白上フブキ")
# Aki     = HoloManager("アキ・ローゼンタール")
# Haato   = HoloManager("赤井はあと")

# # Gamers
# Mio     = HoloManager("大神ミオ")
# Okayu   = HoloManager("猫又おかゆ")
# Korone  = HoloManager("戌神ころね")

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
# Kanata  = HoloManager("")
# Towa    = HoloManager("")
# Coco    = HoloManager("")
# Watame  = HoloManager("")
# Luna    = HoloManager("")

# # 5thGeneration
# Lamy    = HoloManager("")
# Nene    = HoloManager("")
# Botan   = HoloManager("")
# Polka   = HoloManager("")


def main():
    # Me.Timeline()
    Me.Timeline_favorite()
    # Me.Writetweet_by_query("潤羽るしあ",100)
    # Me.Follow_by_query()

    # Me.Follow_by_query("湊あくあ",2)
    # Miko.favorite_by_fanname(20)
    # Aqua.favorite_by_fanname(20)
    # Aqua.favorite_by_livetag(20)
    # Aqua.favorite_by_cuttag(20)
