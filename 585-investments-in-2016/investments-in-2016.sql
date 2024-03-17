# Write your MySQL query statement below
With T1 as(
    Select tiv_2015 from Insurance
    Group by tiv_2015
    having count(tiv_2015)>1
),
T2 as (
    Select lat from insurance
    group by lat,lon
    having count(*)<2
)

Select round(sum(tiv_2016),2) as tiv_2016 from Insurance 
where tiv_2015 in (
    Select * from T1
)
and lat in (
    Select * from t2
)