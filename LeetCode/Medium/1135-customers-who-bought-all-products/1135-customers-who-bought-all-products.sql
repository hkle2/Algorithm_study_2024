# Write your MySQL query statement below
-- SELECT A.customer_id, A.product_key
-- FROM Customer AS A INNER JOIN Product AS B ON A.product_key = B.product_key
-- GROUP BY customer_id, product_key

SELECT customer_id
FROM Customer
GROUP BY customer_id
HAVING COUNT(DISTINCT product_key) = (SELECT COUNT(DISTINCT product_key) FROM Product);