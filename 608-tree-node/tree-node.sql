# Write your MySQL query statement below
SELECT id,
CASE WHEN  p_id is null then "Root"
WHEN id in (select p_id from tree) then 'Inner'
ELSE 'Leaf' END
as "type"
FROM Tree;