

def move(n, src, temp ,dest):
    if n > 0: 
        move(n-1, src, dest, temp)
        print("move %d from %c to %c" % (n,src,dest))
        move(n-1, dest, temp, src)


move(3,'a','b','c')