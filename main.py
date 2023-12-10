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
        print("(c) 2023 梶塚太智. All rights reserved\n")

    def policy(self):
        print("現在のレギオー:", self.army)
        print("現在のローマ都市:", self.city)
        print("現在の持っている金:", self.economic)
        select = input("A：都市建設する？B:戦争する？")
        if "A" in select:
            city_cost = int(input("都市建設にいくら使う？"))
            self.develop_city(city_cost)
        elif "B" in select:
            army_cost = int(input("戦争にいくら使う？"))
            self.battle_war(army_cost)

    def battle_war(self, cost: int):
        print("戦争開始！ワーワー")
        self.army += cost; self.economic -= cost
        enemy = (rd.randint(1,30) / 10) * self.army    
        
        if self.army > enemy:
            print("敵は弱いぞ！")    
            print(f"勝利！報酬{enemy}ゲット") 
            self.economic += int(enemy)
        else:
            print("敵は強いぞ！")
            print(f"敗北・・・。賠償金{(damage := enemy / 2)}払う") 
            self.economic -= int(damage)


    def develop_city(self, cost: int):
        print(f"街を{cost}立派にした！")
        self.city += cost; self.economic -= cost



if __name__ == "__main__":
    rome = Rome()
    rome.opening()

    while True:
        rome.policy()
