
from resources import Player

jil=Player(
    health=100,
    damage=10,
    maxHealth=100,
    armor=30
)

claws=Player(
    health=40,
    damage=60,
    maxHealth=40,
    armor=20
)


Player.reduceHealth(jil,claws)

Player.showHealth(jil)



