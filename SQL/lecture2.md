2023-06-28 강의입니다.

## WHERE

- 데이터에 조건을 부여해서 원하는 데이터만 필터링한 결과를 조회합니다.
- 결합 가능한 연산자의 종류 
  1. 비교연산자(=, <, >, !=, >=, <=)
  2. SQL연산자(BETWEEN)
  3. 논리 연산자(AND, OR) 등

```sql
select *
from users 
where age > 30
and country = 'Brasil';

select *
from users 
where age > 30
or country = 'Brasil';

select * from users where NOT(country = 'United States' or country = 'Brasil');
```

### 논리연산자도 가능합니다.
- `<` `>` ...
```sql
SELECT *
FROM users
WHERE traffic_source <> 'Search';

select 
	id, first_name, last_name 
from users 
WHERE traffic_source != 'Search';
```

- **BETWEEN 연산**
- 설정된 범위를 간단하게 표현합니다.
- between A AND B : A와 B를 포함한 사이의 값

```sql
-- 두 쿼리는 같은 결과값
select * 
from users
where age between 20 and 30

select * 
from users
where age>=20 and age<=30
```

- **날짜 형식**도 논리연산자, between 연산 모두 사용이 가능합니다.
- 날짜는 timestamp 라는 타입!
- 날짜의 경우 시간을 지정하지 않으면 `00시 00분 00초` 로 고려해서 계산합니다.
```sql
select *
from users
where created_at between '2020-01-01' and '2020-02-01';
```

### IN 연산자
- IN A : A안에 값과 일치하는 값을 조회 
- in 조건중에 하나라도 일치하면 선택됩니다.

```sql
select * 
from products
where brand in ('Onia', 'Hurley', 'Matix');
```

```sql

select * 
from users
where id in (1978,4834,37153,49725,61293,63470,74653,80628,84078,41307,44567,45095,60864,97606,9432,20729,21930,33675);
```

### LIKE 연산
- 비교 문자와 형태가 일치 (`%` : 모든 문자, `_`: 한 글자)
- 대소문자를 가리지 않음

- `%`사용
```sql
-- Young이 들어가는 것 찾기
select * 
from products
where name like '%Young%';

-- Hurley로 시작하는 것 찾기
select * 
from products
where name like 'Hurley%';

-- T-shirt로 끝나는 것 찾기
select * 
from products
where name like '%T-shirt';
```

- `_`사용. 자리수 일치하는대로 출력합니다.

```sql
select distinct first_name
from users
where first_name like 'Da___'
```

### IS NULLL
- NULL값을 갖는 값을 찾습니다.
- NULL이 아닌 것은 `IS NOT NULL`을 사용합니다.

```sql
select * 
from order_items
where shipped_at IS NULL;

select * 
from order_items
where shipped_at IS NOT NULL;
```
> NULL(빈 값) != 'NULL'(문자값) 서로 타입이 다르다 → `IS`로 비교

---

## 집계함수

- 집계 함수(aggregate function)는 여러 행으로부터 하나의 결과값을 반환하는 함수입니다.

### COUNT
- count 함수는 해당 항목 레코드 개수를 반환합니다.
```sql
select count(id) 
from users;
```
- 중복을 제거해서 카운팅하기도 합니다.
```sql
select count(distinct city) 
from users;
```

> COUNT(별표)와 COUNT(컬럼명) 차이
> COUNT(별표) : NULL값 포함 O
> COUNT(컬럼명) : NULL값 포함 X

### SUM
- 해당 항목 레코드의 합계를 반환하는 함수입니다.
```sql
select sum(retail_price)
from products
```

### AVG
- 해당 항목 레코드의 평균을 반환하는 함수입니다.
```sql
select avg(cost)
from products;
```

### MAX, MIN
- 최대, 최소
```sql
select max(cost), max(retail_price)
from products;

select min(cost), min(retail_price)
from products;
```

### VARIANCE, STDDEV
- 분산 VARIANCE
- 표준편차 STDDEV

