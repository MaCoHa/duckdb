-- Q1.2

SELECT
    sum(LO_EXTENDEDPRICE * LO_DISCOUNT) AS REVENUE
FROM
    lineorder
JOIN
    date ON LO_ORDERDATE = D_DATEKEY
WHERE
    D_YEARMONTHNUM = 199401
    AND LO_DISCOUNT BETWEEN 4 AND 6
    AND LO_QUANTITY BETWEEN 26 AND 35;