# Write your MySQL query statement below
SELECT user_id, MAX(time_stamp) AS last_stamp
FROM Logins
WHERE time_stamp LIKE '2020-%'
GROUP BY user_id;

-- SELECT user_id, MAX(time_stamp) AS last_stamp
-- FROM Logins
-- WHERE EXTRACT(YEAR FROM time_stamp) = 2020
-- GROUP BY user_id;