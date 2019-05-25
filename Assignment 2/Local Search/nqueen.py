def printBoard(queen):
  for n in queen:
    print("- "*n+"Q"+" -"*(len(queen)-n-1))

def countAttack(queen):
    count = 0
    for row1 in range( 0, len(queen) ):
        for row2 in range( row1 + 1, len( queen ) ):
            if queen[row1] == queen[row2]:
                count += 1
            elif abs(queen[row1] - queen[row2]) == (row2 - row1):
                count += 1
    return count

def printMatrix(queen):
    queenl = list(queen)
    for n in range (0, len(queen)):
        alist =[]
        for i in range(0,len(queen)):
            queenl[n] = i
            alist.insert(i,countAttack(queenl))
        alist[queen[n]] = "-"
        sarr = [str(a) for a in alist]
        print("  " . join(sarr))
        queenl = list(queen)

def moveOne(queen):
    blist = []
    queenl = list(queen)
    for n in range (0, len(queen)):
        alist =[]
        for i in range(0,len(queen)):
            queenl[n] = i
            alist.insert(i,countAttack(queenl))
        alist[queen[n]] = 2000 #can never reached this value. 
        blist.extend(alist)
        queenl = list(queen)
    u = blist.index(min(blist)) + 1
    r = u/(len(queen))
    l = ((((r*10)%10)*len(queen))/10) - 1
    queenl[int(r)] = int(l) 
    return tuple(queenl)

def printMatrix2(queen):
    queenl = list(queen)
    for n in range (0, len(queen)):
        alist =[]
        for i in range(0,len(queen)):
            queenl[n] = queen[i]
            queenl[i] = queen[n] 
            alist.insert(i,countAttack(queenl))
            queenl = list(queen)
        alist[n] = "-"
        sarr = [str(a) for a in alist]
        print("  " . join(sarr))
        queenl = list(queen)

def moveTwo(queen):
    blist = []
    queenl = list(queen)
    for n in range (0, len(queen)):
        alist =[]
        for i in range(0,len(queen)):
            queenl[n] = queen[i]
            queenl[i] = queen[n] 
            alist.insert(i,countAttack(queenl))
            queenl = list(queen)
        alist[n] = 2000 #can't touch this 
        blist.extend(alist)
        queenl = list(queen)
    u = blist.index(min(blist)) + 1
    r = u/(len(queen))
    if (u%len(queen) == 0):
        p = (u-1)%len(queen)
        queenl[p] = queen[int(r)-1]
        queenl[int(r)-1] = queen[p]
        return tuple(queenl) 
    else:    
        l = ((((r*10)%10)*len(queen))/10) - 1
        queenl[int(l)] = queen[int(r)]
        queenl[int(r)] = queen[int(l)]
        return tuple(queenl) 
