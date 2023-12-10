class Rome:
    def __init__(self):
        self.army = 0
        self.economic = 0

    def opening(self):
        msg = ["双子の兄弟、ロムルスとレムスは、神々の子として古代のアルバ・ロンガで誕生した",
            "彼らは運命に導かれ羊飼いに育てられたが、彼らの運命は、遥かなるローマの創設にあった。",
            "ロムルスとレムスの成長と絆が続く中、兄弟は分かれることを余儀なくされたるという悲劇的な運命び転換を迎える。",
            "しかし、ロムルス王の冒険は力と栄光の都市を求め古代の大地にローマの物語が幕を開けるのだった。\n" ]
        
        for i in msg:
            input(i)

        print(" -- ローマ建国RPG --")
        print("(c) 2023 梶塚太智. All rights reserved\n")


if __name__ == "__main__":
    rome = Rome()
    rome.opening()
