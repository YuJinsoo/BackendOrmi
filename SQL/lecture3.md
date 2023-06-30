230629 강의 내용입니다.
---

## 조건분기 CASE

- 분기해주는 명령어로 SELECT 다음에 위치할 수 있습니다.

> CASE WHEN 
> 	조건 
> THEN 
> 	참일경우_실행구문 
> ELSE 
> 	거짓일경우_실행구문 
> END

```sql
SELECT
	CASE 
		WHEN true	THEN '참입니다'
	ELSE
		'거짓입니다'
	END

SELECT
	CASE 
		WHEN false	THEN '참입니다'
	ELSE
		'거짓입니다'
	END
```

- else if 라고 생각하면 됩니다.
```sql
SELECT 
CASE 
	WHEN floor = 1 THEN '1층 입니다.' 
	WHEN floor = 2 THEN '2층 입니다.'
	WHEN floor = 3 THEN '3층 입니다.'
	WHEN floor = 4 THEN '4층 입니다.'
ELSE 
	'층수가 없어요' 
END;
```
- Oracle의 경우에는 DECODE, CASE WHEN
- MsSQL의 경우에는 CASE WHEN
- MySQL의 경우에는 IF, CASE WHEN


- 예제
```sql
select order_id, user_id,
case 
  when status = 'Shipped' then '배송됨'
  when status = 'Processing' then '처리중'
  when status = 'Returned' then '반품됨'
  when status = 'Cancelled' then '취소됨'
  when status = 'Complete' then '완료됨'
  else '기타'
end as status_text
from orders
order by order_id;
```

```sql
select 
  id,
  cost,
  CASE
    WHEN cost <= 20 THEN '저비용' 
    WHEN cost <= 50 THEN '중비용'
    WHEN cost > 50 THEN '고비용'
    ELSE '없음'
  END as cost_level
from products
order by id
```

- 케이스 문으로 보기좋은 결과 표 만들기
```sql
select
  id,
  email,
  gender,
  case when gender = 'M' then 'O' end as is_male, -- 남성에만 값이 들어감 아니면 NULL
  case when gender = 'F' then 'O' end as is_female -- 여성에만 값이 들어감 아니면 NULL
from users

--count에 NULL 값은 뺴고 세는 특성을 이용해서.. 응용한 것 남성, 여성 숫자세기
select
  count(case when gender = 'M' then 'O' end) as male,
  count(case when gender = 'F' then 'O' end) as female,
  count(id) as total
from users

--연도별
select
  extract(year from created_at) as year,
  count(case when gender = 'M' then 'O' end) as male,
  count(case when gender = 'F' then 'O' end) as female,
  count(id) as total
from users
group by extract(year from created_at)
order by year;

--연도별, 연령대별
select
  extract(year from created_at) as year,
  count(case when age between 10 and 19 then '0' end) as "10_19",
  count(case when age between 20 and 29 then '0' end) as "20_29",
  count(case when age between 30 and 39 then '0' end) as "30_39",
  count(case when age between 40 and 49 then '0' end) as "40_49",
  count(case when age between 50 and 59 then '0' end) as "50_59",
  count(case when age between 60 and 69 then '0' end) as "60_69",
  count(case when age between 70 and 79 then '0' end) as "70_79",
  count(id) as total
from users
group by extract(year from created_at)
order by year;

select 
	id,
	email,
	age,
	trunc(age, -1) as age_group
from users; 

--분기별 가입자수
select 
	extract(year from created_at) as year,
	extract(quarter from created_at) as quarter,
	count(id) as user_count
from users
group by year, quarter

-- 이걸 옆으로 펼치고 싶다!
select
	extract(year from created_at) as year,
	count(case when extract(quarter from created_at) = 1 then '0' end) as q1,
	count(case when extract(quarter from created_at) = 2 then '0' end) as q2,
	count(case when extract(quarter from created_at) = 3 then '0' end) as q3,
	count(case when extract(quarter from created_at) = 4 then '0' end) as q4,
	count(id) as total
from users
group by year
order by year
```

## JOIN

- 기준을 가지고 데이터를 합칩니다.
- INNER JOIN, LEFT JOIN, RIGHT JOIN, FULL OUTER JOIN ...
- INNER JOIN = JOIN (얘만 INNER JOIN)
- 나머지는 OUTER JOIN

