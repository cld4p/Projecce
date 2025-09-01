
from resources import Player

jil=Player(
    health=100,
    damage=10,
    maxHealth=100,
    armor=30
)

Player.reduceHealth(jil,40)

Player.showHealth(jil)



