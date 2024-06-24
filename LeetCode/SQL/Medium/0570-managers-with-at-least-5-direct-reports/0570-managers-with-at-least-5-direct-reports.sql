# Write your MySQL query statement below
-- WITH report AS
-- (SELECT managerId, COUNT(*) AS report_cnt
-- FROM Employee
-- GROUP BY managerId
-- HAVING report_cnt >= 5)
-- SELECT Employee.name
-- FROM report
-- INNER JOIN Employee
-- ON report.managerId = Employee.id

SELECT name
FROM Employee
WHERE id IN
(SELECT managerId
FROM Employee
GROUP BY managerId
HAVING COUNT(*) >= 5);