```sql
select variance(retail_price)
from products

select stddev(retail_price)
from products
```

---

## GROUP BY
- 특정 항목을 기준으로 그룹화하여 조회할 수 있습니다. 데이터를 그룹화 하여 조회할 때, 그룹화 하려는 항목이 select 에 들어가야 합니다.

- `group by` 는 where의 뒤에 위치해야 합니다.

```sql
select country, count(id) 
from users
group by country;
```

- 여러 column에 대해 groupping 할 수 있습니다.
```sql
select country, city, count(id) 
from users
group by country, city;
```

- 어떤 흐름으로 가야하는지??
- 카테고리별로 판매금액 합을 알고 싶다면
- 카테고리 조회 > 컬럼 선택 > 통계내릴 함수 순으로 생각하면서 적용해본다.
```sql
select 
	category, 
	sum(retail_price) as sum_retail_price  
from products
group by category;
```
- 카테고리 별 평균 구하기.
```sql
select
	category, avg(cost)
from products
group by category;
```

- 브랜드별 최대, 최소 가격 조회하기
```sql
select 
	brand, 
	max(retail_price) as max_retail_price, 
	min(retail_price) as min_retail_price
from products
group by brand;
```

---

## HAVING
- **그룹화된 데이터**에 조건을 부여합니다. 
- 그룹화된 데이터에 조건을 부여하므로 GROUP BY와 함께 사용합니다.

- from > where > group > having
- 위치는 group by 뒤입니다.

```sql
select 
  country, 
  count(id) as user_count
from users
group by country
having count(id) >= 4000;
```

---

## ORDER BY
- 출력 결과 정렬합니다.

- 오름차순 : ASC(기본, 작은 수에서 큰 수로, Ascending)
- 내림차순 : DESC(큰 수에서 작은 수로, Descending)

- 디폴트는 오름차순이므로 오름차순은 굳이 안써줘도 됩니다.
- having 의 다음입니다.

```sql
-- 내림차순
select * 
from users
order by age desc;

-- 오름차순
select * 
from users
order by age asc;
```

- 2차정렬도 가능함. 나이정렬 + first_name 순
```sql
-- 나이 내림차순 정렬 이름 오름차순 정렬
select * 
from users
order by age desc, first_name asc;
```

- limit 과의 조합
```sql
select * 
from users
order by age
limit 3;
```

- 가장 최근 가입자 10명
```sql
select * 
from users
order by created_at desc
limit 10;
```

## SQL 작성 순서

- 아래 순서대로 작성하는 것을 명심하지

1. from
2. where
3. group by
4. having
5. select
6. order by
7. limit

- 위 순서로 국가별 20세 이하 유저수가 500명 이상인 유저수 국가 TOP 5를 조회하는 과정입니다.

```sql
--
select *
from users

-- 20세 이하
select * 
from users
where age <= 20;

-- 유저 수를 확인
select count(id) as user_count
from users
where age <= 20;

-- 국가별
select
	country,
	count(id) as user_count
from users
where age <= 20
group by country;

-- 그룹나눈거에서 조건있나? 500명 이상
select
	country,
	count(id) as user_count
from users
where age <= 20
group by country
having count(id) >= 500;

-- 유저 수 top 5이므로 정렬 후 5개만 출력
select
	country,
	count(id) as user_count
from users
where age <= 20
group by country
having count(id) >= 500
order by user_count desc
limit 5;
-- 완성!
```



## 숫자함수
- round : 해당 항목 레코드의 숫자를 반올림
> round(숫자, 자리수)
```sql
select round(10.555) --11
select round(12.123412, 3) -- 12.123
```

- trunc : 해당 항목 레코드의 숫자를 내림(절삭)하여 출력하는 함수
> trunc(숫자, 자리수)
```sql
select trunc(10.555) -- 10
select trunc(10.555, 2) -- 10.55
```
- mod : 해당 항목 레코드의 숫자를 나누기하여 나머지를 출력
> mod(숫자, 나눌 값)
```sql
select mod(10,3) --1
```

