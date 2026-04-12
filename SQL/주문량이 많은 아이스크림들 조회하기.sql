/*
문제 설명
다음은 아이스크림 가게의 상반기 주문 정보를 담은 FIRST_HALF 테이블과 7월의 아이스크림 주문 정보를 담은 JULY 테이블입니다. FIRST_HALF 테이블 구조는 다음과 같으며, SHIPMENT_ID, FLAVOR, TOTAL_ORDER는 각각 아이스크림 공장에서 아이스크림 가게까지의 출하 번호, 아이스크림 맛, 상반기 아이스크림 총주문량을 나타냅니다. FIRST_HALF 테이블의 기본 키는 FLAVOR입니다. FIRST_HALF테이블의 SHIPMENT_ID는 JULY테이블의 SHIPMENT_ID의 외래 키입니다.

NAME	TYPE	NULLABLE
SHIPMENT_ID	INT(N)	FALSE
FLAVOR	VARCHAR(N)	FALSE
TOTAL_ORDER	INT(N)	FALSE
JULY 테이블 구조는 다음과 같으며, SHIPMENT_ID, FLAVOR, TOTAL_ORDER 은 각각 아이스크림 공장에서 아이스크림 가게까지의 출하 번호, 아이스크림 맛, 7월 아이스크림 총주문량을 나타냅니다. JULY 테이블의 기본 키는 SHIPMENT_ID입니다. JULY테이블의 FLAVOR는 FIRST_HALF 테이블의 FLAVOR의 외래 키입니다. 7월에는 아이스크림 주문량이 많아 같은 아이스크림에 대하여 서로 다른 두 공장에서 아이스크림 가게로 출하를 진행하는 경우가 있습니다. 이 경우 같은 맛의 아이스크림이라도 다른 출하 번호를 갖게 됩니다.

NAME	TYPE	NULLABLE
SHIPMENT_ID	INT(N)	FALSE
FLAVOR	VARCHAR(N)	FALSE
TOTAL_ORDER	INT(N)	FALSE
문제
7월 아이스크림 총 주문량과 상반기의 아이스크림 총 주문량을 더한 값이 큰 순서대로 상위 3개의 맛을 조회하는 SQL 문을 작성해주세요.

*/

WITH GROUP_FIRST_HALF as (
    SELECT FLAVOR, SUM(TOTAL_ORDER) as sum_order
        FROM FIRST_HALF
    GROUP BY FLAVOR
    ),
GROUP_JULY as (
    SELECT FLAVOR, SUM(TOTAL_ORDER) as sum_order 
        FROM JULY 
    GROUP BY FLAVOR
)
SELECT A.FLAVOR
FROM GROUP_FIRST_HALF as a 
JOIN GROUP_JULY as b 
ON a.FLAVOR = b.FLAVOR 
ORDER BY (A.sum_order + B.sum_order) desc 
LIMIT 3;


