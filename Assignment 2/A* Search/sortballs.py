def applyMove(state, move):
    ls = list(state)
    m = ls.index(0)
    if move == "PUSH":
        if m>0:
            ls[m] = ls[m-1]
            ls[m-1] = 0
            return tuple(ls)
        else:
            return state
    
    elif move == "PULL":
        if m < 5:
            ls[m] = ls[m+1]
            ls[m+1] = 0
            return tuple(ls)
        else:
            return state
            
    elif move == "SWAP":
        if m > 1:
            t1 = ls [m-1]
            t2 = ls [m-2]
            ls [m-2] = t1
            ls [m-1] = t2
            return tuple(ls)
        else:
            return state
    
    else:
        if m < 4:
            flippy = ls[m+1: ] 
            flippy.reverse()
            unflippy = ls[: m+1]
            lsf = unflippy + flippy
            return tuple(lsf)
        else:
            return state

def h(state):
    ls = list (state)
    m = ls.index(0)
    A = m*10
    B=0
    for e in ls:
        j=0
        while j<e:
            if (ls[j]>ls[e] and ls[j]!=0 and ls[e]!=0):
                B=B+1
                break
            j=j+1
    C=0
    for i in ls:
        j=i+1
        while j<len(ls):
            if ls[j]>ls[i] and ls[j]!=0 and ls[i]!=0:
                C+=1
                break
            j=j+1
    
    D = min(B*17, (C*17+8)) 
    return  A + D

def getNext(frontier):
    alist =[]
    tlist =[]
    blist =[]
    for item in frontier:
        alist.append(h(item['state']))
    d = {'PUSH': 10, 'PULL': 5, 'SWAP': 17, 'FLIP': 8}
    res = [sum(map(d.get, item['path'])) for item in frontier]
    blist = [x+y for x, y in zip(res, alist)]
    a = min(blist)
    return frontier.pop(blist.index(a))
    
    