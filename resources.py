
class Player:
    def __init__(self,health,damage,maxHealth,armor):
        self.health=health
        self.damage=damage
        self.maxHealth=maxHealth
        self.armor=armor

    def reduceHealth(self,hit):
        self.health-=hit*15//self.armor
    
    def healHealth(self,heal):
        self.health+=heal-max(0,self.health-self.maxHealth)

    def showHealth(self):
        print("Health: ",self.health,"/",self.maxHealth,",Armor: ",self.armor)
















