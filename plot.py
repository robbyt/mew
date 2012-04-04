#!/usr/bin/env python
import matplotlib
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure
import matplotlib.mlab as mlab
import numpy as np

import csv

# help from: 
# http://www.prettygraph.com/blog/how-to-plot-a-scatter-plot-using-matplotlib/

def index_finder(l):
    prev = 0
    indexes = []
    for r in l:
        if r['data'] == prev:
            print r
        else:
            indexes.append(r['data'])
            print r
        prev = r['data']
    return indexes


def chart_it(csv_r, chart_name='mew', color='red', point_size=0.1):
    fig = Figure(figsize=(15,8))

    # Create a canvas and add the figure to it.
    canvas = FigureCanvas(fig)

    # Create a subplot.
    ax = fig.add_subplot(111)

    # Set the title.
    ax.set_title(chart_name, fontsize=14)

    # Set the X Axis label.
    ax.set_xlabel("Number of list members skiped in multiplication",fontsize=12)

    # Set the Y Axis label.
    ax.set_ylabel("Avg. Compute Time", fontsize=12)

    # Display Grid.
    ax.grid(True, linestyle='-', color='0.75')

    # Generate the Scatter Plot.
    for i in csv_r:
        a = np.array(i)
        ax.scatter(a[0][1], a[0][2], s=point_size, color=i[2], label=i[1])
        assert(False)

    # Save the generated Scatter Plot to a PNG file.
#    canvas.print_figure(file_name.split('.')[0] + ".png", dpi=700)

    ax.legend()

    canvas.print_figure(chart_name + ".png", dpi=700)


def csv_data_summon(fp):
    return [r for r in csv.DictReader(fp)]

def chart_prep(indexes, csv_data_list, file_name):
    colors = 100*np.random.random(100).tolist()
    l = []
    for my_index in indexes:
        my_index_list = []
        for csv_data_chunk in csv_data_list:
            if csv_data_chunk['data'] == my_index:
                my_index_list.append(csv_data_chunk)
        #l.append(my_index_list, file_name, colors.pop()))
        l.append((my_index_list, "{0}_{1}".format(file_name, my_index), colors.pop()))
    return l



def main(args):
    # remove the first arg, the name of this script
    args.remove(args[0])

#    colors = ['b', 'g', 'r', 'c', 'm', 'y', 'k']

    for file_name in args:
        fp = open(file_name, 'rb')
        csv_data_list = csv_data_summon(fp)
        indexes = index_finder(csv_data_list)
        l = chart_prep(indexes, csv_data_list, file_name)

#        l.append((mlab.csv2rec(file_name), file_name, colors.pop()))

    chart_it(l)

    return 0

if __name__ == "__main__":
    import sys
    main(sys.argv)
