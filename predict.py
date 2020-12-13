# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    predict.py                                         :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: obelouch <obelouch@student.1337.ma>        +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/12/13 00:36:02 by obelouch          #+#    #+#              #
#    Updated: 2020/12/13 00:36:02 by obelouch         ###   ########.ma        #
#                                                                              #
# **************************************************************************** #
#!/usr/bin/env python3

from src.get_params import get_params
from src.ftMath import ft_isFloat


def     predict(): 
    '''
    The Predict program
    '''
    user_input = None
    while not ft_isFloat(user_input):
        user_input = input('Please enter a mileage: ')
    mileage = float(user_input)
    print("mileage: " + str(mileage))        #########################
    # Get Thetas from the file if it exist
    theta = get_params()
    estimate_price = theta[0] + theta[1] * mileage
    print(f'This car worth ${round(estimate_price)} euro')


predict()