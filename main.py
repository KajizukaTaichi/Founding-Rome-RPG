import random as rd

class Rome:
    def __init__(self):
        self.army = 0
        self.economic = 100
        self.city = 0
        self.morale = 10

    def opening(self):
        msg = ["双子の兄弟、ロムルスとレムスは、神々の子として古代のアルバ・ロンガで誕生した",
            "彼らは運命に導かれ羊飼いに育てられたが、彼らの運命は、遥かなるローマの創設にあった。",
            "ロムルスとレムスの成長と絆が続く中、兄弟は分かれることを余儀なくされたるという悲劇的な運命び転換を迎える。",
            "しかし、ロムルス王の冒険は力と栄光の都市を求め古代の大地にローマの物語が幕を開けるのだった。\n" ]
        
        for i in msg:
            input(i)

        print(" -- ローマ建国RPG --")
        print("(c) 2023 梶塚太智. All rights reserved")

    def policy(self):
        input()
        print("レギオー:", self.army)
        print("市民の士気:", self.morale)
        print("ローマ都市:レベル", self.city)
        print("経済力:", self.economic, "デナリウス")
        select = input("元老院　{ A:都市建設する？　B:戦争する？　C:民会で演説する？")
        if "A" in select or "a" in select:
            try: 
                cost = int(input("都市建設にいくら使う？"))
            except:
                cost = self.economic / 10 
                print(f"元老院は{cost}デナリウスを使う決議をした")
            self.develop_city(cost)
        elif "B" in select or "b" in select:
            try: 
                cost = int(input("戦争にいくら使う？"))
            except:
                cost = self.economic / 10 
                print(f"元老院は{cost}デナリウスを使う決議をした")
            self.battle_war(cost)
        elif "C" in select or "c" in select:
            try:
                cost = int(input("演説にいくら使う？"))
            except:
                cost = self.economic / 10 
                print(f"元老院は{cost}デナリウスを使う決議をした")
            self.speech(cost)
        else:
            print("元老院 { そんなインペリウムないですよ")

    def speech(self, cost):
        self.morale += cost; self.economic -= cost
        input("市民 { いいぞ！ロムルス王")
        print(f"市民の士気が{cost}アップ!")

    def battle_war(self, cost: int):
        print("戦争開始！ワーワー")
        enemy = int((rd.randint(6,14) / 10) * self.economic)
        self.army += cost; self.economic -= cost
        
        if ((self.army + self.morale) / 2)  > enemy:
            print("敵は弱いぞ:軍事力が",enemy,"しかない")
            input("絶対勝てる、勇気を持って行くぞー！")
            print("おー！")

            print(f"勝利！賠償金{(reward := int(enemy * 2))}デナリウス獲得") 
            self.economic += reward
            print(f"市民の士気が{reward}アップ！")
            self.morale += reward
        else:
            print("敵は強いぞ:軍事力が",enemy,"もある")

            select = input("元老院 { 勝ち目がないな、和平しとく？ (Yes/No)")
            if select == "No":
                print("元老院 { えっ！負けるかもしれない戦争をするの？")

                print(f"敗北・・・。賠償金{(damage := int(enemy * 2))}デナリウス払う") 
                self.economic -= damage
                print(f"市民の士気が{damage}ダウン")
                self.morale -= damage
            else:
                print("元老院は和平の決議をし、ローマは敵と和平を結んだ！")

    def develop_city(self, cost: int):
        print(f"街を{cost}デナリウス分立派にした！")
        self.city += cost; self.economic -= cost
        print(f"報酬{(reward := int(self.city / 6))}デナリウス獲得！")
        self.economic += reward
        self.is_clear()

    def is_clear(self):
        if self.economic < -1000:
            print(f"借金が{abs(self.economic)}デナリウスに膨れ上がった。ゲームオーバー")
            exit(0)
        elif self.city >= 5000:
            input("ゲームクリア！")
            input("ユピテルが風を遣わしてロムルス王の伝説の生涯は終わりましたとさ")
            input("めでたしめでたし")
            exit(0) 


if __name__ == "__main__":
    rome = Rome()
    rome.opening()

    while True:
        rome.policy()
