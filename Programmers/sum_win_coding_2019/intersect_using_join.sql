SELECT A.CART_ID
FROM CART_PRODUCTS AS A
INNER JOIN  CART_PRODUCTS AS B
ON A.CART_ID = B.CART_ID
WHERE A.NAME='Milk' 
AND B.NAME='Yogurt'

/*
우유와 요거트가 담긴 장바구니
하나의 테이블에서 2개의 결과를 가지고 교집합을 구한다.
하지만 intersect 연산자는 쓸 수 없다.
*/