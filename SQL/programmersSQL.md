## 문제: 루시와엘라 찾기
- LEVEL 2
- https://school.programmers.co.kr/learn/courses/30/lessons/59046
```sql
SELECT 
    ANIMAL_ID,
    NAME,
    SEX_UPON_INTAKE
FROM ANIMAL_INS
WHERE NAME IN ('Lucy', 'Ella', 'Pickle', 'Rogan', 'Sabrina', 'Mitty')
ORDER BY ANIMAL_ID;
```

---

## 문제: 나이 정보가 없는 회원 수 구하기
- LEVEL1
- https://school.programmers.co.kr/learn/courses/30/lessons/131528
```SQL
SELECT COUNT(USER_ID)
FROM USER_INFO
WHERE AGE IS NULL;
```

## 문제: 가장 비싼 상품 구하기
- LEVEL1
- https://school.programmers.co.kr/learn/courses/30/lessons/131697
```SQL
SELECT MAX(PRICE) AS MAX_PRICE
FROM PRODUCT;
```

## 문제: 최솟값 구하기
- LEVEL2
- https://school.programmers.co.kr/learn/courses/30/lessons/59038
```SQL
SELECT MIN(DATETIME)
FROM ANIMAL_INS;
```

## 문제: 동물 수 구하기
- LEVEL2
- https://school.programmers.co.kr/learn/courses/30/lessons/59406
```SQL
SELECT COUNT(ANIMAL_ID)
FROM ANIMAL_INS;
```

## 문제: 중복 제거하기
- LEVEL2
- https://school.programmers.co.kr/learn/courses/30/lessons/59408
```SQL
SELECT COUNT(DISTINCT(NAME))
FROM ANIMAL_INS
```

---

## 문제: 어린 동물 찾기
- LEVEL1
- https://school.programmers.co.kr/learn/courses/30/lessons/59037#fn1
```SQL
SELECT ANIMAL_ID, NAME
FROM ANIMAL_INS
WHERE NOT INTAKE_CONDITION = 'Aged';
```

## 문제: 아픈 동물 찾기
- LEVEL1
- https://school.programmers.co.kr/learn/courses/30/lessons/59036
```SQL
SELECT ANIMAL_ID, NAME
FROM ANIMAL_INS
WHERE INTAKE_CONDITION = 'Sick';
```

## 문제: 이름이 있는 동물의 아이디 
- LEVEL1
- https://school.programmers.co.kr/learn/courses/30/lessons/59407
```SQL
SELECT ANIMAL_ID
FROM ANIMAL_INS
WHERE NAME IS NOT NULL
ORDER BY ANIMAL_ID;
```

## 문제: 인기있는 아이스크림
- LEVEL1
- https://school.programmers.co.kr/learn/courses/30/lessons/133024
```SQL
SELECT FLAVOR
FROM FIRST_HALF
ORDER BY TOTAL_ORDER DESC, SHIPMENT_ID ASC;
```

## 문제: 상위 N개 레코드
- LEVEL1
- https://school.programmers.co.kr/learn/courses/30/lessons/59405
```SQL
SELECT NAME
FROM ANIMAL_INS
ORDER BY DATETIME
LIMIT 1;
```

## 문제: 여러 기준으로 정렬하기
- LEVEL1
- https://school.programmers.co.kr/learn/courses/30/lessons/59404
```SQL
SELECT ANIMAL_ID, NAME, DATETIME
FROM ANIMAL_INS
ORDER BY NAME, DATETIME DESC;
```

## 문제: 동물의 아이디와 이름
- LEVEL1
- https://school.programmers.co.kr/learn/courses/30/lessons/59403
```SQL
SELECT ANIMAL_ID, NAME
FROM ANIMAL_INS
ORDER BY ANIMAL_ID;
```

## 문제: 역순 정렬하기
- LEVEL1
- https://school.programmers.co.kr/learn/courses/30/lessons/59035
```SQL
SELECT NAME, DATETIME
FROM ANIMAL_INS
ORDER BY ANIMAL_ID DESC;
```

## 문제: 모든 레코드 조회하기 
- LEVEL1
- https://school.programmers.co.kr/learn/courses/30/lessons/59034
```SQL
SELECT *
FROM ANIMAL_INS
ORDER BY ANIMAL_ID;
```

## 문제: 가격이 제일 비싼 식품의 정보 출력하기
- LEVEL2
- https://school.programmers.co.kr/learn/courses/30/lessons/131115
```SQL
SELECT 
    PRODUCT_ID,
    PRODUCT_NAME,
    PRODUCT_CD,
    CATEGORY,
    PRICE
FROM FOOD_PRODUCT
ORDER BY PRICE DESC
LIMIT 1;
```

## 문제: 이름에 el이 들어가는 동물 찾기
- LEVEL2
- https://school.programmers.co.kr/learn/courses/30/lessons/59047
```SQL
SELECT ANIMAL_ID, NAME
FROM ANIMAL_INS
WHERE NAME LIKE '%el%' AND ANIMAL_TYPE = 'Dog'
ORDER BY NAME;
```

## 문제: 고양이와 개는 몇 마리 있을까?
- LEVEL2
- https://school.programmers.co.kr/learn/courses/30/lessons/59040
```SQL
SELECT ANIMAL_TYPE, COUNT(ANIMAL_ID) AS count
FROM ANIMAL_INS
GROUP BY ANIMAL_TYPE
ORDER BY ANIMAL_TYPE;
```

## 문제: 카테고리 별 상품 개수 구하기
- LEVEL2
- https://school.programmers.co.kr/learn/courses/30/lessons/131529
```SQL
SELECT 
    substr(PRODUCT_CODE, 1, 2) AS CATEGORY,
    COUNT(PRODUCT_ID)
FROM PRODUCT
GROUP BY substr(PRODUCT_CODE, 1, 2);
-- GROUP BY 에 SUBSTR사용가능합니다.
```

## 문제: 가격대 별 상품 개수 구하기
- LEVEL2
- https://school.programmers.co.kr/learn/courses/30/lessons/131530
```SQL
SELECT
    TRUNCATE(PRICE, -4) AS PRICE_GROUP,
    COUNT(PRODUCT_ID) AS PRODUCTS
FROM PRODUCT
GROUP BY TRUNCATE(PRICE, -4)
ORDER BY PRICE_GROUP;
```

## 문제: 동명 동물 수 찾기
- LEVEL2
- https://school.programmers.co.kr/learn/courses/30/lessons/59041
```SQL
SELECT
    NAME,
    COUNT(ANIMAL_ID)
FROM ANIMAL_INS
WHERE NAME IS NOT NULL 
GROUP BY NAME
HAVING COUNT(ANIMAL_ID) >= 2
ORDER BY NAME
```

## 문제: 재구매가 일어난 상품과 회원 리스트 구하기
- LEVEL2
- https://school.programmers.co.kr/learn/courses/30/lessons/131536
```SQL
SELECT USER_ID, PRODUCT_ID
FROM ONLINE_SALE 
GROUP BY USER_ID, PRODUCT_ID
HAVING COUNT(USER_ID)>=2
ORDER BY USER_ID, PRODUCT_ID DESC;
```
---
# 문제 6


## 문제: 
- LEVEL
- 
```SQL

```

## 문제: 
- LEVEL
- 
```SQL

```

## 문제: 
- LEVEL
- 
```SQL

```

## 문제: 
- LEVEL
- 
```SQL

```

## 문제: 
- LEVEL
- 
```SQL

```