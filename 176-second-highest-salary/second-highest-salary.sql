
SELECT MAX(SALARY) as 'SecondHighestSalary'
 FROM Employee 
 WHERE SALARY < (SELECT MAX(SALARY) FROM Employee);