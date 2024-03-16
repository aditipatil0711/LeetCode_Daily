# Write your MySQL query statement below
SELECT employee_id
FROM Employees e
WHERE salary<30000 
and manager_id NOT IN (SELECT employee_id
FROM Employees e)
ORDER BY employee_id