- power: 해당 항목 레코드의 숫자를 제곱하여 출력
> power(밑, 제곱수)
```sql
select power(10,3) -- 1000
```
- sqrt : 해당 항목 레코드의 제곱근을 출력
```sql
select sqrt(10) -- 3.16227...
select sqrt(4) -- 2
```

---

## 문자열 함수

-  substr : 문자열의 일부만 출력할 수 있습니다. 
  - 문자열의 시작 인덱스는 1 입니다. (음수로 지정할 수 있지만 무시당함)
> substr(문자열, 시작 위치, 길이)
```sql
select substr('hello world', 1, 5) -- hello
select substr('hello world', 0, 5) -- hell
select substr('hello world', -1, 5) -- hel

select substr('hello world', 3, 5) -- llo w
select substr('hello world', 3) -- llo world
```
-  left : 문자열을 왼쪽에서 얼만큼 자를 지 설정한 후에 조회
> left(문자열, 길이)
```sql
select left('064-000-0000',3) -- 064
```

-  right : 문자열을 오른쪽에서 얼만큼 자를 지 설정한 후에 조회
> left(문자열, 길이)
```sql
select right('064-000-0000',3) -- 000
```

-  concat : 여러 문자열을 하나로 연결할 수 있습니다.
```sql
select concat('paul', '-', 'lab') -- paul-lab
```
  - 연결연산자(`||`)로도 가능하다 
```sql
select 'paul' || '_'|| 'lab' -- paul_lab
```

-  lower : 문자열을 모두 소문자로 변경
```sql
select lower('AaBbCcDd') -- aabbccdd
```
-  upper : 문자열을 모두 대문자로 변경
```sql
select upper('AaBbCcDd') -- AABBCCDD
```
-  initcap : 제일 앞 글자만 대문자로
```sql
select initcap('AaBbCcDd') -- Aabbccdd
```

-  replace
> replace(문자열, 바꾸고 싶은 값, 바꿀 값)
```sql
select replace('hello world', 'world', 'sql')
-- hello sql
```

-  length : 문자열의 길이를 출력합니다. COUNT와 비교해서 기억해주세요
```sql
select first_name, length(first_name)
from users;
```

-  position : 글자가 포함된 위치를 int로 반환합니다. index는 1부터 시작합니다.
```sql
select POSITION('b' IN 'abcdef');

-- 아이디 혹은 도메인만 추출 가능
select email, POSITION('@' IN email)
from users
```

-  coalesce: 해당 컬럼에 NULL값이 있는 경우 다른 값으로 채워넣을 수 있습니다.
- 다른 DBMS에는 `ifnull`이라는 함수가 있는데 postgre는 없고 이 함수가 있습니다.
```sql
select coalesce(name, '담당자 지정 안됨')
from weniv_event;

select coalesce(name, null, 'a')
from weniv_event;

select coalesce(name, null, null)
from weniv_event;
```

-  ascii : 아스키 코드 번호르 리턴하는 함수입니다.


## 형변환

- 형변환은 아래와 같은 형식으로 진행합니다.
> CAST(데이터 AS 타입명)
> 데이터::타입명

### 문자열 형변환
- 예제
- text는 좌측정렬 숫자는 우측정렬됨(고정인지는 확신하지 않음)
```sql
# 문자열 -> 숫자로 바꾸는거
# 문자열 -> 자연수(INTEGER)
# 문자열 -> FLOAT

select CAST('123' AS INT);
select '123' + '123' # 에러;
select CAST('123' AS INT) + CAST('123' AS INT);
select CAST('123.123' AS FLOAT);
select CAST('123' AS NUMERIC);
select CAST('123.123' AS NUMERIC);

select '123'::INT;
select '123.123'::NUMERIC;
select '123.123'::TEXT;
```

### 숫자 형변환

