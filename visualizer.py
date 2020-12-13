# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    visualizer.py                                      :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: obelouch <obelouch@student.1337.ma>        +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/12/13 03:37:21 by obelouch            #+#    #+#            #
#    Updated: 2020/12/13 03:37:21 by obelouch           ###   ########.ma      #
#                                                                              #
# **************************************************************************** #
#!/usr/bin/env python3

from src.get_params import get_params
import  matplotlib.pyplot as plt
import  pandas as pd
import  numpy as np


def     scatter_plot(df, title, x_dim, y_dim):
    '''
    Ax of the scatter plot for a given DataFrame
    '''
    fig, ax = plt.subplots(figsize=(12, 8))
    ax.scatter(
        x=df[x_dim],
        y=df[y_dim],
        c='Blue',
    )
    # Set Title
    ax.set_title(title)
    # Removing top and right borders
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    # Adds major gridlines
    ax.grid(color='grey', linestyle='-', linewidth=0.25, alpha=0.5)
    #####################

def     line_plot(y, start, stop):
    '''
    Draw A line in a plot
    ''' 
    x = np.linspace(
        start=start,
        stop=stop,
        num=stop-start,
    )
    plt.plot(x, y(x), '-r')


def     visualizer():
    '''
    Visualization of the Dataset and the Hypothesis if the model is trained
    '''
    df = pd.read_csv('Data/data.csv')
    # Data Plot
    scatter_plot(
        df,
        'Price of a car for a given mileage',
        'km',
        'price',
    )
    #####################
    theta = get_params()
    line_plot(
        lambda x: theta[0] + x * theta[1],
        start=0,
        stop=250000,
    )
    plt.show()


visualizer()