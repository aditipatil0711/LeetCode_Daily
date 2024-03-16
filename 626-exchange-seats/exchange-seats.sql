# Write your MySQL query statement below
SELECT
(CASE
    WHEN MOD(id,2) != 0 and counts !=id THEN id+1
    WHEN MOD(id, 2) != 0 AND counts = id THEN id
        ELSE id - 1
    END) AS id
 , student
FROM Seat, (SELECT COUNT(*) as counts from seat) as seat_counts
ORDER BY id ASC