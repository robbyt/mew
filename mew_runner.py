#!/usr/bin/env python
import csv
import subprocess
import timeit
import time

MEW = 'bin/mew_nosum_precise_x64.bin'

DATA_TARGETS = [
    64*1024,
    64*1024*2,
    64*1024*4,
    64*1024*8,
    64*1024*16,
    64*1024*32,
    64*1024*64,
    64*1024*128,
    64*1024*256,
]
#SKIPS = [1, 2, 4, 8, 16, 32, 64, 128, 256]
SKIPS = range(1,769)

MULTI = 3
REPEAT = 100

CSV_TARGET = "out.csv"


def _timer(stmt, setup="import subprocess", repeat=5):
#    print "running timer for {0}".format(stmt)
    return timeit.repeat(stmt=stmt, setup=setup, number=1, repeat=repeat)

def _mew_it(d,n,m=MULTI):
    """ d = base data to create range in mew
        n = number of members to skip
        m = multiple

        this returns a string, that will be run inside the _timer function
    """
 #   print "building a mew string"
    return "subprocess.call(['{0}', '{1}', '{2}', '{3}'])".format(MEW, d, n, m)
    
def data_cleaner(l,n=3):
    """Sort the list, take the n-number of fastest, then avg them and return
    """
    sum_data = 0
    l.sort()

    # make sure the len of the list is larger than the minimum number of datapoints
    assert(len(l) >= n)

    for i in range(n):
        sum_data += l[i]

    return sum_data / n

def do_it(fp):
    csv_file = csv.writer(fp)
    csv_file.writerow(['data', 'skip', 'time']) # header

    for d in DATA_TARGETS:
#        print "starting loop for " + str(d)
        for n in SKIPS:
#            print "starting loop for " + str(n)
            t = _timer(_mew_it(d, n))

            avg = data_cleaner(t)

            out_list = [d, n, avg]
            print out_list

            csv_file.writerow(out_list)
#            time.sleep(1)
            fp.flush()


def main():
    fp = open(CSV_TARGET, 'wb')
    do_it(fp)
    fp.close()


if __name__ == '__main__':
    main()
