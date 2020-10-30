true = 1
false = 0

def boundary(vec):
    ones = [0]*len(vec)
    zeros = [0]*len(vec)
    if vec[-1] == 1:
        ones[-1] = 1
    if vec[-1] == 0:
        zeros[-1] = 1
    for ind in range(len(vec)-1):
        if vec[ind] + vec[ind+1]==1:
            ones[ind] = 1
        else:
            zeros[ind] = 1
    return(ones,zeros)

def preimagecount(state, blockones, blockzeros):
    #[1,0,0,0]
    C1 = blockzeros[0]*blockzeros[1]*blockzeros[2]
    #[0,1,0,0]
    C2 = blockones[0]*blockzeros[1]*blockzeros[2]
    #[0,0,1,0]
    C3 = blockzeros[0]*blockones[1]*blockzeros[2]
    #[0,0,0,1]
    C4 = blockzeros[0]*blockzeros[1]*blockones[2]
    #[1,1,0,0]
    C5 = blockones[0]*blockzeros[1]*blockzeros[2]
    #[0,0,1,1]
    C6 = blockzeros[0]*blockones[1]*blockones[2]
    #[0,1,1,0]
    C7 = blockones[0]*blockones[1]*blockzeros[2]
    #[1,0,0,1]
    C8 = blockzeros[0]*blockzeros[1]*blockones[2]
    #[1,0,1,0]
    C9 = blockzeros[0]*blockones[1]*blockzeros[2]
    #[0,1,0,1]
    C10 = blockones[0]*blockzeros[1]*blockones[2]
    #[0,1,1,1]
    C11 = blockones[0]*blockones[1]*blockones[2]
    #[1,0,1,1]
    C12 = blockzeros[0]*blockones[1]*blockones[2]
    #[1,1,0,1]
    C13 = blockones[0]*blockzeros[1]*ones[2]
    #[1,1,1,0]
    C14 = blockones[0]*blockones[1]*blockzeros[2]
    #[1,1,1,1]
    C15 = blockones[0]*blockones[1]*blockones[2]
    #[0,0,0,0]
    C16 = blockzeros[0]*blockzeros[1]*blockzeros[2]
    if state==1:
        return([C1,C2+C3+C4])
    if state==0:
        return([C5+C8+C9+C12+C13+C14+C15,C6+C7+C10+C11+C16])

def solution(g):
    total = 1
    height = len(g)
    width = len(g[1])
    count1 = [0]*width
    count0 = [0]*width
    countnext1 = boundary(g[-1])[0]
    countnext0 = boundary(g[-1])[1]
    for rowind in reversed(range(height-1)):
        count1[-1] = boundary([g[rowind][width-1], g[rowind+1][width-1]])[0][0]
        count0[-1] = boundary([g[rowind][width-1], g[rowind+1][width-1]])[1][1]
        for colind in reversed(range(width-1)):
            blockones = [count1[rowind+1], countnext1[rowind], countnext1[rowind+1]]
            blockzeros = [count0[rowind+1], countnext0[rowind], countnext0[rowind+1]]
            count1[rowind] = preimagecount(g[rowind][colind], blockones, blockzeros)[0]
            count0[rowind] = preimagecount(g[rowind][colind], blockones, blockzeros)[1]
        for ind in range(width):
            total *= count1[ind] + count0[ind]
        countnext1 = count1
        countnext0 = count0
        count1 = [0]*width
        count0 = [0]*width
    for ind in range(width):
        total *= countnext1[ind] + countnext0[ind]
    return(total)
            

solution([[true, true, false], [true, false, false], [false, false, false]])