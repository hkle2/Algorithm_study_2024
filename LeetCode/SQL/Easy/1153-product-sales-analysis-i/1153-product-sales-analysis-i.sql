# Write your MySQL query statement below
SELECT product_name, year, price
FROM Sales AS A INNER JOIN Product AS B ON A.product_id = B.product_id;
