-- Q4.3

SELECT
    D_YEAR,
    S_CITY,
    P_BRAND,
    sum(LO_REVENUE - LO_SUPPLYCOST) AS profit
FROM
    date
JOIN
    lineorder ON LO_ORDERDATE = D_DATEKEY
JOIN
    customer ON LO_CUSTKEY = C_CUSTKEY
JOIN
    supplier ON LO_SUPPKEY = S_SUPPKEY
JOIN
    part ON LO_PARTKEY = P_PARTKEY
WHERE
    C_REGION = 'AMERICA'
    AND S_NATION = 'UNITED STATES'
    AND D_YEAR IN (1997, 1998)
    AND P_CATEGORY = 'MFGR#14'
GROUP BY
    D_YEAR,
    S_CITY,
    P_BRAND
ORDER BY
    D_YEAR,
    S_CITY,
    P_BRAND;