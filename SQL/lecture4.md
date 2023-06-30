230630 강의 내용입니다.

---

윈도우함수, erd, 요구사항 추출, 테이블생성

## ROLLUP
- ROLLUP 은 집계된 데이터에서 그룹별 소계, 총계를 구하기 위해서 사용됩니다.

- NULL row가 추가되어 해당 그룹에 해당하는 총계를 출력해줌

```sql
SELECT country
     , gender
     , COUNT(id) AS count_user
FROM users
GROUP BY ROLLUP(country, gender)
order by country, gender;
```


## WINDOW 함수

- 현재 행과 관련이있는 일련의 테이블 행에 대해 계산을 수행합니다.

- 분석 함수라고도 부르는 윈도우 함수는 행 그룹의 값을 계산하고 각 행마다 하나의 결과를 반환합니다. 행 그룹에 대해 하나의 결과를 반환하는 집계 함수와는 다릅니다.

- 윈도우 함수는 `OVER` 절을 포함합니다. 이 절은 평가 중인 행을 중심으로 행의 기간을 정의합니다. 각 행에 대한 윈도우 함수 결과는 선택된 행 윈도우를 입력으로 사용하여 집계 방식으로 계산됩니다.

- 윈도우 함수를 사용하면 이동 평균, 항목의 순위, 누적 합계를 계산하고, 기타 분석을 수행할 수 있습니다.

- 집계 함수와 다르게 윈도우 함수는 각 행마다 단일 값을 반환합니다

1. 탐색 함수 : LEAD, LAG, FIRST_VALUE, LAST_VALUE
  - 내 현재행의 위치를 기준으로 다른 행을 찾을 수 있습니다.
2. 번호 지정 함수 : RANK, DENSE_RANK, PERCENT_RANK, CUME_DIST, NTILE
  - 순위 매기기
3. 집계 분석 함수 : 집계 함수들, AVG, COUNT, SUM, MAX, MIN
  - 각 행마다 따로 계산할 수 있도록 제공함


### 윈도우 함수의 분류
- 그룹 내 순위 관련 함수(RANKING FAMILY)
    - RANK, DENSE_RANK, ROW_NUMBER
- 그룹 내 집계 관련 함수(WINDOW AGGREGATE FAMILY)
    - SUM, MAX, MIN, AVG, COUNT
- 그룹 내  행 순서 관련 함수
    - LAG, LEAD, FIRST_VALUE, LAST_VALUE, NTH_VALUE
- 그룹 내 비율 관련 함수
    - CUME_DIST, PERCENT_RANK, NTILE

### 형식
- PARTITION BY는 생략 가능
```SQL
WINDOW_FUNCTION ()
OVER (
    PARTITION BY ~ ORDER BY ~ WINDOW
)
```

## 순위 윈도우 함수

### RANK()
- 파티션 내에서 현재 행의 순위를 부여한다. 동일 값인 경우 동일 순위가 부여되고, 다음 순위는 동일값의 수만큼 건너뛰어 부여된다.
```SQL
select 
  id,
  first_name,
  last_name,
  country,
  age,
  RANK() OVER ( ORDER BY age DESC ) AS rank_number_in_all
from users
where id between 1 and 20
order by age;
```

```SQL
--최신가입 랭크
select 
  id,
  first_name,
  last_name,
  country,
  created_at, 
  age,
  RANK() OVER ( ORDER BY created_at DESC) AS rank
from users
where id between 1 and 20
order by created_at DESC;
```

- partition by 옵션 사용하기
- 윈도우 함수가 계산할 윈도우 크기(범위)를 설정합니다.
- 국가별 나이 순위
```sql
select 
  id,
  first_name,
  last_name,
  country,
  age,
  rank() over (partition by country order by age) as rank
from users
where id between 1 and 20
order by country, age;
```

### DENSE_RANK()
- 파티션 내에서 현재 행의 순위를 부여한다. 동일 값인 경우 동일 순위가 부여되고, 다음 순위는 건너뛰지 않고 순차 번호로 부여 된다.

- 즉 같은 등수가 여러명이고, 빠지는 순위는 없습니다.

> 1등, 2등, 2등, 2등, 3등, 3등, 4등 ..

```sql
select 
  id,
  first_name,
  last_name,
  country,
  age,
  dense_rank() over (partition by country order by age) as rank
from users
where id between 1 and 20
order by rank;
```

### ROW_NUMBER()
- 파티션 내에서 1부터 순차적으로 하나씩 증가하는 번호를 생성한다.
- rank와 다른건 그냥 row의 값이기 때문에 같은 값(공동2위)라도 숫자는 그대로 증가합니다.