- 합쳐진 테이블을 기준으로 WHERE~ 이 적용되어 다양한 값을 얻을 수 있습니다.

### INNER JOIN (=JOIN)

- 형식
```SQL
select table1.id, table2.id
from table1
[inner] join table2 
	on table2.id=table1.id
```

- 어떤 column으로 join 되는지 `on`으로 지정해줌
```sql
select *
from weniv_order join weniv_user on weniv_order.user_id = weniv_user.id;
```

- 위에건 너무 길기 때문에 별칭으로 지정할 수 있습니다.
```sql
-- 처리 row 8개
select *
from weniv_order o
join weniv_user u
	on o.user_id = u.id;
```

### LEFT JOIN
- 왼쪽 테이블 (from에서 지정한 테이블) 의 내용은 모두 보여주고, join한 테이블에서 없는 값이라면 NULL로 처리합니다.

```sql
-- 처리 row 10개
select *
from weniv_order o
left join weniv_user u
	on o.user_id = u.id;
```

- join은 여러개를 연달아서 join 해줄 수 있습니다.
```sql
select *
from weniv_order o
left join weniv_user u on o.user_id = u.id
left join weniv_product p on o.product_id = p.id;
```

- 차이점 확실히 알아야 합니다.
```sql
Vselect *
from weniv_user u
join weniv_order o on u.id = o.user_id
order by u.id;


select *
from weniv_user u
left join weniv_order o on u.id = o.user_id
order by u.id;
```

### CROSS JOIN
- 두 테이블에서 가능한 모든 행 조합을 반환합니다.
- 대체 언제 쓰일까? 모든 경우의 수를 만들어서 복잡한 노가다가 필요한 경우에 쓰입니다.

```sql
select table1.id,table2.id
from table1, table2

select table1.id, table2.id
from table1
cross join table2
```

### 트랜잭션 데이터(transaction data)
- 트랜잭션 데이터는 다양한 애플리케이션에서 일상적인 비즈니스 프로세스를 실행하거나 지원할 때 생성되는 데이터

- ex) 주문 데이터

### 마스터 데이터(master data)
마스터 데이터는 트랜잭션에서 참고되는 각종 정보
- ex) 회원데이터, 상품데이터


---
## UNION
- 집합 작업은 둘 이상의 쿼리 결과를 단일 결과로 결합하는 데 사용됩니다. 결합된 쿼리는 동일한 수의 열을 반환해야 합니다. 호환 가능한 데이터 유형. 해당 열의 이름은 다를 수 있습니다.


### UNION ALL 합집합
- UNION은 두 결과 집합의 결과를 결합하고 중복을 제거합니다. union all은 중복 행을 제거하지 않습니다.

```SQL
select * from weniv_user as user1
UNION ALL
select * from weniv_user3 as user3
```

### UNION DISTINCT
- 중복을 제거합니다.
```SQL
select * from weniv_user as user1
UNION DISTINCT
select * from weniv_user3 as user3
```

### INTERSECT DISTINCT
- 두 결과 집합 모두에 나타나는 행만 반환합니다.
```SQL
select * from weniv_user as user1
INTERSECT DISTINCT
select * from weniv_user3 as user3
```
### EXCEPT DISTINCT
- EXCEPT 첫 번째 결과 집합에는 나타나지만 두 번째 결과 집합에는 나타나지 않는 행만 반환합니다.
```SQL
select * from weniv_user as user1
EXCEPT DISTINCT
select * from weniv_user3 as user3
```

### 예제

- UNION으로 합칠 때에는 필드(COLUMN)의 개수와 타입이 일치해야 합니다.

```SQL
select 
  CAST(extract(year from created_at) AS TEXT) as year,
  count(id) as user_count
from users
group by year
UNION ALL
select 
  'TOTAL' as year,
  count(id) as user_count
from users
order by year
```


## 서브쿼리

- 중첩된 쿼리문을 의미합니다.
- 서브쿼리는 다른 SQL문 안에 중첩된 SELECT 문입니다.

```SQL
select *
from orders
where user_id in (
	select id
	from users
	where country='Brasil'
);

```
- 서브 쿼리는 데이터를 쿼리하고 조작하는 데 매우 유용할 수 있으며 SQL 문을보다 효율적이고 유연하게 만드는 데 도움이 될 수 있습니다.



