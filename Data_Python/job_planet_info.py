from openpyxl import load_workbook
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.remote.webelement import WebElement
from webdriver_manager.chrome import ChromeDriverManager  # 'webdriver_manager' 패키지모듈 다운로드 필요
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from typing import List
import pandas as pd

options = Options()

driver = webdriver.Chrome(executable_path=ChromeDriverManager().install(), options=options)  # 최신 크롬 드라이버 설치
WAIT_TIME = 4


def wait_element_ready(_driver: webdriver, xpath: str, wait: int = WAIT_TIME) -> WebElement:
    WebDriverWait(_driver, wait).until(
        expected_conditions.presence_of_all_elements_located(
            (By.XPATH, xpath)))
    web_element = _driver.find_element_by_xpath(xpath)
    return web_element


def wait_elements_ready(_driver: webdriver, xpath: str, wait: int = WAIT_TIME) -> List:
    WebDriverWait(_driver, wait).until(
        expected_conditions.presence_of_all_elements_located(
            (By.XPATH, xpath)))
    web_elements = _driver.find_elements_by_xpath(xpath)
    return web_elements


EXCEL_FILE = 'job_planet.xlsx'


# 기업명
com_name = []
# 평균 별점
mean_star = []
# 평균 급여
mean_salary = []
# 기업 조회수
com_review = []
# 복지 및 급여
welfare_salary = []
# 업무와 삶의 균형
work_life_balance = []
# 사내 문화
com_culture = []
# 승진 기회 및 가능성
promotion_pos = []
# 경영진
com_head = []
# 기업 추천율
com_recommendation = []
# CEO 지지율
CEO_support = []
# 성장 가능성
growth_pos = []
url = "https://www.jobplanet.co.kr/companies?industry_id=700&page="

