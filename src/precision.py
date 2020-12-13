# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    precision.py                                       :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: obelouch <obelouch@student.1337.ma>        +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/12/13 22:04:59 by obelouch          #+#    #+#              #
#    Updated: 2020/12/13 22:04:59 by obelouch         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import  src.ftMath as myMath
from src.algos import h

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
