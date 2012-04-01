#!/usr/bin/env python

def mew(l, n, m):
    """ l = list of ints
        n = number of list members to skip
        m = multiplier 
    """
    for i in range(0, len(l), n):
        l[i] = l[i] * m
    return l

def summer(l):
    """ Pypy does not support sum()
    """
    ans = 0
    for i in l:
        ans += i
    return ans

def main(args):
    d = mew(range(int(args[1])), int(args[2]), int(args[3]))
#    print summer(d)
#    print sum(d)
    return 0

def target(*args):
    return main, None

if __name__ == "__main__":
    import sys
    main(sys.argv)

