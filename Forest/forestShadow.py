# Forest Shadow

def action():
    enemy = hero.findNearestEnemy()
    if enemy:
        if enemy.type == "thrower" or enemy.type == "munchkin":
            hero.attack(enemy)
    item = hero.findNearestItem()
    if item:
        if item.type == "gem" or item.type == "coin":
            hero.moveXY(item.pos.x, item.pos.y)
    pass

while True:
    hero.moveXY(41, 34)
    action()