- where 절, join 절, select 절 에서 괄호를 이용해 사용할 수 있습니다.
```sql
-- from에서 사용
select id,
  a.first_name,
  a.last_name,
  b.order_count as order_count
from users a
left join (
    select user_id, count(order_id) as order_count 
    from orders
    group by user_id
  ) b on a.id = b.user_id
order by a.id
limit 10;
```

```sql
-- where 에서 사용
select id,
  first_name,
  last_name
from users
where id in (
  select user_id 
  from orders
  group by user_id 
  having count(order_id) >= 3
)
```

```sql
-- select에서 사용
select id,
  first_name,
  last_name,
  (select count(order_id) from orders where user_id = u.id) as order_count
from users u
order by u.id
limit 10;
```

> `select`에 `sub query`가 있는 경우, 해당 column 값을 조회할 떄마다 계속 같은 쿼리를 계산해야 합니다. 그렇기 때문에 조회해야할 데이터가 많아지면 속도에서 매우 불리합니다.

- sub query 안에 sub query 가능합니다.
- sub query를 많이 사용하기는 하지만 DBMS의 최적화 기능을 이용하기 위해서는 join으로 변경해줍니다.
```sql
select *
from products p 
where id in (
	select product_id
	from order_items
	where user_id in(
		select id
		from users
		where country = 'Brasil'
		)
	)
```

## WITH (Common Table Expression)
- with 절은 쿼리 내에서 임시 결과를 정의하고 사용합니다.

- 주요 사용 목적은 복잡한 추출 과정을 분할하여 단계적으로 처리하면서 전체 데이터 추출과정을 단순화시키는 것 입니다.

- 큰 문제를 작은 문제 단위 여러개로 쪼개서 쉽게 풀이할 수 있습니다.

- 자주 사용하는 값들을 with로 정의해두면 편리합니다.

> 사용법 : WITH CTE명 AS ( 쿼리 표현식 )
```sql
WITH user_data AS (select id from users)
select * from user_data
```
> - user_data CTE(유사 테이블)을 정의합니다. 내용은 users의 id값을 조회하는 서브쿼리입니다.
> - user_data 로 부터 데이터를 조회 합니다.


- 예제
- user_data와 user_order_counts 라는 임의의 테이블을 만들어두고, 나중에 불러다가 from과 join에서 선택해서 사용할 수 있습니다.
- 아래처럼 `,`로 구분하여 여러개를 선언해줄 수 있습니다.
```sql
WITH user_data AS (
	select id, email
	from users
	),
user_order_counts as (
	select 
		user_id,
		count(order_id) as order_count
	from orders
	group by user_id
)
select 
	t1.id,
	t1.email,
	t2.order_count
from user_data t1
join user_order_counts t2 on t1.id = t2.user_id;
```

### 유저 아이디별 주문건수
```sql
WITH user_order_counts AS (
  select user_id, count(order_id) as order_count 
  from orders
  group by user_id
) 
select * from user_order_counts
order by order_count desc;
```

### 회원수가 4000명 이상인 국가명과 국가의 회원수
```sql
WITH user_counts AS (
  select 
    country, 
    count(id) as user_count
  from users
  group by country
  having count(id)>=4000
)
select * from user_counts;
```

### 브라질과 일본의 유저 아이디 목록 조회
```sql
WITH user_id_brasil AS (
  select id, country 
  from users
  where country = 'Brasil' limit 10
),
user_id_japan AS (
  select id, country 
  from users
  where country = 'Japan' limit 10
)
select id, country from user_id_brasil
UNION ALL
select id,country from user_id_japan
```

### 유저별 이름과 주문수, 이벤트수 정보 조회
```sql
WITH user_order_counts AS (
  select user_id, count(order_id) as order_count 
  from orders
  group by user_id
), user_event_counts AS (
  select user_id, count(id) as event_count 
  from events
  group by user_id
) 
select 
  a.id,
  a.first_name,
  a.last_name,
  b.order_count,
  c.event_count
from users a
left join user_order_counts b on a.id = b.user_id 
left join user_event_counts c on a.id = c.user_id
order by a.id;
```