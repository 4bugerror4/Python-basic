class Champion:
    def __init__(self, name, health, attack):
        self.name = name
        self.health = health
        self.attack = attack
        print(f"{name}님 소환사 협곡에 오신것을 환영합니다.")

    def basic_attack(self):
        print(f"{self.name} 기본 공격 {self.attack}")

ezreal = Champion("이즈리얼", 700, 90)
leesin = Champion("리신", 800, 95)
yasuo = Champion("야스오", 850, 92)
ezreal.basic_attack()
leesin.basic_attack()
yasuo.basic_attack()