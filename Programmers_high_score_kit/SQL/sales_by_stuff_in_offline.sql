-- 코드를 입력하세요
# SELECT P.PRODUCT_CODE, (O.SALES_AMOUNT * P.PRICE) AS SALES
# FROM PRODUCT AS P, OFFLINE_SALE AS O
# WHERE P.PRODUCT_ID = O.PRODUCT_ID
# GROUP BY P.PRODUCT_CODE
# ORDER BY SALES DESC, P.PRODUCT_CODE ASC

SELECT P.PRODUCT_CODE, SUM(O.SALES_AMOUNT * P.PRICE) AS SALES
FROM PRODUCT AS P, OFFLINE_SALE AS O
WHERE P.PRODUCT_ID = O.PRODUCT_ID
GROUP BY P.PRODUCT_CODE
ORDER BY SALES DESC, P.PRODUCT_CODE ASC

# SELECT *
# FROM PRODUCT AS P, OFFLINE_SALE AS O
# # GROUP BY P.PRODUCT_CODE
# ORDER BY P.PRODUCT_CODE ASC
