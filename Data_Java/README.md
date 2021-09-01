## 1. JAVA&Mariadb Project (사원 급여 프로그램)

### <1>. db_sql
- 로컬에서 쿼리를 실행 시키면 테이블과 tutorial 정보가 저장
- table: department(부서), payment_info(급여정보), user_info(직원정보), user_score(직원 고과정보)
### <2>. db_test.java
- mian java 파일로 db_use.java 파일을 사용함
- 직원입력, 직원 고과정보 입력, 급여 입력, 조회 기능
- 조회: MIN MAX, COUNT, ALL 등으로 키워드를 치면 부서별로 생성
### <3>. db_use.java
- db 테이블에 접근하여 쿼리문을 통해 데이터 select, insert
- 중복된 클래스여서 따로 처리
- ![image](https://user-images.githubusercontent.com/50603209/131627316-2822b6e5-f214-484b-8385-d4a6aa30a074.png)

