-- 코드를 작성해주세요
WITH CHILD_COUNT AS
(SELECT PARENT_ID, COUNT(*) AS CHILD
FROM ECOLI_DATA
GROUP BY PARENT_ID)
SELECT A.ID, IFNULL(B.CHILD, 0) AS CHILD_COUNT
FROM ECOLI_DATA AS A LEFT JOIN CHILD_COUNT AS B ON A.ID = B.PARENT_ID