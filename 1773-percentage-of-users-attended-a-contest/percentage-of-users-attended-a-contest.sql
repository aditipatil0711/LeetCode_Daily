# Write your MySQL query statement below
SELECT
    Register.contest_id,
    ROUND((COUNT(Register.user_id) / (SELECT COUNT(DISTINCT user_id) FROM Users)) * 100, 2) as percentage #dont have to join just because there are two tables. For this type of question, use one table
FROM
    Register    
GROUP BY
    Register.contest_id
ORDER BY
    percentage DESC,
    Register.contest_id ASC