import csv
import io
import random
from flask import Flask
from flask import Response, request, render_template
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
import matplotlib
from matplotlib.ticker import MultipleLocator
import numpy as np
import pandas as pd

app = Flask(__name__)

@app.route('/')
def index():
    return 'OK'

@app.route('/plot.png')
def plot_png():
    fig = create_heatmap()
    output = io.BytesIO()
    FigureCanvas(fig).print_png(output)
    return Response(output.getvalue(), mimetype='image/png')
    
def read_csv(filename):
    matrix = []
    with open(filename) as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            new_row = [float(value) for value in row]
            print(new_row)
            matrix.append(new_row)
    return np.array(matrix)

def create_heatmap():
    a = read_csv('plot.csv')
    cmap = matplotlib.colors.LinearSegmentedColormap.from_list('', ['#ff3d3d', 'yellow', '#74ff52'])
    norm = matplotlib.colors.TwoSlopeNorm(vcenter=2.30, vmin=a.min(), vmax=a.max())

    fig, ax = plt.subplots()
    img = ax.imshow(a, interpolation='none', cmap=cmap, norm=norm)
    ax.xaxis.set_major_locator(MultipleLocator(1))
    ax.yaxis.set_major_locator(MultipleLocator(1))
    plt.colorbar(img, ax=ax)
    plt.tight_layout()
    return fig

if __name__ == '__main__':
   app.run(host='0.0.0.0')
