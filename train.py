# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    train.py                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: obelouch <obelouch@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/12/13 03:23:06 by obelouch          #+#    #+#              #
#    Updated: 2020/12/14 02:08:00 by obelouch         ###   ########.fr        #
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
import  re


# Error Macros:
ERROR_FLAG = 1
ERROR_ARGC = 2

# Algorithm Variables:
algo = 'BGD'
alpha = 0.01


def     set_ALGOandLR(res_algo, res_alpha):
    '''
    Set the Algorithm and Learning Rate depend on the flag
    '''
    global  algo
    global  alpha

    if res_algo:
        algo = res_algo.group()
    if res_alpha:
        alpha = float(res_alpha.group())
    if alpha > 1:
        print('The Gradient Discent Diverge with this learning rate value!')
        print('Setting the default value: 0.01')
        alpha = 0.01


def     exit_usage(error):
    if error == ERROR_ARGC:
        print('Error: Wrong number of arguments!')
    if error == ERROR_FLAG:
        print('Error: Wrong flag!')
    print('\nUsage: python3 train.py [-BGD | -SGD | -LS][{< alpha >}]')
    print('  SGD: Stochastic Gradient Descent')
    print('  BGD: Batch Gradient Descent')
    print('  LS: Least Squares')
    print('  alpha: learning rate < 1')
    exit(1)


def     pick_algo():
    '''
    Check the argument and Pick an algo depend on the flag
    '''
    # Check if nbr of args > 2
    if len(sys.argv) > 2:
        exit_usage(ERROR_ARGC)
    flag = sys.argv[1] 
    # Check syntax of the flag
    if not re.match(r'^-(BGD|SGD|LS)(\{[0-9]+(\.[0-9]+)?\})?$', flag):
        exit_usage(ERROR_FLAG)
    # Set the variables: algo, alpha
    set_ALGOandLR(
        # algo part from the flag 
        re.search(r'[A-Z]+', flag),
        # alpha part from the flag 
        re.search(r'[0-9]+(\.[0-9]+)?', flag),
    )


def     get_theta(norm_X, norm_Y):
    '''
    Get Theta0, Theta1 depend of the choosed Algorithm
    '''
    if algo == 'SGD':
        return sgd(norm_X, norm_Y, alpha)
    if algo == 'LS':
        return least_square(norm_X, norm_Y)
    return bgd(norm_X, norm_Y, alpha)


def     print_loading():
    '''
    Print The Loading Message depend on the Algo type
    '''
    print('\nTraining using ', end='')
    if algo == 'SGD':
        print('Stochastic Gradient Descent Algorithm ....\n')
    elif algo == 'LS':
        print('Least Squares Algorithm ....\n')
    else:
        print('Batch Gradient Descent Algorithm ....\n')


def     train_model():
    '''
    Train the univariable linear regression model with the dataset
    '''
    if len(sys.argv) > 1:
        pick_algo()
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
    print_loading()
    theta = get_theta(norm_X, norm_Y)
    # Adapt the Theta to the Denormalization
    theta[1] = theta[1] * maxPrice / maxKm
    theta[0] = theta[0] * maxPrice
    # Write Thetas in params file
    write_params(theta)
    print('Training DONE ✅\n')
    print_precision(theta, X, Y)


# Launch the program
train_model()