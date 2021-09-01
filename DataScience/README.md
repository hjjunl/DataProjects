# Prophet model
### 1. Single variable model
- DB is private and data forms are int(255)
- Change DB to yours to fit the model
- ds: date  yhat: predicted value  yhat_lower: predicted value low  yhat_upper: predicted value high in 95% range
- Black line is the actual data, blue line is predicted data, sky blue color range is the range in 95% accuracy
![image](https://user-images.githubusercontent.com/50603209/131627632-e13152a9-1b76-4b3b-9e6e-08e6cea4804f.png)

### 2. Multivariable model
- Using other varible that affects cost data prediction (variable cost, fixed cost, material cost, exchange rate, interest rate)
- add_regression to predict 12 months
![image](https://user-images.githubusercontent.com/50603209/131627531-30e19baf-50e5-483c-9b38-bf52cb4a116c.png)

