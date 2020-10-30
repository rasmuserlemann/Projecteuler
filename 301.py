def is_square(integer):
    root = math.sqrt(integer)
    return integer == int(root + 0.5) ** 2

for a in range(101):
    for b in range(101):
        for c in range(101):
            for d in range(101):
                