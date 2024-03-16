SELECT s.product_id, s.year AS first_year, s.quantity, s.price
FROM Sales s
INNER JOIN (
    SELECT product_id, MIN(year) AS min_year
    FROM Sales
    GROUP BY product_id
) as sub
ON s.product_id = sub.product_id AND s.year = sub.min_year;
