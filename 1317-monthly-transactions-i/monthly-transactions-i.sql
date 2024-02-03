/* Write your T-SQL query statement below */
SELECT LEFT(t.trans_date, '7') month, 
t.country country,
count(*) as trans_count,
SUM(CASE WHEN t.state = 'approved' THEN 1 ELSE 0 END) as approved_count,
(SUM(amount)) as trans_total_amount,
SUM(CASE WHEN t.state = 'approved' THEN t.amount ELSE 0 END) as approved_total_amount

FROM Transactions as t
GROUP BY LEFT(t.trans_date, '7') ,country
