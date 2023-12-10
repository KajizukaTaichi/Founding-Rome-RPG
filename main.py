import random as rd

class Rome:
    def __init__(self):
        self.army = 0
        self.economic = 100
        self.city = 0

    def opening(self):
        msg = ["双子の兄弟、ロムルスとレムスは、神々の子として古代のアルバ・ロンガで誕生した",
            "彼らは運命に導かれ羊飼いに育てられたが、彼らの運命は、遥かなるローマの創設にあった。",
            "ロムルスとレムスの成長と絆が続く中、兄弟は分かれることを余儀なくされたるという悲劇的な運命び転換を迎える。",
            "しかし、ロムルス王の冒険は力と栄光の都市を求め古代の大地にローマの物語が幕を開けるのだった。\n" ]
        
        for i in msg:
            input(i)

        print(" -- ローマ建国RPG --")
        input("(c) 2023 梶塚太智. All rights reserved\n")

    def policy(self):
        print("現在のレギオー:", self.army)
        print("現在のローマ都市:", self.city)
        print("現在の持っている金:", self.economic, "デナリウス")
        select = input("A: 都市建設する？B: 戦争する？")
        if "A" in select:
            city_cost = int(input("都市建設にいくら使う？"))
            self.develop_city(city_cost)
        elif "B" in select:
            army_cost = int(input("戦争にいくら使う？"))
            self.battle_war(army_cost)
        else:
            print("元老院: そんなインペリウムないですよ")

    def battle_war(self, cost: int):
        print("戦争開始！ワーワー")
        enemy = int((rd.randint(6,12) / 10) * self.economic)
        self.army += cost; self.economic -= cost
        
        if self.army > enemy:
            print("敵は弱いぞ:",enemy)    
            print(f"勝利！賠償金{(reward := int(enemy * 2))}デナリウス獲得") 
            self.economic += reward
        else:
            print("敵は強いぞ:",enemy)
            print(f"敗北・・・。賠償金{(damage := int(enemy / 2))}デナリウス払う") 
            self.economic -= damage


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