```sql
select 
  id,
  first_name,
  last_name,
  country,
  created_at,
  ROW_NUMBER() OVER ( ORDER BY created_at ) AS order_number
from users
where id between 1 and 20

# order_number_in_country : 유저의 국가내에서 나이순 번호(나이가 같은 경우 순차적으로 번호 부여)
select 
  id,
  first_name,
  last_name,
  country,
  ROW_NUMBER() OVER ( PARTITION BY country ORDER BY age ) AS order_number_in_country
from users
where id between 1 and 20
```

### Rank 예제

- Raking With Group By
- 사용자의 소비 금액 랭크
```sql
select 
  user_id,
  round(sum(sale_price), 0) as total,
  rank() over( order by sum(sale_price) desc) as rnk
from order_items
group by user_id
order by rnk
```

## 탐색함수 (그룹 내 행 순서 관련 함수)

### LAG, LEAD
- LAG: 바로 앞
- LEAD: 바로 뒤

- 없는 행일 경우 `NULL`값이 입력됩니다.

```sql
select 
  id,
  first_name,
  last_name,
  lag(id) over(order by id) as id_prev,
  lead(id) over(order by id) as id_next
 from users
 where id in (1,2,3,4,5)
 order by id
 ```


 ```sql
 -- 이벤트 테이블에서 얼마만의 재방문인지 확인합니다
 select 
  id,
  user_id,
  created_at,
  lag(created_at) over(order by created_at) as created_at_prev,
  created_at - (lag(created_at) over(order by created_at)) as time_diff,
  extract('epoch' from  created_at - lag(created_at) over(order by created_at)) as prev_visit_second
 from events
 where user_id = 16006
 order by created_at
 ```


### FIRST_VALUE, LAST_VALUE

- FIRST_VALUE은 그룹 내의 첫값을 구하고, LAST_VALUE는 마지막 값을 구합니다.
- LAST_VALUE는 지금까지 읽은 행의 집합을 의미하기 때문에 항상 자기 자신입니다.
- 전체 그룹에 대한 마지막 값을 구하려면 ROWS 옵션을 주어야 합니다.


```sql
-- last_id가 10이 나오지 않음
select 
  id,
  email,
  created_at,
  FIRST_VALUE(id) OVER ( ORDER BY id ) as first_id,
  FIRST_VALUE(email) OVER ( ORDER BY id ) as first_email, 
  LAST_VALUE(id) OVER ( ORDER BY id ) as last_id,
  LAST_VALUE(email) OVER ( ORDER BY id ) as last_email
from users
where id between 1 and 10
```

- 맨 위부터 현재 행까지가 기본 윈도우 범위로 지정되기 때문에 last_id가 10이 발생하지 않고, 현재 id가 뜸

```sql
-- 윈도우 범위 전체로 강제설정해서 전체 범위에 대해 계산
select 
  id,
  email,
  created_at,
  FIRST_VALUE(id) OVER ( ORDER BY id ) as first_id, 
  LAST_VALUE(id) OVER ( ORDER BY id ) as last_id_current_window,
  LAST_VALUE(id) OVER ( ORDER BY id) as tmp,
  LAST_VALUE(id) OVER ( ORDER BY id ROWS BETWEEN UNBOUNDED PRECEDING AND UNBOUNDED FOLLOWING) as last_id_from_all,
  LAST_VALUE(id) OVER ( ORDER BY id rows between 2 preceding and 2 following) as prced_fol_2_last,
  FIRST_VALUE(id) OVER ( ORDER BY id rows between 2 preceding and 2 following) as prced_fol_2_first
from users
where id between 1 and 10
```
> 윈도우 범위 옵션
> `rows`를 하고 아래 범위 옵션으로 범위를 지정해줍니다.
> `UNBOUNDED PRECEDING` 은 맨 앞 위치
> `UNBOUNDED FOLLOWING` 은 맨 끝 위치
> `CURRENT ROW` 현재 위치
> `N PRECEDING` 현재에서 몇개 앞 까지
> `M FOLLOWING` 현재에서 몇개 뒤 까지


### NTH_VALUE
- 현재 윈도우 프레임에 있는 N번째 행의 값을 반환합니다. 이 행이 없으면 NULL을 반환합니다.

