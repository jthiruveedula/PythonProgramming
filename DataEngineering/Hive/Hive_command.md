# Hive commands

- set hive.metastore.warehouse.dir

This will shows the metastore location where tables are being stored

- Creating tables in Hive

```
create table if not exists table_test(col1 string,col2 string) 
row format delimited fields terminated by ',' 
lines terminated by '\n' stored as textfile location '/home/jagadeesh/data.txt';
```


- Loading file data into table

```
load data local inpath'/home/jagadeesh/data.txt' into table test_table;

load data local inpath'/home/jagadeesh/data.txt' into table test_table partition(data='txt');
```
- Insert / Insert overwrite 

Hive supports append insertion and overwrite of tables.

```
insert into table table_test1 select * from test_table;

insert overwrite table table_test1 select * from test_table;
```
- Multi Insert in Hive

Hive supports insertion of data into multiple tables at a time.
```
from emp_tab insert into table table_test select col1,col2 insert into table table_test1 select col1,col2;
```



## Commands:

- desc table;
- desc database;
- desc formatted table;


## Functions

- from_unixtimstamp
- split(),substr(),instr()
- rlike
- sort by,order by,distribute by,cluster by
- rank(),dense_rank(), row_number(), over(order by || partition by)

## Partitioning 
- Static partitioning(Manual loading of data)
- Dynamic partitioning(Hive will create partitions based on partition column)

Enabling dynamic partitioning in hive.
```
 set hive.exec.dynamic.partition=true;
 set hive.exec.dynamic.partition.mode=nonstrict;
 ```
 - Deleting partitioning and Refreshing table
 ```
 show partitions table_test;
 alter table table_test add partition(data='txt');
 alter table table_test drop partition(data='txt');
 msck repair table table_test;
 ```

 ## Bucketing

 Enabling bucketing in hive and creating table with buckets.

 imp:- Reducer tasks == Buckets provided in table.

 Bucketed Map joins are faster joins and we should join both tables on bucketed columns.

 ```
 set hive.enforce.bucketing=true;
 set hive.exec.dynamic.partition.mode=nonstrict;
 create table if not exists bucket_tab (deptno int,deptname string,empname string,location string)
 partitioned by (deptname string) clustered by(location) into 4 buckets 
 row format delimited fields terminated by ',' lines terminated by '\n' stored as textfile;
 ```
 ## Table Sampling
Sampling on buckted columns for faster retrival and avoiding full table scan.
 ```
 select deptno,deptname,location from bucket_tab tablesample (bucket 1 out out of 2 on location);
 
 select deptno,deptname,location from bucket_tab tablesample (2 percent);

 select deptno,deptname,location from bucket_tab tablesample (1M);

 select deptno,deptname,location from bucket_tab tablesample (20 rows);
 ```

## Protecting tables(no_drop, offline)

```
alter table bucketed_tab enable no_drop;

alter table bucketed_tab disable no_drop;

alter table bucketed_tab drop partition(deptname='HR') enable no_drop;

alter table bucketed_tabl enable offline;

alter table bucketed_tab drop partition(deptname='HR') enable offline;

```