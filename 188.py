tri = [int((n*(n+1))/2) for n in range(45, 141)]
squ = [n**2 for n in range(32,99)]
pen = [int((n*(3*n-1))/2) for n in range(26, 82)]
hex = [n*(2*n-1) for n in range(23, 71)]
hep = [int((n*(5*n-3))/2) for n in range(21, 64)]
oct = [n*(3*n-2) for n in range(19, 59)]

for a in tri:
    dig1 = list(str(a))
    for b in squ:
        dig2 = list(str(b))
        if (dig1[2:]!=dig2[:2]):
            break
        for c in pen:
            dig3 = list(str(c))
            if (dig2[2:]!=dig3[:2]):
                break
            for d in hex:
                dig4 = list(str(d))
                if (dig3[2:]!=dig4[:2]):
                    break
                for e in hep:
                    dig5 = list(str(e))
                    if (dig4[2:]!=dig5[:2]):
                        break
                    for f in oct:
                        dig6 = list(str(f))
                        if (dig1[2:]==dig2[:2] and dig2[2:]==dig3[:2] and dig3[2:]==dig4[:2] and dig4[2:]==dig5[:2] and dig5[2:]==dig6[:2] and dig6[2:]==dig1[:2]):
                            print(a)
                            print(b)
                            print(c)
                            print(d)
                            print(e)
                            print(f)
        