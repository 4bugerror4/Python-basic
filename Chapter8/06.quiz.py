class Item:
    def __init__(self, name, price, weight, isdropable):
        self.name = name
        self.price = price
        self.weight = weight
        self.isdropable = isdropable
    
    def sale(self):
        print(f"무기를 판매하였습니다. [판매가격 : {self.price}]")

    def discard(self):
        if self.isdropable != True:
            print("아이템을 버릴 수  없습니다.")
        else:
            print("아이템을 버렸습니다.")

class WearableItem(Item):
    def __init__(self, name, price, weight, isdropable, effect):
        super().__init__(name, price, weight, isdropable)
        self.effect = effect
    
    def wear(self):
        print(f"[{self.effect} 효과]")

class UseableItem(Item):
    def __init__(self, name, price, weight, isdropable, effect):
        super().__init__(name, price, weight, isdropable)
        self.effect = effect

    def use(self):
        print(f"[{self.effect} 효과]")


sword = UseableItem("엑스칼리버", 1000, 500, True, "공격력 50 증가")
sword.use()

pants = WearableItem("바지", 500, 30, True, "방어력 10 증가")
pants.wear()

ring = WearableItem("반지", 50000, 50, False, "공격력 2000, 방어력 2000 증가")
ring.discard()
ring.wear()
