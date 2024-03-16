# Write your MySQL query statement below
#CTE to count ratinsg of all movies

WITh count_ratings AS
(
    SELECT user_id, COUNT(movie_id) as rated_movies
    FROM MovieRating 
    GROUP BY User_id
)

, avg_movie_ratings AS(
    SELECT movie_id, AVG(rating) AS avg_rating
    FROM MovieRating 
    WHERE created_at BETWEEN '2020-02-01' AND '2020-02-29'
GROUP BY movie_id
)

(SELECT u.name AS results
FROM count_ratings cr
INNER JOIN Users u
ON cr.user_id = u.user_id
ORDER BY rated_movies DESC , name ASC
LIMIT 1 )

UNION ALL

#movie name with the highest average rating, ordered by lexicographically smaller movie name.
(SELECT m.title AS results
FROM avg_movie_ratings AS amr
INNER JOIN Movies m
ON amr.movie_id = m.movie_id
ORDER BY avg_rating DESC, title ASC
LIMIT 1);
