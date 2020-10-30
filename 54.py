f = open("/Users/rasmuser/Dropbox/ProjectEuler/54.txt", "r")
wins = 0

def RF(x):
    xx = sorted(x)
    if xx[-1]-x[0]==4 and xx[-1]==14:
        return True
    return False
def SF(x):
    xx = sorted(x)
    if xx[-1]-xx[0]==4 and not xx[-1]==14:
        return xx[-1]
    return False
def FK(x):
    check1 = False
    out = 0
    out2 = 0
    for elem in x:
        if x.count(elem)==4:
            check1 = True
            out = elem
        if x.count(elem)==1:
            out2 = elem  
    if check1:
        return out, out2
    return False
def FH(x):
    check1 = False
    check2 = False
    out = 0
    out2 = 0
    for elem in x:
        if x.count(elem)==3:
            check1 = True
            out = elem
        if x.count(elem)==2:
            check2 = True
            out2 = elem  
    if check1 and check2:
        return out, out2
    return False
def Fl(x):
    return max(x)
def St(x):
    xx = sorted(x)
    if xx[-1]-xx[0]==4:
        return xx[-1]
    return False
def TK(x):
    check1 = False
    check2 = False
    out = 0
    out2 = []
    for elem in x:
        if x.count(elem)==3:
            check1 = True
            out = elem
        if x.count(elem)==1:
            check2 = True
            out2.append(elem)
    if check1 and check2:
        return out, max(out2)
    return False
def TP(x):
    check1 = False
    check2 = False
    check3 = False
    out = []
    out2 = 0
    for elem in x:
        if x.count(elem)==2 and elem not in out and not check1:
            check1 = True
            out.append(elem)
        if x.count(elem)==2 and elem not in out:
            check2 = True
            out.append(elem)
        if x.count(elem)==1:
            check3 = True
            out2 = elem
    if check1 and check2 and check3:
        return out, out2
    return False
def OP(x):
    check1 = False
    out = 0
    out2 = []
    if len(set(x))==4:
        check1 = True
        for elem in x:
            if x.count(elem)==2:
                out = elem
            if x.count(elem)==1:
                out2.append(elem)
    if check1:
        return out, max(out2)
    return False
def HC(x):
    xx = sorted(x)
    if len(set(x))==5 and St(x)==False:
        return xx[-1], xx[-2]
    return False
def calc(x):
    score = 0
    if FK(x)!=False:
        score = 8
    if FH(x)!=False:
        score = 7
    if St(x)!=False:
        score = 5
    if TK(x)!=False:
        score = 4
    if TP(x)!=False:
        score = 3
    if OP(x)!=False:
        score = 2
    if HC(x)!=False:
        score = 1
    return score
    

        
for hand in f:
    hand = hand.split(" ")
    hand[-1] = hand[-1].strip("\n")
    score1 = 0
    score2 = 0
    high11 = 0
    high21 = 0
    high12 = 0
    high22 = 0
    h1n = []
    h2n = []
    h1s = []
    h2s = []
    for k in range(0,5):
        if list(hand[k])[0]=="T":
            h1n.append(10)
        if list(hand[k])[0]=="J":
            h1n.append(11)
        if list(hand[k])[0]=="Q":
            h1n.append(12)
        if list(hand[k])[0]=="K":
            h1n.append(13)
        if list(hand[k])[0]=="A":
            h1n.append(14)
        if list(hand[k])[0] not in ["T", "J", "Q", "K", "A"]:
            h1n.append(int(list(hand[k])[0]))
        h1s.append(list(hand[k])[1])
    for kk in range(5, 10):
        if list(hand[kk])[0]=="T":
            h2n.append(10)
        if list(hand[kk])[0]=="J":
            h2n.append(11)
        if list(hand[kk])[0]=="Q":
            h2n.append(12)
        if list(hand[kk])[0]=="K":
            h2n.append(13)
        if list(hand[kk])[0]=="A":
            h2n.append(14)
        if list(hand[kk])[0] not in ["T", "J", "Q", "K", "A"]:
            h2n.append(int(list(hand[kk])[0]))
        h2s.append(list(hand[kk])[1])
        
    if len(set(h1s))==1:
        if RF(h1n)!=False:
            score1 = 10
        if SF(h1n)!=False:
            score1 = 9
        if RF(h1n)==False and SF(h1n)==False:
            score1 = 6
    if len(set(h2s))==1:
        if RF(h2n)!=False:
            score2 = 10
        if SF(h2n)!=False:
            score2 = 9
        if RF(h2n)==False and SF(h2n)==False:
            score2 = 6
    if len(set(h1s))>1:
        score1 = calc(h1n)
    if len(set(h2s))>1:
        score2 = calc(h2n)
    if score1==score2==9:
        if SF(h1n)>SF(h2n):
            score1 = 9.5
    if score1==score2==8:
        if FK(h1n)[0]>FK(h2n)[0]:
            score1 = 8.5
        if FK(h1n)[0]==FK(h2n)[0]:
            if FK(h1n)[1]>FK(h2n)[1]:
                score1 = 8.5
    if score1==score2==7:
        if FH(h1n)[0]>FH(h2n)[0]:
            score1 = 7.5
        if FH(h1n)[0]==FH(h2n)[0]:
            if FH(h1n)[1]>FH(h2n)[1]:
                score1 = 7.5
    if score1==score2==6:
        if Fl(h1n)>Fh(h2n):
            score1 = 6.5
    if score1==score2==5:
        if St(h1n)>St(h2n):
            score1 = 5.5
    if score1==score2==4:
        if TK(h1n)[0]>TK(h2n)[0]:
            score1 = 4.5
        if TK(h1n)[0]==TK(h2n)[0]:
            if TK(h1n)[1]>TK(h2n)[1]:
                score1 = 4.5
    if score1==score2==3:
        if TP(h1n)[0][0]>TP(h2n)[0][0]:
            score1 = 3.5
        if TP(h1n)[0][0]==TP(h2n)[0][0] and TP(h1n)[0][1]>TP(h2n)[0][1]:
            score1 = 3.5
        if set(TP(h1n)[0])==set(TP(h2n)[0]):
            if TP(h1n)[1]>TP(h2n)[1]:
                score1 = 3.5
    if score1==score2==2:
        if OP(h1n)[0]>OP(h2n)[0]:
            score1 = 2.5
        if OP(h1n)[0]==OP(h2n)[0]:
            if OP(h1n)[1]>OP(h2n)[1]:
                score1 = 2.5
    if score1==score2==1:
        if HC(h1n)>HC(h2n):
            score1 = 1.5
    if score1 > score2:
        wins = wins + 1  
        print("---")
        print(h1n)
        print(h1s)
        print(" ")
        print(h2n)
        print(h2s)
        print("---")
    
print(wins)
            

        
            

    