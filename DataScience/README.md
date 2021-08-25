# Prophet model
### 1. Single variable model
- DB is private and data forms are int(255)
- Change DB to yours to fit the model
- ds: date  yhat: predicted value  yhat_lower: predicted value low  yhat_upper: predicted value high in 95% range
- Black line is the actual data, blue line is predicted data, sky blue color range is the range in 95% accuracy

### 2. Multivariable model
- Using other varible that affects cost data prediction (variable cost, fixed cost, material cost, exchange rate, interest rate)
- add_regression to predict 12 months

