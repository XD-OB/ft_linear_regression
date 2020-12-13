# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    params.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: obelouch <obelouch@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/12/13 05:21:37 by obelouch          #+#    #+#              #
#    Updated: 2020/12/13 19:03:06 by obelouch         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from re import match
from os import path

def     is_correct_content(text):
    '''
    Check if the file "params" content respect the norme
    '''
    if match(r'^-?[0-9]+(\.[0-9]+)? -?[0-9]+(\.[0-9]+)?$', text):
        return True
    return False

def     get_params():
    '''
    Get Theta0, Theta1 from the params file
    '''
    theta = [0, 0]
    # Get the params if the file exist:
    if path.exists('Data/params'):
        fd = open('Data/params', 'r')
        line = fd.read()
        if is_correct_content(line):
            theta = [float(item) for item in line.split()]
        else:
            print('\nError: The content of the file "params" doesn\'t respect the norme')
            print('       Norme: <Theta_0> <Theta_1>')
            print('       Fix Problem: Delete the File')
            exit(1)
        # Close the file
        fd.close()
    return theta


def     write_params(theta):
    '''
    Write Theta0, Theta1 in the params file
    '''
    fd = open('Data/params', 'w')
    fd.write(f'{theta[0]} {theta[1]}')
    # Close the file
    fd.close()