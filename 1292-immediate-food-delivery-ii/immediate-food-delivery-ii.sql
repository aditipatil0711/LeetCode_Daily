/* Write your T-SQL query statement below */


WITH First_Order AS (
SELECT customer_id, preference
FROM (
select 
customer_id
,order_date
,customer_pref_delivery_date
,row_number() over (partition by customer_id order by order_date) as rn 
, case when order_date = customer_pref_delivery_date then 'immediate' else 'scheduled' end as preference
from delivery 
) as SubQ 
where SubQ.rn = 1
)

SELECT 
ROUND(SUM(CASE WHEN preference = 'immediate' then 1 else 0 end + 0.00 )*100 / COUNT(*), 2) as immediate_percentage

from first_order
