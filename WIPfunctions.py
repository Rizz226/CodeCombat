# These functions are in progress. Theres something there, but I havent gotten it all worked out yet how I'd like.

# needs location objects, not X-Y coords.
def fightToPos(pos):
    if enemies:
        for e in enemies:
            if disBetween(pos, e) < hero.distanceTo(pos):
                if hero.distanceTo(e) < 15:
                    fight(e)
    if hero.pos == pos.pos:
        return
    hero.move(pos.pos)

# needs  objects, not X-Y coords.
def disBetween(A, B):
    x = A.pos.x - B.pos.x
    y = A.pos.y - B.pos.y
    disBet = (((x**2) + (y**2)) ** (1/2))
    return disBet
