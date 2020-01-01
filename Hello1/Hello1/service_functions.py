
import pandas as pd
import matplotlib.pyplot as plt
import os

import io
import base64
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure


def plot_series():
    print("Running from plot_series()")
    d = {1:1 , 2:4 , 3:9 , 4:16}
    s = pd.Series(d)
    fig = plt.figure()
    ax = fig.add_subplot(111)
    s.plot(ax=ax,  kind = 'line', title = 'yPlot', figsize = (6, 6), fontsize = 22, style = 'r2-.')
    pngImage = io.BytesIO()
    FigureCanvas(fig).print_png(pngImage)
    pngImageB64String = "data:image/png;base64,"
    pngImageB64String += base64.b64encode(pngImage.getvalue()).decode('utf8')
    return pngImageB64String


def plot_series_bar():
    print("Running from plot_series()")
    d = {1:1 , 2:4 , 3:9 , 4:16 , 5:25 , 6:16 , 7:9 , 8:4 , 9:1}
    s = pd.Series(d)
    fig = plt.figure()
    ax = fig.add_subplot(111)
    s.plot(ax=ax,  kind = 'bar', title = 'barPlot', figsize = (24, 6), fontsize = 22)
    pngImage = io.BytesIO()
    FigureCanvas(fig).print_png(pngImage)
    pngImageB64String = "data:image/png;base64,"
    pngImageB64String += base64.b64encode(pngImage.getvalue()).decode('utf8')
    return pngImageB64String