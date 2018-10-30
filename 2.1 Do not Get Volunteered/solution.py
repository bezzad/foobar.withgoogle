# -------------------------
# | 0| 1| 2| 3| 4| 5| 6| 7|
# -------------------------
# | 8| 9|10|11|12|13|14|15|
# -------------------------
# |16|17|  |NW|  |NE|--|23|
# -------------------------
# |24|  |WN|  |  |  |EN|  |
# -------------------------
# |32|33|--|--|36|--|--|39|
# -------------------------
# |40|  |WS|  |  |  |ES|  |
# -------------------------
# |48|49|  |SW|  |SE|  |55|
# -------------------------
# |56|57|58|59|60|61|62|63|
# -------------------------


class Position:
    def __init__(self, index=None):
        if(index != None):
            self.col = (index % 8)+1
            self.row = (index/8)+1

    @classmethod
    def create(cls, col, row):
        c = Position()
        c.col = col
        c.row = row
        return c


def getPossibleMovements(srcPos, destPos):
    res = []
    res.append(Position.create(srcPos.col-1, srcPos.row-2))  # NW
    res.append(Position.create(srcPos.col+1, srcPos.row-2))  # NE
    res.append(Position.create(srcPos.col-1, srcPos.row+2))  # SW
    res.append(Position.create(srcPos.col+1, srcPos.row+2))  # SE
    res.append(Position.create(srcPos.col+2, srcPos.row-1))  # EN
    res.append(Position.create(srcPos.col+2, srcPos.row+1))  # ES
    res.append(Position.create(srcPos.col-2, srcPos.row-1))  # WN
    res.append(Position.create(srcPos.col-2, srcPos.row+1))  # WS

    for p in res:
        if(p.col < 1 or p.col > 8 or p.row < 1 or p.row > 8):
            res.remove(p)
        elif(p.col == destPos.col and p.row == destPos.row):
            return None  # found dest position

    return res


def getMovementsCount(srcPos, destPos):
    level = 1
    bufferNextLevelMoves = []
    moves = getPossibleMovements(srcPos, destPos)

    if(moves == None): 
        return level # end of puzzle

    while True:
        level += 1

        for m in moves:
            nextLevelMoves = getPossibleMovements(m, destPos)
            if(nextLevelMoves == None):
                return level
            bufferNextLevelMoves.extend(nextLevelMoves)

        moves = bufferNextLevelMoves
        bufferNextLevelMoves = []


def answer(src, dest):
    srcPos = Position(src)
    destPos = Position(dest)
    if(srcPos.col == destPos.col and srcPos.row == destPos.row):
        return 0
    return getMovementsCount(srcPos, destPos)

# sample
print(answer(0, 1))