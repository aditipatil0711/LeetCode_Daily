/* Write your T-SQL query statement below */
Delete p1 from PErson p1 , Person p2 
WHERE p1.Email = p2.email AND p1.id>p2.id
