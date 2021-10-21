vimport io
import os
import pickle
import joblib
import numpy as np
import plot as plot
from matplotlib import pyplot
from numpy import dot
from numpy.linalg import norm
from sqlalchemy import create_engine
import pandas as pd
import pymysql
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor

path = 'static/model/model.pkl'
dbCon = pymysql.connect(host = '127.0.0.1', user = 'root', db = 'testdb', passwd = '2000', charset = 'utf8')


# IT 기업 추천
def job_recomendation(mean_sal, mean_star, welfare_sal, wo_la_bal, com_cul, opportunity, com_head,
                      com_review_seg, growth_pos_seg, com_rec_seg, CEO_sup_seg):
    # 추천 할 값과 회사
    rec_value_list = []
    rec_com_list = []
    # 초기 상태
    if mean_sal == '' or mean_star == '' or welfare_sal == '':
        rec_value_list = [0, 0, 0, 0, 0, 0, 0, 0, 0]
        rec_com_list = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    else:
        conn = pymysql.connect(host = '127.0.0.1', user = 'root', db = 'testdb', passwd = '2000', charset = 'utf8')
        arr = []
        with conn.cursor() as curs:
            sql = "select * from job_planet"
            curs.execute(sql)
            rs = curs.fetchall()
            for row in rs:
                arr.append(row)

        df = pd.DataFrame(columns = ['id', 'com_name', 'mean_star', 'com_review', 'mean_sal', 'welfare_sal',
                                     'wo_la_bal', 'com_cul', 'opportunity', 'com_head', 'com_rec', 'CEO_sup', 'growth_pos'],
                          data = arr)
        # print(df)
        labels = np.arange(1, 6, 1)

        # 평균 연복은 크게 5개로 나눔 cut
        mean_sal_seg_series = pd.Series(list(pd.cut(df['mean_sal'], 5, labels = labels)), name = 'mean_sal_seg')  # 2800씩 등차함수

        # 나머지는 각 수에 맞춰 qcut
        com_rec_seg_series = pd.Series(list(pd.qcut(df['com_rec'], 5, labels = labels)), name = 'com_rec_seg')
        CEO_sup_seg_series = pd.Series(list(pd.qcut(df['CEO_sup'], 5, labels = labels)), name = 'CEO_sup_seg')
        growth_pos_seg_series = pd.Series(list(pd.cut(df['growth_pos'], 5, labels = labels)), name = 'growth_pos_seg')

        # com_review 인지도로 나타낸다 (리뷰수)
        com_review_seg_series = pd.Series(list(pd.qcut(df['com_review'], 5, labels = labels)), name = 'com_review_seg')

        # 데이터 병합 1~5점으로 변환
        df = pd.concat([df, com_review_seg_series, growth_pos_seg_series, com_rec_seg_series, mean_sal_seg_series, CEO_sup_seg_series], axis = 1)
        df.reset_index(drop = True, inplace = True)

        # 연봉 범위 정할 때
        # sal = 5
        if mean_sal == 1:
            new_df = df[(df['mean_sal_seg'] == 1)]
        elif mean_sal == 2:
            new_df = df[(df['mean_sal_seg'] == 2)]
        elif mean_sal == 3:
            new_df = df[(df['mean_sal_seg'] == 3)]
        elif mean_sal == 4:
            new_df = df[(df['mean_sal_seg'] == 4)]
        elif mean_sal == 5:
            new_df = df[(df['mean_sal_seg'] == 5)]
            print(new_df)
        new_df.reset_index(drop = True, inplace = True)
        # Choose mean_star 평균 별점 선택시 +-0.5로 범위 설정
        if mean_star == 1:
            new_df = new_df[(new_df['mean_star'] >= 0.5) & (new_df['mean_star'] <= 1.5)]
        elif mean_star == 2:
            new_df = new_df[(new_df['mean_star'] >= 1.5) & (new_df['mean_star'] <= 2.5)]
        elif mean_star == 3:
            new_df = new_df[(new_df['mean_star'] >= 2.5) & (new_df['mean_star'] <= 3.5)]
        elif mean_star == 4:
            new_df = new_df[(new_df['mean_star'] >= 3.5) & (new_df['mean_star'] <= 4.5)]
        elif mean_star == 5:
            new_df = new_df[(new_df['mean_star'] >= 4.5)]
        # user가 선택한 값들
        user_1 = [welfare_sal, wo_la_bal, com_cul, opportunity, com_head,
                      com_review_seg, growth_pos_seg, com_rec_seg, CEO_sup_seg]

        com_df = new_df.drop(['id', 'CEO_sup', 'mean_sal', 'com_rec', 'growth_pos', 'com_review' , 'mean_star', 'mean_sal_seg'], axis = 1)

        com_df.reset_index(drop = True, inplace = True)

        # 행을 잘라 list로 붙임
        com_list = []
        for i in range(len(com_df)):
            com_list.append(list(com_df.loc[i]))

        # 함수 호출
        sim = cos_sim(user_1, com_list)

        for i in range(10):
            print(sim[i][0])
            print(sim[i][1])

            rec_value_list.append(sim[i][1])
            rec_com_list.append(sim[i][0])

        return rec_value_list, rec_com_list


# list 간 코사인 유사도 계산
def cos_sim(user, com_list_):
    cos_sim_list = []
    com_name = []
    for i in com_list_:
        com_name.append(i[0])
    for i in range(len(com_list_)):
        com_list_[i].pop(0)
        # 예외 처리
        if len(com_list_[i]) == 8:
            cos_sim_list.append([0, 0, 0, 0, 0, 0, 0, 0, 0])
        try:
            cos_sim_list.append(dot(user, com_list_[i]) / (norm(user) * norm(com_list_[i])))
        except Exception:
            cos_sim_list.append([0, 0, 0, 0, 0, 0, 0, 0, 0])
    # 회사와 cos sim 묶은후 정렬
    rec_dic = dict(zip(com_name, cos_sim_list))
    rec_dic = sorted(rec_dic.items(), key = lambda x: x[ 1 ], reverse = True)
    rec_dic = rec_dic[:10]
    return rec_dic


if __name__ == '__main__':
    # 'welfare_sal', 'wo_la_bal', 'com_cul', 'opportunity','com_head', 'com_review_seg',
    # 'growth_pos_seg', 'com_rec_seg','CEO_sup_seg'
    job_recomendation(4, 3.7, 4, 4, 4, 4, 3, \
                      5, 2.5, 3.5, 3)
