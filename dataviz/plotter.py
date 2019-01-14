# -*- coding: utf-8 -*-
"""
Created on Mon Jan 14 11:14:17 2019

@author: Subea
"""

from bokeh.plotting import figure
from bokeh.io import show, output_file
from bokeh.models import FactorRange, ColumnDataSource
from bokeh.models.tools import HoverTool

def plot_vbars(out, x, y, title="", yaxis_label="", xaxis_label="", hover_x="", hover_y=""):
    """
    A function that takes in lists of corresponding x and y values from a DataFrame and plots them into an interactive vertical bar graph. 
    
    Parameters
    ----------------------------------------------------
    out : output filename (i.e. 'plot.html')
    x : list of index values for x-axis
    y : list of number type values for y-axis
    title : title of plot/graph
    yaxis_label : a string type y-axis label 
    xaxis_label : a string type y-axis label
    hover_x : a string type hover name for x values
    hover_y : a string type hover name for y values
    
    Returns
    ----------------------------------------------------
    An interactive vertical bar graph in html format
    """
    
    output_file(out)

    x_val = x
    y_val = y
    
    p = figure(x_range=x_val, plot_height=500, plot_width=700, title=title,
               toolbar_location=None, tools="")
    
    source = ColumnDataSource(data=dict(x=x_val, y=y_val))
    
    p.vbar(x='x_val', top='y_val', width=0.9, source=source)
    
    p.xgrid.grid_line_color = None
    p.xaxis.axis_label = xaxis_label
    p.yaxis.axis_label = yaxis_label
    p.y_range.start = 0
    
    
    hover = HoverTool()
    hover.tooltips=[
        (hover_x, '@x_val'),
        (hover_y, '@y_val')
    ]

    p.add_tools(hover)
    
    show(p)  
  

def plot_vbars_q(out, f, y, title="", trend='mean', yaxis_label="", xaxis_label="", hover_x="", hover_y=""):
    """
    A function that takes in lists of corresponding x and y values from a DataFrame and plots them into an interactive quarterly vertical bar graph. 
    
    Parameters
    ----------------------------------------------------
    out : output filename (i.e. 'plot.html')
    f : list of index values for x-axis
    y : list of number type values for y-axis
    trend: per quarter; default='mean', other valid inputs are 'min' and 'max'
    title : title of plot/graph
    yaxis_label : a string type y-axis label 
    xaxis_label : a string type y-axis label
    hover_x : a string type hover name for x values
    hover_y : a string type hover name for y values
    
    Returns
    ----------------------------------------------------
    An interactive vertical bar graph for quarterly analysis in html format
    """
    
    output_file(out)

    factors = [
        ("Q1", f[0]), ("Q1", f[1]), ("Q1", f[2]),
        ("Q2", f[3]), ("Q2", f[4]), ("Q2", f[5]),
        ("Q3", f[6]), ("Q3", f[7]), ("Q3", f[8]),
        ("Q4", f[9]), ("Q4", f[10]), ("Q4", f[11]),
    ]
    
    p = figure(x_range=FactorRange(*factors), plot_height=500, plot_width=700, title=title,
               toolbar_location=None, tools="")
    
    y_val = y
    
    source = ColumnDataSource(data=dict(x=factors, y=y_val))
    
    p.vbar(x='x', top='y', width=0.9, alpha=0.5, source=source)
    if trend=='min':
        y1 = y[0:2].min()
        y2 = y[3:5].min()
        y3 = y[6:8].min()
        y4 = y[9:11].min()
        p.line(x=["Q1", "Q2", "Q3", "Q4"], y=[y1, y2, y3, y4], color="yellow", line_width=2)
    elif trend=='max':
        y1 = y[0:2].max()
        y2 = y[3:5].max()
        y3 = y[6:8].max()
        y4 = y[9:11].max()
        p.line(x=["Q1", "Q2", "Q3", "Q4"], y=[y1, y2, y3, y4], color="green", line_width=2)
    else:   
        y1 = y[0:2].mean()
        y2 = y[3:5].mean()
        y3 = y[6:8].mean()
        y4 = y[9:11].mean()
        p.line(x=["Q1", "Q2", "Q3", "Q4"], y=[y1, y2, y3, y4], color="red", line_width=2)
    
    p.y_range.start = 0
    p.yaxis.axis_label = yaxis_label
    p.xaxis.axis_label = xaxis_label
    p.x_range.range_padding = 0.1
    p.xaxis.major_label_orientation = 1
    p.xgrid.grid_line_color = None
    
    hover = HoverTool()
    hover.tooltips=[
            (hover_x, '@x'),
            (hover_y, '@y')
        ]

    p.add_tools(hover)

    show(p)  


def plot_hbar(out, df, val_col, sort_by="", title="", yaxis_label="", xaxis_label="", hover_x="", hover_y=""):
    """
    A function that takes in lists of corresponding x and y values from a DataFrame and plots them into an interactive vertical bar graph. 
    
    Parameters
    ----------------------------------------------------
    out : output filename (i.e. 'plot.html')
    df : input DataFrame
    sort_by : string column name which the sort will base on
    val_col : string column name of number values for plotting
    title : title of plot/graph
    yaxis_label : a string type y-axis label 
    xaxis_label : a string type y-axis label
    hover_x : a string type hover name for x values
    hover_y : a string type hover name for y values
    
    Returns
    ----------------------------------------------------
    An interactive horizontal bar graph in html format
    """

    output_file(out)
    
    sample = df.sort_values(sort_by)
    
    p = figure(y_range=list(sample.index), plot_width=1000, plot_height=1500, title=title)
    
    source = ColumnDataSource(data=dict(x=list(sample[val_col]), y=sample.index))
    
    p.hbar(y='y', height=0.5, left=0,
           right='x', color="green", source=source)
    
    p.x_range.start = 0
    p.xaxis.axis_label = xaxis_label
    p.yaxis.axis_label = yaxis_label
    p.y_range.range_padding = 0.01
    p.yaxis.major_label_orientation = 1
    p.yaxis.axis_label_text_font_size = "10pt"
    p.yaxis.major_label_orientation = 'horizontal'
    p.ygrid.grid_line_color = None
    
    hover = HoverTool()
    hover.tooltips=[
            (hover_y, '@y'),
            (hover_x, '@x')
        ]
    p.add_tools(hover)

    show(p)