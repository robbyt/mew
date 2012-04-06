#!/usr/bin/env python
import matplotlib
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure

import matplotlib.colors 

import matplotlib.mlab as mlab
import numpy as np

import csv

LOG_X = True

_bad_colors = ['oldlace',
               'whitesmoke',
               'lightsteelblue', 
               'azure', 
               'beige', 
               'lavenderblush', 
               'lightyellow']

COLORS = matplotlib.colors.cnames.keys()
for b in _bad_colors:
    COLORS.remove(b)

# help from: 
# http://www.prettygraph.com/blog/how-to-plot-a-scatter-plot-using-matplotlib/

def index_finder(l):
    prev = 0
    indexes = []
    for r in l:
        if r[0] == prev:
    #        print r
            pass
        else:
            indexes.append(r[0])
    #        print r
        prev = r[0]
    return indexes

def range_size(data_set):
    """ From some basic benchmarks, it takes about 2097224 bytes to 
        store a list of 65536 ints
    """
    a = int(data_set) / 65536 * 2097224

    #return  str(mem_count.asizeof(range(int(data_set)))) +"_bytes"
    return str(a) + "_bytes" 

def chart_it(csv_r, chart_name='mew', color='red', point_size=0.5):
    fig = Figure(figsize=(15,8))

    # Create a canvas and add the figure to it.
    canvas = FigureCanvas(fig)

    # Create a subplot.
    ax = fig.add_subplot(111)

    # Set the title.
    ax.set_title(chart_name, fontsize=14)

    # Set the X Axis label.
    ax.set_xlabel("Number of list members skiped in multiplication",
                  fontsize=12)

    # Set the Y Axis label.
    ax.set_ylabel("Avg. Compute Time", fontsize=12)

    # Display Grid.
    ax.grid(True, linestyle='-', color='0.75')

#    colors = 100*np.random.random(100).tolist()
    # Generate the Scatter Plot.
    for i in csv_r:
        a = np.array(i[0])
        print "graphing: " + str(i[1])
        skips = np.float64(a[:,1])
        time = np.float64(a[:,2])
        c = COLORS.pop()
        print c
        ax.scatter(skips, 
                   time,
                   s=point_size,
                   label=range_size(i[1]),
                   color=c)

        ax.legend()
        ax.set_xlim(left=0,right=800)
        if LOG_X:
            ax.set_xscale('log')
        canvas.print_figure(i[1] + ".png", dpi=300)


    # Save the generated Scatter Plot to a PNG file.
#    canvas.print_figure(file_name.split('.')[0] + ".png", dpi=700)

    ax.legend()

    canvas.print_figure(chart_name + ".png", dpi=300)


def csv_data_summon(fp):
    l = [r for r in csv.reader(fp)]
    # skip the first row
    return l[1:]

def chart_prep(indexes, csv_data_list, file_name):
    colors = 100*np.random.random(100).tolist()
    l = []
    for my_index in indexes:
        my_index_list = []
        for csv_data_chunk in csv_data_list:
            if csv_data_chunk[0] == my_index:
                my_index_list.append(csv_data_chunk)
        #l.append(my_index_list, file_name, colors.pop()))
        l.append((my_index_list, my_index, colors.pop()))
    return l



def main(args):
    # remove the first arg, the name of this script
    args.remove(args[0])

    for file_name in args:
        # grab a file pointer for each arg
        fp = open(file_name, 'rb')

        # read the csv file in, return back a big list of all rows from the 
        # csv (each row is a dict)
        csv_data_list = csv_data_summon(fp)

        # read the 'data' value from each row, and create an index of unique 
        # data values
        indexes = index_finder(csv_data_list)

        # create a packed list, that contains the segmented csv data, the 
        # filename_indexname,
        l = chart_prep(indexes, csv_data_list, file_name)

    chart_it(l)

    return 0

if __name__ == "__main__":
    import sys
    main(sys.argv)
