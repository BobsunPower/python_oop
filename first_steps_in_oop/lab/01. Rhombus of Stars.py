nbr = int(input())
dwn = nbr
for row in range(1, 2 * nbr):
    if row <= nbr:
        print(" " * (nbr - row) + "* " * row)
    else:
        dwn -= 1
        print(" " * (row - nbr) + "* " * dwn)
