def check_com_info(com_name, com_id):
    # DB 내 정보 유무 확인
    pymysql.install_as_MySQLdb()
    engine = create_engine("mysql+mysqldb://root:" + "2000" + "@127.0.0.1:3306/testdb", encoding='utf-8')
    conn = pymysql.connect(host='127.0.0.1', user='root', db='testdb', passwd='2000', charset='utf8')
    arr1 = []
    check = []
    try:
        with conn.cursor() as curs:
            sql = '''SELECT com_id FROM com_info;'''
            curs.execute(sql)
            rs = curs.fetchall()
            for e in rs:
                temp = {'id': e[0]}
                check.append(int(e[0]))
            print(check)
            if int(com_id) in check:
                print("there is id")
                sql = '''SELECT com_name, com_info.* FROM com_info LEFT JOIN job_planet ON com_info.com_id=job_planet.id where job_planet.id =''' + "'" + str(
                    com_id) + "';"
                curs.execute(sql)
                rs = curs.fetchall()
                for e in rs:
                    temp = {'com_name': e[0], 'com_bis': e[3], 'com_emp': e[4], 'com_div': e[5],
                            'com_est': e[6], 'com_capital': e[7], 'com_rev': e[8], 'com_sal': e[9], 'com_ceo': e[10],
                            'com_main_bis': e[11], 'com_en': e[12], 'com_page': e[13], 'com_address': e[14],
                            'com_rel_com': e[15]}
                    arr1.append(temp)
                print(arr1)
                column_kor = ['기업명', '산업', '사원수', '기업구분', '설립일', '자본금', '매출액', '대졸초임', '대표자', '주요사업', '4대보험', '홈페이지',
                              '주소', '계열사']
                column_en = ['com_name', 'com_bis', 'com_emp', 'com_div', 'com_est', 'com_capital', 'com_rev', \
                             'com_sal', 'com_ceo', 'com_main_bis', 'com_en', 'com_page', 'com_address', 'com_rel_com']
                df = pd.DataFrame(columns=column_en, data=arr1)
                df.columns = column_kor
                df.reset_index(drop=True, inplace=True)
                print(df)
            else:
                url = 'https://www.jobkorea.co.kr/'
                options = Options()
                # 화면 유무
                # options.add_argument("headless")
                driver = webdriver.Chrome(executable_path=ChromeDriverManager().install(), options=options)
                driver.get(url)

                # 기업명 클릭
                wait_element_ready(driver, '//*[@id="stext"]').send_keys(com_name)
                # click search
                wait_element_ready(driver, '//*[@id="common_search_btn"]').click()
                # 기업정보 클릭
                wait_element_ready(driver, '//*[@id="content"]/div/div/div[1]/div/div[1]/div/button[2]').click()
                try:
                    wait_element_ready(driver,
                                       '//*[@id="content"]/div/div/div[1]/div/div[3]/div[2]/div/div[1]/ul/li[1]/div/div[1]/div/a').click()
                except Exception:
                    print('No company')
                    column = ['com_id', 'com_bis', 'com_emp', 'com_div', 'com_est', 'com_capital', 'com_rev', \
                              'com_sal', 'com_ceo', 'com_main_bis', 'com_en', 'com_page', 'com_address', 'com_rel_com']
                    com_info_list = tuple([com_id, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
                    df = pd.DataFrame([com_info_list], columns=column)
                    print(df)
                    df.reset_index(drop=True, inplace=True)
                    conn = engine.connect()
                    df.to_sql(name='com_info', con=engine, if_exists='append', index=False)
                    driver.close()
                    return 0

                # 새로 바뀐 창으로 가기
                driver.switch_to.window(driver.window_handles[-1])
                print(driver.current_url)
                try:
                    print('바로 기업정보')
                    com_data = wait_element_ready(driver, '//*[@id="company-body"]/div[1]/div[1]/div/table/tbody').text

                except Exception:
                    # 기업 정보 클릭
                    print("기업 정보 클릭")
                    try:
                        wait_element_ready(driver, '/html/body/div[2]/div[4]/div[2]/div[2]/div/a[2]/div[1]').click()
                        com_data = wait_element_ready(driver,
                                                      '//*[@id="company-body"]/div[1]/div[2]/div/table/tbody').text
                    except Exception:
                        print('예외처리무슨...')
                        com_data = wait_element_ready(driver,
                                                      '//*[@id="company-body"]/div[1]/div[2]/div/table/tbody').text

                com_data_list = []
                # 데이터 전처리
                com_data = com_data.replace('\n', "|")
                com_data = com_data.split('|')
                for i in range(len(com_data)):
                    arr = []
                    if '산업' in com_data[i] and len(com_data[i]) == 2:
                        arr.append('com_bis')
                        if i + 1 < len(com_data):
                            arr.append(com_data[i + 1])
                        com_data_list.append(arr)
                    if '사원수' in com_data[i]:
                        arr.append('com_emp')
                        if i + 1 < len(com_data):
                            arr.append(com_data[i + 1])
                        com_data_list.append(arr)
                    if '기업구분' in com_data[i]:
                        arr.append('com_div')
                        if i + 1 < len(com_data):
                            arr.append(com_data[i + 1])
                        com_data_list.append(arr)

                    if '설립일' in com_data[i]:
                        arr.append('com_est')
                        if i + 1 < len(com_data):
                            arr.append(com_data[i + 1])
                        com_data_list.append(arr)

                    if '자본금' in com_data[i]:
                        print("자본금 있다")
                        arr.append('com_capital')
                        if i + 1 < len(com_data):
                            arr.append(com_data[i + 1])
                        com_data_list.append(arr)

                    if '매출액' in com_data[i]:
                        arr.append('com_rev')
                        if i + 1 < len(com_data):
                            arr.append(com_data[i + 1])
                        com_data_list.append(arr)

                    if '대졸초임' in com_data[i]:
                        arr.append('com_sal')
                        if i + 1 < len(com_data):
                            arr.append(com_data[i + 1])
                        com_data_list.append(arr)

                    if '대표자' in com_data[i]:
                        arr.append('com_ceo')
                        if i + 1 < len(com_data):
                            arr.append(com_data[i + 1])
                        com_data_list.append(arr)

                    if '주요사업' in com_data[i]:
                        arr.append('com_main_bis')
                        if i + 1 < len(com_data):
                            arr.append(com_data[i + 1])
                        com_data_list.append(arr)

                    if '4대보험' in com_data[i]:
                        arr.append('com_en')
                        if i + 1 < len(com_data):
                            arr.append(com_data[i + 1])
                        com_data_list.append(arr)
                    if '홈페이지' in com_data[i]:
                        arr.append('com_page')
                        if i + 1 < len(com_data):
                            arr.append(com_data[i + 1])
                        com_data_list.append(arr)
                    if '주소' in com_data[i]:
                        arr.append('com_address')
                        if i + 1 < len(com_data):
                            arr.append(com_data[i + 1])
                        com_data_list.append(arr)
                    if '계열사' in com_data[i]:
                        arr.append('com_rel_com')
                        if i + 1 < len(com_data):
                            arr.append(com_data[i + 1])
                        com_data_list.append(arr)

                driver.close()
                # 초기화면으로 돌아오기
                driver.switch_to.window(driver.window_handles[0])

                driver.close()
                com_info_list = []
                com_current_col = []
                for i in com_data_list:
                    com_current_col.append(i[0])
                    com_info_list.append(i[1])
                com_info_list.insert(0, int(com_id))
                com_current_col.insert(0, 'com_id')
                com_info_list = tuple(com_info_list)
                print(com_info_list)
                df = pd.DataFrame([com_info_list], columns=com_current_col)
                df.reset_index(drop=True, inplace=True)
                print(df)
                conn = engine.connect()
                df.to_sql(name='com_info', con=engine, if_exists='append', index=False)

    finally:
        conn.close()

    return df
