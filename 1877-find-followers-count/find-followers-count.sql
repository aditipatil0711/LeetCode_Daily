/* Write your T-SQL query statement below */
select user_id, COUNT(DISTINCT follower_id) as followers_count
FROM Followers 
GROUP BY user_id
ORDER By user_id