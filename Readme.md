# Univariable Linear Regression

The aim of this project is to introduce you to the basic concept behind machine learning. For this project, you will have to create a program that predicts the price of a car
by using a linear function train with a gradient descent algorithm.

### Subject PDF:
[project_pdf!](https://github.com/XD-OB/ft_linear_regression/blob/master/Files/en.subject.pdf)

### Cook Book:
[Cook_book!](https://github.com/XD-OB/ft_linear_regression/blob/master/Files/cook_book.ipynb)

## Install modules:
In order to launch the scripts you should install the following modules and packages:
* Install python3 and pip3
- pip3 install numpy
- pip3 install pandas
- pip3 install matplotlib

## Train the model use:
* python3 train.py [-BGD | -SGD | -LS][{< alpha >}]
- BGD: Batch Gradient Descent
- SGD: Stochastic Gradient Descent   (Bonus)
- LS: Least Squares   (Bonus)
- alpha: learning rate (a number < 1)   (Bonus)

Once the Training is done a bunch metrics evoluations are shown to evaluate the model: (Bonus)
- MAPE : Mean absolute percentage error
- RMSE : Root of Mean Squared Error
- MAE: Mean Absolute Error

![Screen Shot 1](https://github.com/XD-OB/ft_linear_regression/blob/master/Files/train.png)

## Plot the Dataset with the model hypothesis: (Bonus)
* python3 visualizer.py

![Screen Shot 2](https://github.com/XD-OB/ft_linear_regression/blob/master/Files/visualizer.png)

## Predict the Price for a given mileage:
Using the Parameters tuned with the trained model using the given dataset, i can predict the price of a car for a mileage given as input by the User.
* python3 predict.py

## obelouch