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

from src.algos import least_square, bgd, sgd, h
from src.csv_tools import df_fromCSV
from src.params import write_params
import  src.ftMath as myMath
import  pandas as pd
import  numpy as np


def     print_precision(theta, X, Y):
    '''
    Print the precision of the Algorithm using:
    MAPE : Mean absolute percentage error (is the percentage equivalent of MAE)
    RMSE : Root of Mean Squared Error
           (is the average of the squares of the difference between observed and predicted values)
    MAE: Mean Absolute Error
         (It’s the average over the test sample of the absolute differences between prediction and actual observation)
    '''
    mape = 0
    rmse = 0
    mae = 0
    for predict, y in zip(h(theta, X), Y):
        mape += myMath.ft_abs(y - predict) / y
        rmse += (y - predict) ** 2
        mae += myMath.ft_abs(y - predict)
    # MAPE calculate the error in percente
    mape = round(100 - (100 * mape / Y.shape[0]), 4)
    # RMSE calculate
    rmse = round((rmse / Y.shape[0]) ** 0.5, 4)
    # MAE calculate
    mae = round(mape / Y.shape[0], 4)
    print('\nTraining DONE!\n')
    print('Precision of the algorithm using:')
    print(f'MAPE: {mape} %')
    print(f'RMSE: {rmse}')
    print(f'MAE: {mae}')
    

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