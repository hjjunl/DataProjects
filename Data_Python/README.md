# Data projects done by python

### <DB is private use your DB to fit the model>

### Currency_ETL_automation

- Crawl data by read_html
- Fit the data format to db format (int, varchar...)
- Use pymysql for insertion
- Use schedulers for automation (every 10:30 a.m) 
  
![image](https://user-images.githubusercontent.com/50603209/131627788-1621daa0-3676-4ec8-b227-f5cbac04316f.png)

### Currency_db_save

- Crawl data from Korea's hana bank using selinium and BeautifulSoup
- Input data: 2021-01-01 Out put: 2021-01-01's currency data EURO, CHN, JPN, USD in Korean won
  
![image](https://user-images.githubusercontent.com/50603209/131627897-8c3a4190-c6b1-4c73-8ea9-7b7630e4528c.png)

### Excel_save

- Save Excel data to your database
- You need your database structure before this. 

  ![image](https://user-images.githubusercontent.com/50603209/131627970-1b959313-f2d6-425d-93be-21b1db455ffe.png)

 ### Naver news data crawling
  
- Using selenium to get data crawling automation
- Change data into Excel form
- Data paste avaliable

### Gragh automation and data concatnation
  
- Find data start with [1~[20
- Grouping the data as a same csv file if the number is same
- Handling the data into the style I like.
- Make the graph automatically (scatter graph)
  - (Data set,           Result graph)
  
  ![image](https://user-images.githubusercontent.com/50603209/133026964-1eae1d25-dec0-40ea-b15d-425277dd238c.png) ![image](https://user-images.githubusercontent.com/50603209/133028536-65e95d65-5366-4fa7-b141-fc6bb20e1f4f.png)

### Korean IT company information crawling (jobplanet.co.kr)
- Crawling IT companies info from Korean job application site
- Data: 기업명, 평균 별점, 평균연봉, 기업 조회수, 복지 및 급여, 업무와 삶의 균형, 사내문화...etc
- Useful for recommendation system and company analysis
- Extract data in Excel file
![image](https://user-images.githubusercontent.com/50603209/138049911-a0d27238-c79c-4c0d-84b1-793e345ae036.png)
### Using jobplanet's crawling data for recommendation program
- Using crawled data for job recommendation (User based collaborative filtering)
- data set: 연봉 범위 선택 2800 5600, 평균 별점 선택, 복지 및 급여, 업무와 삶의 균형, 사내문화, 승진 기회 및 가능성, 경영진, 기업 조회: 기업 인지도, 성장 가능성, 기업 추천율, CEO 지지율
- cosine similarity was used
- 2110 IT company data
- flask application is used too check flask project
- automatically saved to database
![image](https://user-images.githubusercontent.com/50603209/139201623-b36fad60-e3c2-4e29-a3ac-5f62ac6ab9e8.png)

