class Character : 
    def __init__(self , name , health , attack):
        self.name = name
        self.health = health
        self.attack = attack

    def attackEnemy(self):
        print(f'{self.name} is attack with power {self.attack}')


warrior = Character('Thor' , 100 , 50)
mega = Character('Gandlalf' , 80 , 70)
archer = Character('Archer' , 80 , 90)

warrior.attackEnemy()
mega.attackEnemy()
archer.attackEnemy()