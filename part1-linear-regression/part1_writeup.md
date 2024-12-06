# Part 1 - Linear Regression Writeup

After completing `a6_part1.py` answer the following questions

## Questions to answer

1. What is the r squared value?  What does this say about this linear regression model?
The R squared value is 0.626, which is not horrible, but not a super powerful correlation.
2. According to your model, what is the predicted systolic blood pressure for a person who is 42 years old?
136.52
3. How accurate do you think this model's predictions are?  Do you think this model is accurate enough to reliably predict someone's blood pressure based on their age?  Why or why not?  And if not, what could improve the model?
I do not think this model is that accurate. While Age certainly impacts blood pressure, using only age assumes that every human lives the same life and eats the same food, etc. To improve the model, I would find a way to either include other variables like health choices, or to limit the category to people with certain levels of pysical activity or diets.