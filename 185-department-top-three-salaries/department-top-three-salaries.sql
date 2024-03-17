# Write your MySQL query statement below
with depart_rank as (select salary, departmentID,
DENSE_RANK() OVER(Partition by departmentID ORDER BY salary desc) as de_rank
from Employee)

select D.name as Department, E.name as Employee, E.salary
from Employee E
INNER JOIN Department D 
ON E.departmentID = D.id
where (E.departmentID, E.salary) 
IN(
select distinct departmentID, salary
from depart_rank
where de_rank < 4)