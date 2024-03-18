import sys
sys.setrecursionlimit(10**6)


def pow(n):
    if n == 0:
        return 1 
    else: 
        return 2 * pow(n-1)

print(pow(100))