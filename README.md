## Data Science
### 1. Prophet project (for Manufacturing company income)
* Analysis using Prophet models
* To find insight, predict future income.
* Two types (single variable, multivariate variables)

### 2. Simple prediction for new employ's salary
* Used at flask project
* data is hand made (no reliability)
* random forest regression
* data processing

### 3. Bicycle rent prediction
* This dataset soure is from https://dacon.io/competitions/official/235837/data
* This program is about predicting future rental numbers of bicycles at Seoul Korea.
* It's just personal toy project for ML.

### 4. NH stock holding period prediction (No dataset offered)
* I failed to predict this project. (daycon's NH_bank competition)
* This dataset is forbidden to use so only the code remains.
* Used the outer variables such as PER, PBR, KRX...etc
* It's just personal toy project for ML.

### 5. Using jobplanet's crawling data for recommendation program (User based collaborative filtering)
* Using crawled data for job recommendation
* 연봉 범위 선택 2800 5600, 평균 별점 선택, 복지 및 급여, 업무와 삶의 균형, 사내문화, 승진 기회 및 가능성, 경영진, 기업 조회: 기업 인지도, 성장 가능성, 기업 추천율, CEO 지지율
* mean salary, mean_star, com_review_seg, welfare_sal, work_life_balance, company_culture, promotion opportunity, company head, company growth posibility_seg, company_recommendation_seg, CEO_support_seg
* cosine similarity was used
* 2110 IT company data

### 6. Stock prediction done by mutivariate LSTM model (FED FUNDS data added)
* Using LSTM model for prediction
* code base line: Vytautas Bielinskas's LSTM project
* get rid of the time lagging problem
* feature extraction and external data FED FUNDS data was used
* used yahoo finace Api to get stock dataset

## Data_Python (Automation)
### 1. Exchange rate ETL automation (dalily)
 * Used crawling to get exchange rate
 * save data in the database every 10:20 a.m
### 2. Exchange rate Crawling (past data)
* Crawl data from 2001-01-10 to 2020-12-10(monthly)
### 3. Naver news data crawling
* Crawl news data from Naver news
* Save data as a Excel file
### 4. Data concatnation and Graph automation
* Make several data into one csv file
* Draw graph (scatter graph)
### 5. Korean IT company info crawling (jobplanet.co.k)
* Crawling IT companies info from Korean job application site
* 기업명, 평균 별점, 평균연봉, 기업 조회수, 복지 및 급여, 업무와 삶의 균형, 사내문화...etc
* Useful for recommendation system and company analysis
* row:3306, col: 12

## Data_Java_SQL
### 1. Simple Employ project
* SELECT, INSERT, JOIN, SUM, MAX, MIN
* Example query for tutorial(employee salary program)
