# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    train.py                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: obelouch <obelouch@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/12/13 03:23:06 by obelouch          #+#    #+#              #
#    Updated: 2020/12/13 20:55:56 by obelouch         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from src.algos import least_square, bgd, sgd
from src.precision import print_precision
from src.csv_tools import df_fromCSV
from src.params import write_params
import  src.ftMath as myMath
import  pandas as pd
import  numpy as np
import  sys

# Macros:
BGD = 0
SGD = 1
LS = 2

# Algorithm Variables:
algo = BGD
learning_rate = 0.01


def     pick_algo():
    '''
    Pick an algo depend on the flag
    '''
    # Check if nbr of args > 2
    if len(sys.argv) > 2:
        print('error')
        exit(1)
    # Apply fonction only if nbr of args == 2
    if len(sys.argv) == 2:
        flag = sys.argv[1]
        # Check syntax of the flag
        if True:
            pass



def     train_model():
    '''
    Train the univariable linear regression model with the dataset
    '''
    # Read Dataset CSV File 
    df = df_fromCSV('Data/data.csv')
    Y = np.array(df['price'])
    X = np.array(df['km'])
    # Normalize X and Y:
    maxKm = myMath.ft_max(X)
    maxPrice = myMath.ft_max(Y)
    devide_x = lambda x: x / maxKm
    devide_y = lambda y: y / maxPrice
    norm_X = np.array([devide_x(x) for x in X])
    norm_Y = np.array([devide_y(y) for y in Y])
    # Apply Algorithm
    theta = sgd(norm_X, norm_Y, 0.01)
    # Adapt the Theta to the Denormalization
    theta[1] = theta[1] * maxPrice / maxKm
    theta[0] = theta[0] * maxPrice
    # Write Thetas in params file
    write_params(theta)
    print_precision(theta, X, Y)


# Launch the program
train_model()