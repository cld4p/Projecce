
class Player:
    def __init__(self,health,damage,maxHealth,armor):
        self.health=health
        self.damage=damage
        self.maxHealth=maxHealth
        self.armor=armor

    def reduceHealth(victim,attacker):
       victim.health-=attacker.damage*15//victim.armor
    
    def healHealth(self,heal):
        self.health+=heal-max(0,self.health-self.maxHealth)

    def showHealth(self):
        print("Health: ",self.health,"/",self.maxHealth,",Armor: ",self.armor)
    
    def setArmor(self,armorAmount):
        self.armor=armorAmount

    def setMaxHealth(self,setHealth):
        self.maxHealth=setHealth
    
    def setDamage(self,damageamt):
        self.damage=damageamt