- 아래 예제는 5번째 요소가 존재하지 않음(윈도우 범위 때문에)
-그래서 위에 4개는 NULL이 출력됨
```sql
SELECT 
  id,
  email,
  created_at,
  NTH_VALUE(email, 5) OVER( ORDER BY id ) AS fifth_signup_user_email,
  NTH_VALUE(created_at, 5) OVER( ORDER BY id ) AS fifth_signup_user_created_at
FROM users
```

- 전체에 대해서 가지고 오고 싶으면 윈도우 범위 지정
```sql
SELECT 
  id,
  email,
  created_at,
  NTH_VALUE(email, 5) OVER(ORDER BY id ROWS BETWEEN UNBOUNDED PRECEDING AND UNBOUNDED FOLLOWING) AS fifth_signup_user_email,
  NTH_VALUE(created_at, 5) OVER(ORDER BY id ROWS BETWEEN UNBOUNDED PRECEDING AND UNBOUNDED FOLLOWING) AS fifth_signup_user_created_at
FROM users
LIMIT 100
```

- 예제
```sql
-- 각 제품의 브랜드별 1~3번 까지 제품ID 조회
select 
  id,
  name,
  brand,
  category,
  retail_price,
  NTH_VALUE(id, 1) OVER (
    PARTITION BY brand 
    ORDER BY retail_price desc
    ROWS BETWEEN UNBOUNDED PRECEDING AND UNBOUNDED FOLLOWING
  ) as first,
  NTH_VALUE(id, 2) OVER (
    PARTITION BY brand 
    ORDER BY retail_price desc
    ROWS BETWEEN UNBOUNDED PRECEDING AND UNBOUNDED FOLLOWING
  ) as second,
  NTH_VALUE(id, 3) OVER (
    PARTITION BY brand 
    ORDER BY retail_price desc
    ROWS BETWEEN UNBOUNDED PRECEDING AND UNBOUNDED FOLLOWING
  ) as third
from products
where brand IS NOT NULL
```


### 그룹 내 비율 관련 함수

- PERCENT_RANK()
  - 현재 행의 상대적 순위를 반환한다.
  - 계산에 따라 0과 1 사이의 범위에서 행의 백분율 순위를 계산한다.

```SQL
select 
  id,
  name,
  cost,
  PERCENT_RANK() OVER (ORDER BY cost) as percent_rank
from products
order by percent_rank
```

- CUME_DIST() - 누적분포
  - cumulative distribution
  - 0보다 크고 1보다 작거나 같은 값이 나옴.
  - n보다 값이 정렬순으로 이전이거나 같은 행의 갯수 / 현재 window 또는 파티션의 row 개수

```SQL
select 
  id,
  name,
  cost,
  CUME_DIST() OVER (ORDER BY cost )
from products
where brand = 'Lee';
```

- NTILE(n)
  - 레코드의 집합을 n개의 영역으로 구분하고 소속 영역을 구한다. 인수 n은 나눌 영역의 개수를 지정한다.
  - n개의 바구니에 나누어 담는다

  - 활용방법? 등급?

## 집계 분석 함수(그룹 내 집계 관련 함수)

### SUM(value)
- 파티션별 윈도우 내에서 지정된 value의 합을 계산한다.

```SQL
select id,
  name,
  category,
  retail_price,
  SUM(retail_price) OVER() as sum_retail_price,
  SUM(retail_price) OVER(ORDER BY id) as running_sum_retail_price,
  SUM(retail_price) OVER(PARTITION BY category) as sum_category_retail_price
from products
order by id
```

- 누적 합계
```SQL
select 
  value,
  sum(value) over( 
		order by value 
		ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW
	) as running_total
from value_list
order by id
```

- 최근 30일 합계
```SQL
elect 
  value,
  sum(value) over( order by value ROWS BETWEEN 29 PRECEDING AND CURRENT ROW) as total
from value_list
order by id
```

### MAX, MIN, AVG, COUNT


# data 생성

## CREATE, INSERT

- table 생성
```sql
create table weniv_product
(
    id   serial primary key,
    name varchar(30) null,
    cost int         null
);
```

- 테이블에 데이터 넣기 `INSERT`

> `INSERT INTO 테이블명 값`

```sql
INSERT INTO weniv_product (id, name, cost) VALUES (1, 'desk', 200000);
INSERT INTO weniv_product (id, name, cost) VALUES (2, 'monitor', 500000);
INSERT INTO weniv_product (id, name, cost) VALUES
(3, 'calender', 30000),
(4, 'pen', 1000),
(5, 'chair', 50000),
(6, 'bookshelf', 70000),
(7, 'wristband', 300),
(8, 'laptop case', 30000),
(9, 'sticker', 2500),
(10, 'key ring', 3500);
```


