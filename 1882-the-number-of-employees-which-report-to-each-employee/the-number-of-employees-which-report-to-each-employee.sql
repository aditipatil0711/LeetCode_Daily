# Write your MySQL query statement below
SELECT 
  e.reports_to AS employee_id, 
  e1.name,
  COUNT(e.reports_to) AS reports_count, 
  ROUND(AVG(e.age)) AS average_age 
FROM 
  employees e 
JOIN 
  employees e1 
ON 
  e.reports_to = e1.employee_id
GROUP BY 
  e.reports_to, 
  e1.name
HAVING 
  COUNT(e.reports_to) > 0 
ORDER BY 
  employee_id;
