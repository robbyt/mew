#!/usr/bin/env python
import matplotlib
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure
import matplotlib.mlab as mlab

# help from: 
# http://www.prettygraph.com/blog/how-to-plot-a-scatter-plot-using-matplotlib/

def chart_it(csv_r, chart_name='mew', color='red'):
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
        ax.scatter(i[0].skip, i[0].time, s=0.1, color=i[2], label=i[1])

    # Save the generated Scatter Plot to a PNG file.
#    canvas.print_figure(file_name.split('.')[0] + ".png", dpi=700)

    ax.legend()

    canvas.print_figure(chart_name + ".png", dpi=700)



    
def main(args):
    # remove the first arg, the name of this script
    args.remove(args[0])

    colors = ['b', 'g', 'r', 'c', 'm', 'y', 'k']
    l = []
    for file_name in args:
        l.append((mlab.csv2rec(file_name), file_name, colors.pop()))

    chart_it(l)

    return 0

if __name__ == "__main__":
    import sys
    main(sys.argv)
