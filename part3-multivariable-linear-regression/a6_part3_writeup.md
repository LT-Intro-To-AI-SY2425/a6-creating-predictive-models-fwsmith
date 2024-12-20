# Part 3 - Multivariable Linear Regression Writeup

After completing `a6_part3.py` answer the following questions

## Questions to answer

1. What is the R Squared coefficient for your model? What does that mean about the model in relation to your data?
0.85, which is good, and that it can predict data proficiently
2. Is your model accurate? Why or why not?
yes, because it ives predictions which are consistently close to the actual outcome, as shown by the R squared value
3. What does the model predict a 10-year-old car with 89000 miles is worth? What about a car that is 20 years old with 150000 miles?
the 10-year-old car is predicted as 8585.60, and the 20-year-old is predicted to be 802.17
4. You may notice that some of your predicted results are negative. This is occurring when the value of age and the mileage of the car are very high. Why do you think this is happening?
because the correlation is linear, it will eventually pass the x-axis into negative values as values increase.