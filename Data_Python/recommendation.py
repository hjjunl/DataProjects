# IT 기업 추천 (Item based collaborative filtering)
def job_recomendation(user, mean_sal, mean_star, com_review_seg, welfare_sal, wo_la_bal, com_cul, 
                      opportunity, com_head, growth_pos_seg, com_rec_seg, CEO_sup_seg):
  
    pymysql.install_as_MySQLdb()
    engine = create_engine("mysql+mysqldb://root:" + "2000" + "@127.0.0.1:3306/testdb", encoding='utf-8')
    conn = pymysql.connect(host='127.0.0.1', user='root', db='testdb', passwd='2000', charset='utf8')
    # 추천 할 값과 회사
    rec_com_list = []
    # 초기 상태
    if mean_sal == '' or mean_star == '' or welfare_sal == '' or com_review_seg == '':
        rec_com_list = [['']]
    else:
        arr = []
        with conn.cursor() as curs:
            sql = "select * from job_planet"
            curs.execute(sql)
            rs = curs.fetchall()
            for row in rs:
                arr.append(row)

        df = pd.DataFrame(
            columns=['id', 'com_name', 'com_relation', 'mean_star', 'com_review', 'mean_sal', 'welfare_sal', \
                     'wo_la_bal', 'com_cul', 'opportunity', 'com_head', 'com_rec', 'CEO_sup', \
                     'growth_pos'],
            data=arr)
        labels = np.arange(1, 6, 1)

        # 평균 연복은 크게 5개로 나눔 cut
        mean_sal_seg_series = pd.Series(list(pd.cut(df['mean_sal'], 5, labels=labels)),
                                        name='mean_sal_seg')  # 2800씩 등차함수

        # 나머지는 각 수에 맞춰 qcut
        com_rec_seg_series = pd.Series(list(pd.cut(df['com_rec'], 5, labels=labels)), name='com_rec_seg')
        CEO_sup_seg_series = pd.Series(list(pd.qcut(df['CEO_sup'], 5, labels=labels)), name='CEO_sup_seg')
        growth_pos_seg_series = pd.Series(list(pd.qcut(df['growth_pos'], 5, labels=labels)), name='growth_pos_seg')
        # com_review 인지도로 나타낸다 (리뷰수)
        com_review_seg_series = pd.Series(list(pd.qcut(df['com_review'], 5, labels=labels)), name='com_review_seg')
        # 데이터 병합 1~5점으로 변환
        df = pd.concat([df, com_review_seg_series, growth_pos_seg_series, com_rec_seg_series, mean_sal_seg_series,
                        CEO_sup_seg_series], axis=1)
        df.reset_index(drop=True, inplace=True)

        # 연봉 범위 정할 때
        if mean_sal >= 0 and mean_sal <= 1.5:
            df = df[(df['mean_sal_seg'] == 1)]
        if mean_sal <= 2.5 and mean_sal > 1.5:
            df = df[(df['mean_sal_seg'] == 2)]
        if mean_sal <= 3.5 and mean_sal > 2.5:
            df = df[(df['mean_sal_seg'] == 3)]
        if mean_sal <= 4.5 and mean_sal > 3.5:
            df = df[(df['mean_sal_seg'] == 4)]
        if mean_sal > 4.5:
            df = df[(df['mean_sal_seg'] == 5)]

        df.reset_index(drop=True, inplace=True)

        # Choose mean_star 평균 별점 선택시 +-0.5로 범위 설정
        if mean_star <= 1.5:
            df = df[(df['mean_star'] >= 0) & (df['mean_star'] <= 1.5)]
        if mean_star <= 2.5 and mean_star > 1.5:
            df = df[(df['mean_star'] > 1.5) & (df['mean_star'] <= 2.5)]
        if mean_star <= 3.5 and mean_star > 2.5:
            df = df[(df['mean_star'] > 2.5) & (df['mean_star'] <= 3.5)]
        if mean_star <= 4 and mean_star > 3.5:
            df = df[(df['mean_star'] > 3.5) & (df['mean_star'] <= 4.5)]
        if mean_star > 4.5:
            df = df[(df['mean_star'] >= 4)]
        # user가 선택한 값들
        user_1 = [int(com_review_seg), int(welfare_sal), int(wo_la_bal), int(com_cul), int(opportunity), int(com_head),
                  int(growth_pos_seg), int(com_rec_seg), int(CEO_sup_seg)]

        com_df = df.drop(['CEO_sup', 'com_rec', 'growth_pos', 'com_review', 'mean_sal_seg', 'com_relation'], axis=1)
        com_df.reset_index(drop=True, inplace=True)
        com_df = com_df[
                       [
                       'id', 'com_name', 'mean_star', 'com_review_seg', 'mean_sal', 'welfare_sal', 'wo_la_bal', \
                       'com_cul', 'opportunity', 'com_head', 'growth_pos_seg', 'com_rec_seg', 'CEO_sup_seg'
                       ]
                       ]
        # 행을 잘라 list로 붙임
        com_list = []
        for i in range(len(com_df)):
            com_list.append(list(com_df.loc[i]))

        # 함수 호출
        sim = cos_sim(user_1, com_list)
        for i, j in sim:
            j.insert(0, i)
            rec_com_list.append(j)

        print(rec_com_list)
        com_result = []
        for i in rec_com_list:
            com_result.append(i[1])
        com_name = ','.join(com_result)
        user_choice = [int(user), mean_sal, mean_star, com_review_seg, welfare_sal, wo_la_bal, com_cul, opportunity,
                       com_head,
                       growth_pos_seg, com_rec_seg, CEO_sup_seg, com_name]

        sql_col = [
                  'user_id', 'mean_sal', 'mean_star', 'com_review_seg', 'welfare_sal', 'wo_la_bal', \
                  'com_cul', 'opportunity', 'com_head', 'growth_pos_seg', 'com_rec_seg', 'CEO_sup_seg', 'com_result'
                  ]
        user_choice = tuple(user_choice)

        df = pd.DataFrame([user_choice], columns=sql_col)
        print(df)
        df.reset_index(drop=True, inplace=True)

        df.to_sql(name='user_rec', con=engine, if_exists='append', index=False)
        print('user_choice', user_choice)
        return rec_com_list
