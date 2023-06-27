# SQL

- Sturcted Query Language : 구조화된 요청 언어
- DBMS는 달라도 SQL은 공통이기 때문에 대동소이 합니다. 그렇기 때문에 한번 익혀두면 다른 DBMS 프로그램도 잘 다를 수 있습니다.

> 노션링크 : https://paullabworkspace.notion.site/SQL-with-PostgreSQL-16a28e7c00474b6b90ab2850d1e54301


- DB: 데이터베이스. 자료의 집합
- DBMS(DataBase Management System): DB를 효율적으로 관리하기 위한 software
- RDB: 관계형 데이터베이스
- RDBMS: RDB를 관리하는 소프트웨어

- 많이 사용하는 RDBMSOracle, SQL Server, PostSQL, MySQL

- MS 진영의 DBMS 특징 : 튜닝할부분이 별로 없어서 좋음
- 오픈소스 DBMS 특징 : 큰 커뮤니티 장점. 대용량 트래픽시 튜닝을 해줘야한다?

## SQL 종류
- 데이터 조작어(DML)
  : SELECT, INSERT, UPDATE, DELETE

- 데이터 정의어 (DDL)
  : CREATE DATABASE, CREATE TABLE, CREATE INDEX, ALTER ADTABASE, ALTER TABLE ...

- 트랜잭션 : 작업을 세트로 묶어서...성공했을때 데이터베이스에 반영 (실패하면 롤백?)
- 트랜젝션 제어어 (TCL)
  : COMMIT, ROLLBACK, SAVEPOINT


## 찾아서 공부해볼 키워드
- 트래픽이 많아지면 분산처리, 로드밸런스, 캐시레이어 ...?


## 참고 사이트
1. 사이트
  - https://sqlschool.co.kr/
  - w3 sql tutorial : 굉장히 깊게 알려주진 않지만 꼭 필요한것은 최소한으로하여 알려줌

2. 도구
  - jetbrain - datagrip 쓸수있으면 추천 (학교이메일 있으면 무료?)


- 우리 강의는 DBeaber라는 도구로 DB에 접속하여 SQL 실습 할 것입니다.

## DB 접속

- DBeaber를 설치

> 새 데이터베이스 연결 - PostgreSQL 선택하고 위 정보 입력해서 연결. 드라이버 설치(PostgreSQL JDBC Driver 42.5.2??)

- 아래 내용을 입력해 DB에 접속합니다.

```plain text
Host: ls-1cd264b85086b397d3799fc2e6498927fdb3785a.cg0aaxf2hjqt.ap-northeast-2.rds.amazonaws.com
Port: 5432
database name: dbstudy

Username: sqlstudy
Password: FUYzVFF6YP4WqhA
```

- dbstudy - Schemas - public 안에 있는 테이블들을 볼 것입니다.


## SQL 편집기
- `[SQL 편집기] - SQL 편집기` 에서 SQL을 작성해서 쿼리를 날릴 수있습니다.
- `ctrl+Enter` 로 쿼리를 실행시킬 수 있습니다.

### DB column name TIP!

- 일반적인 관례를 가진 column 이름을 쓰는게 좋음. 회사에 가면 회사의 룰을 따라서 쓰면 됩니다.
 ex) id, created_at, updated_at etc..
 프레임워크에서 알아서 스스로 찾아서 쓰게끔 만들어짐
 


### SELECT

- select뒤에 있는 값을 표현이 가능하다.

```sql
select ~~;
```

- ~~에
- 사칙연산 가능
%연산 가능 (// 는 안됨)

- 문자열 붙이는 연산 || (+ 는안됨), concat()
```sql
select 'hello' || 'world';
select concat('hello',' ','world');
```

- user 테이블의 모든(*) 데이터 조회하기
```sql
select * from "user";
```

- 원하는 column만 가져오기 (id, first_name)
```sql
select id, first_name from "user";
```

### to_char(값, 패턴) 함수

- 계산한 값이 integer일때 char로 출력하고 싶을 떄, to_char(값, 패턴)함수를 사용
패턴에 9를 자리수만큼 써주면 됨.
to_char(int값, '9999')

```sql
select 
	id product_id,
	category product_category,
	name product_name,
	retail_price product_price,
	cost product_cost,
	retail_price-cost product_profit,
	to_char((retail_price-cost)/cost*100, '99.99%') product_profit_rate
from products;

-- product_profit_rate column은  __.__% 로 출력됨
```

### AS

- AS는 해당 컬럼의 이름을 다시 정해서(별칭을 정하여) 보여주는 기능입니다. 

```sql
select 
  id as product_id,
  name as product_name,
  retail_price as product_price,
  cost as product_cost,
  retail_price - cost as product_profit
from products;
```

- 주로 식으로 된 컬럼의 컬럼명을 설정하거나 기존의 컬럼명을 보다 간결하게 또는 보다 가독성 있게 설정하는데 사용합니다.
- column 값 끼리 값을 계산해서 새로운 column으로 값을 보여주고 싶을 때 사용하는 함수입니다.

- 사용하지 않아도 공백 1칸 뒤에 이름을 지정할 수 있습니다.

```sql
select age, 2023-age as birth_year from users;

select age, 2023-age birth_year from users;
```

- 테이블 명도 지정할 수 있습니다.
- 테이블 명에 as를 지정해서 해당 테이블의 column을 쉽게 지정할 수 있습니다.
```sql
select a.id, a.name from products as a;
select a.id, a.name from products a;
```

### LIMIT

- LIMIT는 조회할 결과의 레코드수(row 수)를 제한합니다. 

- LIMIT가 없이 조회를 하면 모든 레코드를 조회하지만 LIMIT <조회할 레코드 수> 를 이용하면 지정한 만큼의 결과 개수만 가지고 옵니다.

- 위치는 `from` 뒤에 붙입니다.

```sql
select * from products limit 5;
```

### DISTINCT

- 결과에서 중복되는 행을 제거합니다.
- 중복된 값을 제거할 `column` 앞에 `DISTINCT`를 붙입니다.
- 여러 개를 지정할 수 있습니다.

```sql
select distinct country from users;

select 
  distinct country, city
from users;

```