hp = {"sr":100, "you":100}
ap = {"sr": 5, "you":10}
gp = 5
item = 10

for num in range(10000):
    hp["sr"] = 100
    print("{}匹目のスライムが現れた！".format(num+1))

    while hp["sr"] > 0 :
        print("どうする？")
        select = input("1.攻撃　2.ガード 3.回復  :\n")

        if select=="1":
            print("あなたのターン")
            print("えい！")
            hp["sr"] -= ap["you"]
            print("スライムに{}のダメージ".format(ap["you"]))
            ap["you"] += 5
            print("攻撃力が5上がった！\n")

            print("スライムのターン")
            print("うわあ！")
            hp["you"] -= ap["sr"]
            print("あなたに５のダメージ\n")

            print("あなたのHP：{}".format(hp["you"]))
            print("スライムのHP：{}".format(hp["sr"]))
            print("")
            print("")

        
        elif select=="2":
            print("スライムのターン")
            print("スライムの攻撃をガードした！\n")

            print("あなたのHP：{}".format(hp["you"]))
            print("スライムのHP：{}".format(hp["sr"]))
            print("")
            print("")


        elif select=="3":
            print("りんごを食べた！")
            hp["you"] = 100
            print("HPがMAXになった！\n")

            print("あなたのHP：{}".format(hp["you"]))
            print("スライムのHP：{}".format(hp["sr"]))
            print("")
            print("")

        else:
            print("しね")
            print("")
            print("")

    print("よし！倒したぞ！")
    print("")
    print("")