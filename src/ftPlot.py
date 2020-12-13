# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ftPlot.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: obelouch <obelouch@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/12/13 18:58:57 by obelouch          #+#    #+#              #
#    Updated: 2020/12/13 19:01:08 by obelouch         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import  matplotlib.pyplot as plt
import  numpy as np

def     scatter_plot(df, title, x_dim, y_dim):
    '''
    Ax of the scatter plot for a given DataFrame
    '''
    fig, ax = plt.subplots(figsize=(12, 8))
    # Set Figure Title
    fig.canvas.set_window_title(title)
    # Draw points
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