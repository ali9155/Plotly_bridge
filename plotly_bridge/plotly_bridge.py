"""
    Example showing how to share data on the web using the Plot.ly
    web graphing service.
    
    To run this example, you'll first need to install the "plotly" Python
    package. You can do this from the Canopy Package Manager, which can be
    launched from the Canopy welcome screen.

    You will also need to set up a Plot.ly account.  Here's how:
    
    https://plot.ly/python/getting-started/
    
    This module defines one function, which takes an array of data from
    LabVIEW, along with a string name, and packages the data up to send
    to the Plot.ly service.
"""

# Import a few packages so we can use their functionality.
# The main one here is "plotly", which provides Python functions that talk to
# the plot.ly web service.

import sys

import numpy as np
import plotly.plotly as py
from plotly.graph_objs import Scatter, Data


def post_to_plotly(data, name):
    """ Make and share an X-Y graph using the Plot.ly web service.
    
    The "plotly" package will also attempt to open the default web browser
    when finished so we can see our data on the Web.
    
    data: A NumPy array, from LabVIEW, with the data to plot
    name: A string giving the name of the plot.
    """
    
    # Plotly wants both X and Y coordinates.  So we auto-generate an array
    # with values 0, 1, 2... etc., up to the number of elements in "data"
    x = np.arange(len(data))
    
    # Send the plot request to the Plot.ly web service, and open a browser
    # window to view the data
    py.plot(Data([Scatter(x=x, y=data)]), filename=name.decode('ascii'))