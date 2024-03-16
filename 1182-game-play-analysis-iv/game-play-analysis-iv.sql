/* Write your T-SQL query statement below 

*/

WITH CTE AS
(
    SELECT player_id,datediff(day,min(event_date) OVER(PARTITION BY player_id), event_date)
    AS daydiff from activity

)

SELECT round(COUNT(CASE WHEN daydiff = 1 THEN player_id END) * 1.0 / COUNT(distinct player_id) ,2) as fraction
FROM cte;
