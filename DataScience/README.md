# ML Prediction
### Bicycle rental prediction
* This dataset soure is from https://dacon.io/competitions/official/235837/data
* This program is about predicting future rental numbers of bicycles at Seoul Korea.
* It's just personal toy project for ML.

### NH stock holding period prediction (dataset is not allowed to use)
* I failed to predict the future stock holding period. (daycon NH_bank competition)
* This dataset is forbidden to use so only the code remains.
* Used the outer variables such as PER, PBR, KRX...etc
* It's just personal toy project for ML.
### Instacart Market Basket Analysis
* predict which previously purchased products will be in a user’s next order.
* Toy project to make new variables and improve the model
* Xgboost, Catboost, RandomForest, Logistic Regression ensembled model

![image](https://user-images.githubusercontent.com/50603209/158091981-35647573-eb81-4348-80c0-a5be2a78bdb6.png)

# Recommendation
### Using jobplanet's crawling data for recommendation program (User based collaborative filtering)
* Using crawled data for job recommendation
* 연봉 범위 선택 2800 5600, 평균 별점 선택, 복지 및 급여, 업무와 삶의 균형, 사내문화, 승진 기회 및 가능성, 경영진, 기업 조회: 기업 인지도, 성장 가능성, 기업 추천율, CEO 지지율
* mean salary, mean_star, com_review_seg, welfare_sal, work_life_balance, company_culture, promotion opportunity, company head, company growth posibility_seg, company_recommendation_seg, CEO_support_seg
* cosine similarity was used
* 2110 IT company data

# Time Series Analysis
## LSTM model
### Stock prediction done by mutivariate LSTM model (FED FUNDS data)
* Using LSTM model for prediction
* code base line: I used 'Vytautas Bielinskas's code as my baseline. 2020.
* get rid of the time lagging problem
* feature extraction and external data FED FUNDS data was used
* used yahoo finace Api to get stock dataset

![image](https://user-images.githubusercontent.com/50603209/141417239-2e16d0da-aadc-4c8b-bfa1-f989e870f365.png)

## Prophet Model
### Single variable model
- DB is private and data forms are int(255)
- Change DB to yours to fit the model
- ds: date  yhat: predicted value  yhat_lower: predicted value low  yhat_upper: predicted value high in 95% range
- Black line is the actual data, blue line is predicted data, sky blue color range is the range in 95% accuracy

![image](https://user-images.githubusercontent.com/50603209/131627632-e13152a9-1b76-4b3b-9e6e-08e6cea4804f.png)

### Multivariable Model
- Using other varible that affects cost data prediction (variable cost, fixed cost, material cost, exchange rate, interest rate)
- add_regression to predict 12 months

![image](https://user-images.githubusercontent.com/50603209/131627531-30e19baf-50e5-483c-9b38-bf52cb4a116c.png)

