/* Write your T-SQL query statement below */
SELECT SUBSTRING(format(trans_date,'yyyy-MM-dd hh:mm:ss tt'),1,7)  as month, 
t.country country,
count(*) as trans_count,
SUM(CASE WHEN t.state = 'approved' THEN 1 ELSE 0 END) as approved_count,
(SUM(amount)) as trans_total_amount,
SUM(CASE WHEN t.state = 'approved' THEN t.amount ELSE 0 END) as approved_total_amount

FROM Transactions as t
GROUP BY SUBSTRING(format(trans_date,'yyyy-MM-dd hh:mm:ss tt'),1,7) ,country
