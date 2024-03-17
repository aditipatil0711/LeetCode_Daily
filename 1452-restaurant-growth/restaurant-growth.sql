
# Write your MySQL query statement below
with t1 as (select visited_on ,sum(amount) as amount, ROW_NUMBER() over(order by visited_on) as rn from Customer group by visited_on),

t2 as (select rn, visited_on, sum(amount) over(order by visited_on ROWS 6 PRECEDING) as amount, round(avg(amount) over(order by visited_on ROWS 6 PRECEDING),2) as average_amount from t1)

select visited_on, amount, average_amount from t2 where rn > 6