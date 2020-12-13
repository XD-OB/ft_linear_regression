# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    algos.py                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: obelouch <obelouch@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/12/13 19:05:17 by obelouch          #+#    #+#              #
#    Updated: 2020/12/13 19:08:56 by obelouch         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import  src.ftMath as myMath
import  numpy as np

###########################################################################
####################### GRADIENT Descent Algorithm ########################
###########################################################################

# Min Step for gradient descent
MIN_STEP = 0.000000001

def     h(theta, X):
    '''
    Hypothesis of the Vector X
    '''
    return theta[0] + theta[1] * X


def     J(theta, X, Y):
    '''
    Cost fonction
    '''
    m = Y.shape[0]
    error_array = myMath.ft_arraySquare(h(theta, X) - Y)
    return myMath.ft_arraySum(error_array / (2 * m))


def     gradient_descent(X, Y, alpha):
    '''
    Implementation of Gradient Descent
    alpha: Learning rate
    '''
    # Normalize X and Y:
    maxKm = myMath.ft_max(X)
    maxPrice = myMath.ft_max(Y)
    devide_x = lambda x: x / maxKm
    devide_y = lambda y: y / maxPrice
    X = np.array([devide_x(x) for x in X])
    Y = np.array([devide_y(y) for y in Y])
    ######################
    m = Y.shape[0]
    theta = [0, 0]
    error = 100000
    while True:
        delta_J = [0, 0]
        prev_error = error
        error = myMath.ft_arraySum(h(theta, X) - Y)
        delta_J[0] = error
        delta_J[1] = np.transpose(h(theta, X) - Y).dot(X)
        theta[0] -= (alpha / m) * delta_J[0] 
        theta[1] -= (alpha / m) * delta_J[1] 
        if abs(error - prev_error) < MIN_STEP:
            break
    # Adapt the Theta to the Denormalization
    theta[1] = theta[1] * maxPrice / maxKm
    theta[0] = theta[0] * maxPrice
    return theta