## 1. JAVA&Mariadb Project (사원 급여 프로그램)

### <1>. db_sql
- 로컬에서 쿼리를 실행 시키면 테이블과 tutorial 정보가 저장
- table: department(부서), payment_info(급여정보), user_info(직원정보), user_score(직원 고과정보)
### <2>. db_test.java
- mian java 파일로 db_use.java 파일을 사용함
- Insertion: 직원입력, 직원 고과정보 입력, 급여 입력, 조회 기능
- Selection: MIN MAX, COUNT, ALL 등으로 키워드를 치면 부서별로 생성
### <3>. db_use.java
- db 테이블에 접근하여 쿼리문을 통해 데이터 select, insert
- 중복된 클래스여서 따로 처리
- 테이블 명을 치면 자동으로 insertion 가능
- You don't have to setInt, setString, etc for insertion. This program verifies the column type and automatically set data in its type.
![image](https://user-images.githubusercontent.com/50603209/131972006-cca69bb2-b47b-41a4-a2ef-a435060fea12.png)