for k in range(1, 332):
    try:
        for i in range(1, 11):
            # start driver
            driver.get(url + str(k))
            # 기업명
            print('메인페이지 기업 위치: ', i)
            print('페이지: ', k)
            # time.sleep(2)
            com_name_check = '//*[@id="listCompanies"]/div/div[1]/section[' + str(i) + ']/div/div/dl[1]/dt/a'
            # 기업 평균 연봉
            mean_salary_check = '//*[@id="listCompanies"]/div/div[1]/section[' + str(
                i) + ']/div/div/dl[2]/dd[2]/a/strong'
            # 기업 평균 별점
            mean_star_check = '//*[@id="listCompanies"]/div/div[1]/section[' + str(i) + ']/div/div/dl[2]/dd[1]/span'
           # 기업 조회수
            com_review_check = '//*[@id="listCompanies"]/div/div[1]/section[' + str(i) + ']/div/div/dl[2]/dt'
            # 기업 상세 조회 클릭
            com_click = '//*[@id="listCompanies"]/div/div[1]/section[' + str(i) + ']/div/div/dl[1]/dt/a'
            try:
                print('제대로 된 mian 화면')
                # 기업명 저장
                com_name.append(wait_element_ready(driver, com_name_check).text)
                # 평균 연봉 저장
                mean_salary.append(int(wait_element_ready(driver, mean_salary_check).text.replace(',', "")))
                # 평균 별점 저장
                mean_star.append(float(wait_element_ready(driver, mean_star_check).text))
                # 기업 조회수 저장
                com_review.append(int(wait_element_ready(driver, com_review_check).text.split('개의 리뷰')[0].replace(',', "")))
                # 기업 상세 조회 다른 화면으로 전환
                wait_element_ready(driver, com_click).click()

            except Exception:
                print("main 화면이 아님")
                print(driver.current_url)
                driver.get(url + str(k))
                # 기업명 저장
                com_name.append(wait_element_ready(driver, com_name_check).text)
                # 평균 연봉 저장
                mean_salary.append(int(wait_element_ready(driver, mean_salary_check).text.replace(',', "")))
                # 평균 별점 저장
                mean_star.append(float(wait_element_ready(driver, mean_star_check).text))
                # 기업 조회수 저장
                com_review.append(int(wait_element_ready(driver, com_review_check).text.split('개의 리뷰')[0].replace(',', "")))
                # 기업 상세 조회 다른 화면으로 전환
                wait_element_ready(driver, com_click).click()

            # 리뷰 버튼 클릭
            if 'reviews' not in driver.current_url:  # 상세 조회시 리뷰화면이 아니라 뉴스룸일 때
                try:
                    print('click review button')
                    wait_element_ready(driver, '//*[@id="viewCompaniesMenu"]/ul/li[3]/a').click()

                except Exception:
                    print('팝업 닫고 리뷰 버튼 클릭 다시 클릭')
                    print(driver.current_url)
                    if 'page=' in driver.current_url:
                        wait_element_ready(driver, com_click).click()
                    else:
                        print("사이트 암호화 됨, 그대로 진행")
                        try:
                            # 복지 및 급여
                            welfare_salary.append(float(wait_element_ready(driver,
                                                                           '//*[@id="premiumReviewStatistics"]/div/div/div/div[2]/div[2]/div[1]/div/div[2]/span[2]').text))
                        except Exception:
                            welfare_salary.append(0)
                        try:
                            # 업무와 삶의 균형
                            work_life_balance.append(float(wait_element_ready(driver,
                                                                              '//*[@id="premiumReviewStatistics"]/div/div/div/div[2]/div[2]/div[2]/div/div[2]/span[2]').text))
                        except Exception:
                            work_life_balance.append(0)
                        try:
                            # 사내 문화
                            com_culture.append(float(wait_element_ready(driver,
                                                                        '//*[@id="premiumReviewStatistics"]/div/div/div/div[2]/div[2]/div[3]/div/div[2]/span[2]').text))
                        except Exception:
                            com_culture.append(0)
                        try:
                            # 승진 기회 및 가능성
                            promotion_pos.append(
                                float(wait_element_ready(driver, '//*[@id="premiumReviewStatistics"]/div/div/div/div['
                                                                 '2]/div[2]/div[4]/div/div[2]/span[2]').text))
                        except Exception:
                            promotion_pos.append(0)
                        try:
                            # 경영진
                            com_head.append(
                                float(wait_element_ready(driver, '//*[@id="premiumReviewStatistics"]/div/div/div/div['
                                                                 '2]/div[2]/div[5]/div/div[2]/span[2]').text))
                        except Exception:
                            print('com_head error')
                            com_head.append(0)

                        try:
                            # 기업 추천율
                            com_recommendation.append(int(wait_element_ready(driver,
                                                                             '//*[@id="premiumReviewStatistics"]/div/div/div/div[3]/div[1]/div[1]/span').text.replace(
                                '%', "")))

                        except Exception:
                            com_recommendation.append(0)
                        try:
                            # CEO 지지율
                            CEO_support.append(
                                int(wait_element_ready(driver, '//*[@id="premiumReviewStatistics"]/div/div/div/div['
                                                               '3]/div[2]/div[1]/span').text.replace('%', "")))
                        except Exception:
                            CEO_support.append(0)
                        try:
                            # 성장 가능성
                            growth_pos.append(
                                int(wait_element_ready(driver, '//*[@id="premiumReviewStatistics"]/div/div/div/div['
                                                               '3]/div[3]/div[1]/span').text.replace('%', "")))
                        except Exception:
                            growth_pos.append(0)
                        print('데이터 row 수: ', len(com_name))
                        print(com_name)
                        print(com_review)
                    try:
                        # 팝업 닫기
                        wait_element_ready(driver,
                                           '//*[@id="premiumReviewChart"]/div/div[3]/div[2]/div/div[1]/button').click()
                        # 리뷰 클릭
                        wait_element_ready(driver, '//*[@id="viewCompaniesMenu"]/ul/li[3]/a').click()

                    except Exception:
                        # 리뷰 클릭
                        wait_element_ready(driver, '//*[@id="viewCompaniesMenu"]/ul/li[3]/a').click()
            try:
                # 복지 및 급여
                welfare_salary.append(float(wait_element_ready(driver,
                                                               '//*[@id="premiumReviewStatistics"]/div/div/div/div[2]/div[2]/div[1]/div/div[2]/span[2]').text))
            except Exception:
                welfare_salary.append(0)
            try:
                # 업무와 삶의 균형
                work_life_balance.append(float(wait_element_ready(driver,
                                                                  '//*[@id="premiumReviewStatistics"]/div/div/div/div[2]/div[2]/div[2]/div/div[2]/span[2]').text))
            except Exception:
                work_life_balance.append(0)
            try:
                # 사내 문화
                com_culture.append(float(wait_element_ready(driver,
                                                            '//*[@id="premiumReviewStatistics"]/div/div/div/div[2]/div[2]/div[3]/div/div[2]/span[2]').text))
            except Exception:
                com_culture.append(0)
            try:
                # 승진 기회 및 가능성
                promotion_pos.append(
                    float(wait_element_ready(driver, '//*[@id="premiumReviewStatistics"]/div/div/div/div['
                                                     '2]/div[2]/div[4]/div/div[2]/span[2]').text))
            except Exception:
                promotion_pos.append(0)
            try:
                # 경영진
                com_head.append(float(wait_element_ready(driver, '//*[@id="premiumReviewStatistics"]/div/div/div/div['
                                                                 '2]/div[2]/div[5]/div/div[2]/span[2]').text))
            except Exception:
                print('com_head error')
                com_head.append(0)

            try:
                # 기업 추천율
                com_recommendation.append(int(wait_element_ready(driver,
                                                                 '//*[@id="premiumReviewStatistics"]/div/div/div/div[3]/div[1]/div[1]/span').text.replace(
                    '%', "")))

            except Exception:
                com_recommendation.append(0)
            try:
                # CEO 지지율
                CEO_support.append(int(wait_element_ready(driver, '//*[@id="premiumReviewStatistics"]/div/div/div/div['
                                                                  '3]/div[2]/div[1]/span').text.replace('%', "")))
            except Exception:
                CEO_support.append(0)
            try:
                # 성장 가능성
                growth_pos.append(int(wait_element_ready(driver, '//*[@id="premiumReviewStatistics"]/div/div/div/div['
                                                                 '3]/div[3]/div[1]/span').text.replace('%', "")))
            except Exception:
                growth_pos.append(0)
            print('데이터 row 수: ', len(com_name))
            print(com_name)
            print(com_review)
        # IT는 372페이지까지 있음
        if k == 331:
            com_dict = {'기업명': com_name, '평균 별점': mean_star, '평균연봉': mean_salary, '기업 조회수': com_review, \
                        '복지 및 급여': welfare_salary, '업무와 삶의 균형': work_life_balance, \
                        '사내문화': com_culture, '승진 기회 및 가능성': promotion_pos, '경영진': com_head, \
                        '기업 추천율': com_recommendation, 'CEO 지지율': CEO_support, '성장 가능성': growth_pos}
            df = pd.DataFrame(com_dict)
            df.reset_index(drop=True, inplace=True)
            df.to_excel('job_planet.xlsx', index=False)
            driver.close()

    except Exception:
        print("program exception: 지금까지 작업했던 데이터들 우선 저장")
        com_dict = {'기업명': com_name[0:len(mean_star) - 2], '평균 별점': mean_star[0:len(mean_star) - 2], '기업 조회수': com_review[0:len(mean_star) - 2], \
                    '평균연봉': mean_salary[0:len(mean_star) - 2], '복지 및 급여': welfare_salary[0:len(mean_star) - 2], \
                    '업무와 삶의 균형': work_life_balance[0:len(mean_star) - 2], \
                    '사내문화': com_culture[0:len(mean_star) - 2], '승진 기회 및 가능성': promotion_pos[0:len(mean_star) - 2],
                    '경영진': com_head[0:len(mean_star) - 2], '기업 추천율': com_recommendation[0:len(mean_star) - 2],
                    'CEO 지지율': CEO_support[0:len(mean_star) - 2], '성장 가능성': growth_pos[0:len(mean_star) - 2]}
        df = pd.DataFrame(com_dict)
        df.reset_index(drop=True, inplace=True)
        df.to_excel('job_planet.xlsx', index=False)
        driver.close()
