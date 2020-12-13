# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    csv_tools.py                                       :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: obelouch <obelouch@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/12/13 19:33:44 by obelouch          #+#    #+#              #
#    Updated: 2020/12/13 19:38:59 by obelouch         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from os import path
import  pandas as pd

def     df_fromCSV(filename):
    '''
    Get Dataframe from a CSV file
    Errors are treated
    '''
    # Check if the Dataset file exist
    if not path.exists(filename):
        print(f'\nError: Dataset file "{filename}" not found!')
        exit(1)
    # Read Dataset CSV File 
    df = pd.read_csv(filename)
    # Check if the dataframe is empty
    if df.empty:
        print(f'\nError: Can\'t read data from "{filename}"!')
        exit(1)
    return df