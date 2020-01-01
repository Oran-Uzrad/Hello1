"""
Routes and views for the flask application.
"""

from datetime import datetime
from flask import render_template
from flask import request
from flask import redirect
from flask import make_response
from Hello1 import app
from flask_bootstrap import Bootstrap
from flask_moment import Moment
import pandas as pd
import matplotlib.pyplot as plt
import os

import io
import base64

import Hello1.service_functions
from Hello1.service_functions import plot_series
from Hello1.service_functions import plot_series_bar

from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure


bootstrap = Bootstrap(app)
moment = Moment(app)



@app.route('/')
@app.route('/home')
def home():
    print("Running from home()")
    return render_template('index.html',current_time=datetime.utcnow())
    
@app.route('/gallery')
def gallery():
    print("Running from gallery()")
    return render_template('Gallery.html')

@app.route('/project')
def project():
    print("Running from gallery()")
    return render_template('project.html')

@app.route('/rawdata')
def rawdata():
    print("Running from rawdata()")
    df = pd.read_excel('GSAF5.xls')
    df_short = df[0:100]
    return render_template('rawdata.html', raw_data_table=df_short.to_html(classes = 'table table-hover'))

@app.route('/plot')
def plot():
    print("Running from plot()")
    # plot_image = plot_series()
    return render_template('plot.html', 
                           src = plot_series(),
                           src_bar = plot_series_bar())

@app.route('/user/<name>')
def user(name):
    print("Running user3c")
    return render_template('user3c.html', name=name)

@app.route('/cookie')
def cookie():
    resp = make_response('<h3> This document carries a cookie </h3>')
    resp.set_cookie('answer', '42')
    print("cockie is running")
    return resp

@app.route('/elsewhere')
def elswhere():
    return redirect('https://www.yahoo.com/')

@app.before_request
def before_func():
    print("before_func is running")

@app.after_request
def after_func(response):
    print("after_func is running")
    return response

@app.before_first_request
def before_first_func():
    print("before_first_func is running")



@app.teardown_request
def teardown_func(error = None):
    print("teardown_func is running")


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500