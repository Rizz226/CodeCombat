coinHunter.py

def isCoinClose(coin):
    distance = hero.distanceTo(coin)
    if distance < 20:
        return True
    else:
        return False
        pass

while True:
    item = hero.findNearestItem()
    if item:
        if isCoinClose(item):
            hero.moveXY(item.pos.x, item.pos.y)
