/* Write your T-SQL query statement below */
SELECT M.reports_to AS employee_id,E.name
,COUNT(M.employee_id) reports_count, ROUND(SUM(age)*1.00/COUNT(M.employee_id)*1.00,0) average_age 
FROM Employees M 
LEFT JOIN (SELECT DISTINCT employee_id,name FROm Employees) E 
ON M.reports_to=E.employee_id
WHERE M.reports_to IS NOT NULL
GROUP BY M.reports_to,E.name
ORDER BY M.reports_to