## UPDATE

- 조건에 맞는 기존 레코드를 수정할 수 있습니다. where로 여러개를 select하여 바꿀 수 있습니다. 
- 업데이트는 사고가 날 수 있기 때문에 주의를 기울여서 사용해야 합니다. select로 먼저 값을 확인하고 적용하고, where 로 조건이 잘 선택되었는지 확인해야 합니다.

- where문이 없으면 모든 레코드에 적용됩니다.

```SQL
UPDATE 테이블명
SET 컬럼명1 = 값1, 컬럼명2 = 값2, ...
WHERE 조건;
```

### 하나의 레코드에 업데이트
```sql
UPDATE weniv_product 
SET cost = 210100 
WHERE id = 1;
```


### 모든 레코드 업데이트

- where 문이 없으면 됨
```sql
update weniv_product 
set cost = cost + 100;
```


## DELETE

- 조건을 써주지 않으면 전부 다 삭제됩니다.

> 형식
```sql
DELETE FROM 테이블명 
WHERE 조건;
```

- where절에 조건을 걸어서 여러개를 삭제할 수 있습니다.

- 자주 사용하는 명령어는 아닙니다.

### 진짜로 삭제하나요?
- 만약 회원탈퇴를 하더라도 대부분 바로 삭제하지 않습니다.
- soft 삭제 라는 기법을 사용합니다. 
- 삭제여부를 표시하는 column을 따로 만들어서 논리적으로 삭제합니다.
  - del_yn, use_yn


## UPSERT

- 데이터가 없으면 추가하고 있으면 수정하는 명령어

- 예제 테이블 생성
```sql
DROP TABLE IF EXISTS customers;

CREATE TABLE customers (
	customer_id serial PRIMARY KEY,
	name VARCHAR UNIQUE,
	email VARCHAR NOT NULL,
	active bool NOT NULL DEFAULT TRUE
);


INSERT INTO
    customers (name, email)
VALUES
    ('IBM', 'contact@ibm.com'),
    ('Microsoft', 'contact@microsoft.com'),
    ('Intel', 'contact@intel.com');
```

-  고객 이름(customers_name_key)이 테이블에 있으면 그냥 무시(아무것도 하지 않음)합니다.

```sql
INSERT INTO customers (NAME, email)
VALUES('Microsoft','hotline@microsoft.com')
ON CONFLICT ON CONSTRAINT customers_name_key
DO NOTHING;
```

- 고객 이름(customers_name_key)이 테이블에 있으면 그냥 무시(아무것도 하지 않음)합니다.
```sql
INSERT INTO customers (name, email)
VALUES('Microsoft','hotline@microsoft.com')
ON CONFLICT (name)
DO NOTHING;
```

- 해당 name이 존재하면 update를 합니다.
```sql
INSERT INTO customers (name, email)
VALUES('Microsoft','hotline@microsoft.com')
ON CONFLICT (name)
DO
   UPDATE SET email = EXCLUDED.email || ';' || customers.email;
```


### CREATE

> CREATE DATABASE 데이터베이스명;

> 테이블 생성
```sql
CREATE TABLE 테이블명(
	컬럼명1 데이터_타입 [primary key],
	컬럼명2 데이터_타입
);
```

- 레코드 추가시 serial 로 id를 입력해주지 않아도 자동으로 생성되도록 함

```sql
create table sample_table2(
	id serial primary key,
	name varchar(12)
	);

-- id를 입력하지 않아도 자동으로 생성됩니다.
insert into sample_table2 (name)
values('aaaa');

select * from sample_table2;
```



## ALTER TABLE

- 기존 테이블에 다양한 제약조건을 추가, 수정, 삭제합니다. 

### 컬럼 추가
- 기존 테이블에 컬럼명을 추가할 수 있습니다.
```sql
ALTER TABLE 테이블명
ADD 컬럼명 데이터_타입;
```

```sql
ALTER TABLE sample_table2
ADD phone VARCHAR(11);
```

- 추가된 컬럼값은 모두 NULL로 되어있음...?

### 컬럼 삭제

> 형식
```sql
ALTER TABLE 테이블명
DROP COLUMN 컬럼명;
```

```sql
ALTER TABLE sample_table2
DROP COLUMN phone;
```

### 컬럼명 변경
- 컬럼의 이름을 변경해주는 함수
```sql
ALTER TABLE 테이블명
RENAME COLUMN 기존_컬럼명 TO 새로운_컬럼명;
```


### 데이터 유형 변경


## DROP

- DB, Table 삭제할 수 있습니다.