```sql
-- 숫자(INTEGER) -> 문자
-- 숫자(FLOAT) -> 문자
-- true, false -> 문자
select CAST(123 AS TEXT)
select CAST(123.123 AS TEXT)
select CAST(true AS TEXT)
select CAST(false AS TEXT)
select CAST(NULL AS TEXT)

select 123::TEXT;
select 123.123::TEXT;
select true::TEXT;
```

### 날짜타입 형변환

``` sql
-- 날짜 타입
-- 1) DATE
-- 문자열 -> DATE
-- 2) DATETIME
-- 문자열 -> DATETIME

select DATE('2011-12-01 11:12:34')

SELECT '2011-12-01 11:12:34'::DATE;
SELECT '2011-12-01 11:12:34'::TIME;
SELECT '2011-12-01 11:12:34'::TIMESTAMP;
```

---

## 날짜함수

- 날짜의 표현 방법
```sql
--현재날짜
SELECT CURRENT_DATE;
--현재날짜시간
select current_timestamp;
--현재날짜시간, 시차
select now();
```

- 날짜타입으로 변환해서 검색할 수 있다. 이러면 날짜까지만 따지기 때문에 시, 분, 초를 고려하지 않아도 됩니다.
```sql
select 
	id,
	email,
	created_at::DATE
from users
where created_at::DATE between '2021-01-01' and '2021-01-31';
```

### EXTRACT : 데이터 추출
  - 날짜의 각 요소인 year, month day를 추출할 수 있습니다.
```sql
SELECT EXTRACT(YEAR FROM DATE '2023-1-1');
SELECT EXTRACT(MONTH FROM DATE '2023-1-1');
SELECT EXTRACT(DAY FROM DATE '2023-1-1');
```
  - 현재 시간의 데이트 값을 가져와서 추출하기
```sql
select extract(year from date(now()))
--시간까지...
select extract(hour from now())
```
  - 분기별로 뽑을 수도 있음
```sql
select 
	created_at,
	extract(quarter from created_at)
from users;
```

### to_char(데이터, 양식): 특정 포맷으로 문자열을 출력해주는 함수

```sql
SELECT TO_CHAR(DATE '2023-01-25', 'MM/DD/YYYY') AS US_format;
SELECT TO_CHAR(DATE '2023-01-25', 'YYYY-MM-DD') AS KD_format;

SELECT TO_CHAR(TIMESTAMP '2023-01-25 15:30:25', 'MM/DD/YYYY HH24:MI:SS') AS US_format;
SELECT TO_CHAR(TIMESTAMP '2023-01-25 15:30:25', 'YYYY-MM-DD HH24:MI:SS') AS KD_format;
```

## 날짜, 시간 차이 구하기

```sql
--날짜 차이계산 음수도 나옴.
select DATE '2023-08-27' - DATE '2023-06-26' AS date_difference;

select '2023-08-27'::DATE - '2023-06-26'::DATE;

select '2023-06-26'::DATE - '2023-08-27'::DATE;
```

```sql
--시간도 차이 구할 수 있습니다.
select TIME '12:30' - TIME '10:45' AS time_difference;
select TIMESTAMP '2023-06-27 12:30' - TIMESTAMP '2023-06-26 10:45' AS time_difference;
```

```sql
-- 예제
select delivered_at - created_at 
from orders
where status = 'Complete'
```

### interval : 지정된 시간 간격을 추가 및 빼는 함수입니다.

```sql
select '2023-1-25'::DATE + interval '5 day'; -- 5일 후
select '2023-1-25'::DATE - interval '5 day'; -- 5일 전

select '2023-1-25'::DATE + interval '5 month';
select '2023-1-25'::DATE - interval '5 month';

select '2023-1-25'::DATE + interval '5 year';
```

```sql
select NOW() + interval '1 day';

SELECT '2023-12-25 15:30:00'::TIMESTAMP + INTERVAL '10 MINUTE'; -- 10분 후
SELECT '2023-12-25 15:30:00'::TIMESTAMP - INTERVAL '10 MINUTE'; -- 10분 전

SELECT created_at::TIME, (created_at + INTERVAL '10 minute')::TIME
from users;
```