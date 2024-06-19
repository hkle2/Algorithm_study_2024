# Write your MySQL query statement below
# GROUP BY와 SUM을 이용해보세요
-- SELECT
--     event_day AS day,
--     emp_id,
--     SUM(out_time - in_time) AS total_time
-- FROM
--     Employees
-- GROUP BY 
--     event_day,
--     emp_id

SELECT event_day AS day, emp_id, SUM(out_time - in_time) AS total_time
FROM Employees
GROUP BY event_day, emp_id