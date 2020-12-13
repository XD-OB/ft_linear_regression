# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    train.py                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: obelouch <obelouch@student.1337.ma>        +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/12/13 03:23:06 by obelouch          #+#    #+#              #
#    Updated: 2020/12/13 03:23:06 by obelouch         ###   ########.ma        #
#                                                                              #
# **************************************************************************** #
#!/usr/bin/env python3

import  src.ftMath as myMath
import  pandas as pd
import  numpy as np

# Min Step for gradient descent
MIN_STEP = 0.000000001

def     write_params(theta):
    '''
    Write Theta0, Theta1 in the params file
    '''
    fd = open('Data/params', 'w')
    fd.write(f'{theta[0]} {theta[1]}')
    # Close the file
    fd.close()


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
    print(theta[1], theta[0]) ########################
    theta[1] = theta[1] * maxPrice / maxKm
    theta[0] = theta[0] * maxPrice
    return theta


def     calculate_MAPE(theta, X, Y):
    '''
    Mean absolute percentage error (is the percentage equivalent of MAE)
    '''
    mape_sum = 0
    for predict, y in zip(h(theta, X), Y):
        mape_sum += myMath.ft_abs(y - predict) / y
    mape = mape_sum / Y.shape[0]
    return mape


def     train_model():
    '''
    Train the univariable linear regression model with the dataset
    '''
    df = pd.read_csv('Data/data.csv')
    Y = np.array(df['price'])
    X = np.array(df['km'])
    # Gradient Descent
    theta = gradient_descent(X, Y, 0.01)
    print(theta) ########################################
    # Write Thetas in params file
    write_params(theta)
    if True:#is_showPrecision:
        m_a_p_e = calculate_MAPE(theta, X, Y)
        print(f'mape= {m_a_p_e}')


train_model()