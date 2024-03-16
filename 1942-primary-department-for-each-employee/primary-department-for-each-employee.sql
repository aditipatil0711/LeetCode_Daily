# Write your MySQL query statement below
SELECT employee_id,department_id 

FROM(
SELECT 
      *, 
      COUNT(employee_id) OVER(PARTITION BY employee_id) AS EmployeeCount
    FROM 
      Employee) e
WHERE 
primary_flag = 'Y' OR EmployeeCount = 1
