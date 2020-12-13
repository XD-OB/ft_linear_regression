# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    algos.py                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: obelouch <obelouch@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/12/13 19:05:17 by obelouch          #+#    #+#              #
#    Updated: 2020/12/13 21:00:08 by obelouch         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import  src.ftMath as myMath
import  numpy as np

################################################################################
######################   Batch Gradient Descent   ##############################
################################################################################

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


def     bgd(X, Y, alpha):
    '''
    Implementation of the Batch Gradient Descent Algorithm
    alpha: Learning rate
    '''
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
    return theta



################################################################################
##########################   Stochastic Descent   ##############################
#
# In Batch Gradient Descent, we use the whole training data per epoch whereas,
# in Stochastic Gradient Descent, we use only single training example per epoch
# and Mini-batch Gradient Descent lies in between of these two extremes,
# in which we can use a mini-batch(small portion) of training data per epoch
#
################################################################################

def     sgd(X, Y, alpha):
    '''
    Implementation of the Stochastic Gradient Descent Algorithm
    alpha: Learning rate
    '''
    m = Y.shape[0]
    theta = [0, 0]
    error = 100000
    while True:
        prev_error = error
        for i in range(m):
            pred = theta[0] + theta[1] * X[i]
            error = pred - Y[i]
            theta[1] -= alpha * error * X[i]
            theta[0] -= alpha * error
        if abs(error - prev_error) < MIN_STEP:
            break
    return theta



################################################################################
###########################   Least Squares   ##################################
#
# The method of least squares is a standard approach in regression analysis to
# approximate the solution of overdetermined systems by minimizing the sum of
# the squares of the residuals made in the results of every single equation
#
################################################################################

def     least_square(X, Y):
    '''
    Implementation of the Least Square Algorithm
    '''
    # Means ###
    x_mean = myMath.ft_mean(X)
    y_mean = myMath.ft_mean(Y)
    ###########
    theta = [0, 0]
    theta[1] = np.transpose(X - x_mean).dot(Y - y_mean) / np.transpose(X - x_mean).dot(X - x_mean)
    theta[0] = y_mean - theta[1] * x_mean
    return theta