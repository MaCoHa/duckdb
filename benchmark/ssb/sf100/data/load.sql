CREATE TABLE customer
(
    C_CUSTKEY       INTEGER,
    C_NAME          VARCHAR,
    C_ADDRESS       VARCHAR,
    C_CITY          VARCHAR,
    C_NATION        VARCHAR,
    C_REGION        VARCHAR,
    C_PHONE         VARCHAR,
    C_MKTSEGMENT    VARCHAR
);

CREATE TABLE lineorder
(
    LO_ORDERKEY             INTEGER,
    LO_LINENUMBER           INTEGER,
    LO_CUSTKEY              INTEGER,
    LO_PARTKEY              INTEGER,
    LO_SUPPKEY              INTEGER,
    LO_ORDERDATE            DATE,
    LO_ORDERPRIORITY        VARCHAR,
    LO_SHIPPRIORITY         INTEGER,
    LO_QUANTITY             INTEGER,
    LO_EXTENDEDPRICE        INTEGER,
    LO_ORDTOTALPRICE        INTEGER,
    LO_DISCOUNT             INTEGER,
    LO_REVENUE              INTEGER,
    LO_SUPPLYCOST           INTEGER,
    LO_TAX                  INTEGER,
    LO_COMMITDATE           DATE,
    LO_SHIPMODE             VARCHAR
);

CREATE TABLE part
(
    P_PARTKEY       INTEGER,
    P_NAME          VARCHAR,
    P_MFGR          VARCHAR,
    P_CATEGORY      VARCHAR,
    P_BRAND         VARCHAR,
    P_COLOR         VARCHAR,
    P_TYPE          VARCHAR,
    P_SIZE          INTEGER,
    P_CONTAINER     VARCHAR
);

CREATE TABLE supplier
(
    S_SUPPKEY       INTEGER,
    S_NAME          VARCHAR,
    S_ADDRESS       VARCHAR,
    S_CITY          VARCHAR,
    S_NATION        VARCHAR,
    S_REGION        VARCHAR,
    S_PHONE         VARCHAR
);

CREATE TABLE date
(
    D_DATEKEY            DATE,
    D_DATE               VARCHAR(18),
    D_DAYOFWEEK          VARCHAR,
    D_MONTH              VARCHAR,
    D_YEAR               INTEGER,
    D_YEARMONTHNUM       INTEGER,
    D_YEARMONTH          VARCHAR(7),
    D_DAYNUMINWEEK       INTEGER,
    D_DAYNUMINMONTH      INTEGER,
    D_DAYNUMINYEAR       INTEGER,
    D_MONTHNUMINYEAR     INTEGER,
    D_WEEKNUMINYEAR      INTEGER,
    D_SELLINGSEASON      VARCHAR,
    D_LASTDAYINWEEKFL    INTEGER,
    D_LASTDAYINMONTHFL   INTEGER,
    D_HOLIDAYFL          INTEGER,
    D_WEEKDAYFL          INTEGER
);

-- sf 1
COPY part FROM 'benchmark/ssb/sf100/data/part.tbl' (DELIMITER ',');
COPY supplier FROM 'benchmark/ssb/sf100/data/supplier.tbl' (DELIMITER ',');
COPY customer FROM 'benchmark/ssb/sf100/data/customer.tbl' (DELIMITER ',');
COPY date FROM 'benchmark/ssb/sf100/data/date.tbl' (DELIMITER ',');
COPY lineorder FROM 'benchmark/ssb/sf100/data/lineorder.tbl' (DELIMITER ',');


