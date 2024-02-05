/* Write your T-SQL query statement below */
with first_order as (
    select 
        customer_id,
        order_date,
        customer_pref_delivery_date,
        rnk 
    from (select 
        customer_id,
        order_date,
        customer_pref_delivery_date,
        rank() over (partition by customer_id order by order_date) as rnk 
    from Delivery) a
    where rnk = 1
)
select 
round(
    sum(
        case
	    when order_date = customer_pref_delivery_date then 1
	    else 0
    end)*100.0/count(customer_id)
,2) as immediate_percentage
from first_order