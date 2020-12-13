# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    visualizer.py                                      :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: obelouch <obelouch@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/12/13 03:37:21 by obelouch          #+#    #+#              #
#    Updated: 2020/12/13 19:35:28 by obelouch         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #


from src.ftPlot import scatter_plot, line_plot
from src.csv_tools import df_fromCSV
from src.params import get_params
import  matplotlib.pyplot as plt


def     visualizer():
    '''
    Visualization of the Dataset and the Hypothesis if the model is trained
    '''
    df = df_fromCSV('Data/data.csv')
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


# Launch the program
visualizer()