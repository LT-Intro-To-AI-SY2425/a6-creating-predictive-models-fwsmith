import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

#imports and formats the data
data = pd.read_csv("part3-multivariable-linear-regression/car_data.csv")
x = data[["miles","age"]].values
y = data["Price"].values

#split the data into training and testing data
xtrain, xtest, ytrain, ytest = train_test_split(x, y, test_size = .2)

#create linear regression model
model = LinearRegression().fit(xtrain, ytrain)

#Find and print the coefficients, intercept, and r squared values. 
#Each should be rounded to two decimal places. 
coef = np.around(model.coef_, 2)
print(f"Coefficent is {coef}")
intercept = round(float(model.intercept_), 2)
print(f"The intercept is {intercept}")
r_squared = round(model.score(x, y),2)
print(f"r squared value is {r_squared}")



#Loop through the data and print out the predicted prices and the 
#actual prices

print("***************")
print("Testing Results")

print("predictions")
miles_1=89000
age_1=10
predict_1=model.predict([[miles_1, age_1]])
print(f"prediction for {age_1} year old car with {miles_1} miles is {predict_1}")
miles_1=150000
age_1=20
predict_1=model.predict([[miles_1, age_1]])
print(f"prediction for {age_1} year old car with {miles_1} miles is {predict_1}")

predict = model.predict(xtest)
predict = np.around(predict, 2)
for index in range(len(xtest)):
    actual = ytest[index] # gets the actual y value from the ytest dataset
    predicted_y = predict[index] # gets the predicted y value from the predict variable
    x_coord = xtest[index] # gets the x value from the xtest dataset
    print(f"miles: {x_coord[0]} Age: {x_coord[1]}  Actual: {actual} Predicted: {predicted_y}")