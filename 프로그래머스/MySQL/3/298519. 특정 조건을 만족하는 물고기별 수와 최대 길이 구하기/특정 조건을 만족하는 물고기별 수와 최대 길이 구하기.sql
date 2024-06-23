-- 코드를 작성해주세요
WITH LENGTH AS
(SELECT FISH_TYPE, AVG(IFNULL(LENGTH, 10)) AS AVG_LENGTH
FROM FISH_INFO
GROUP BY FISH_TYPE
HAVING AVG_LENGTH >= 33)
SELECT COUNT(A.FISH_TYPE) AS FISH_COUNT, MAX(A.LENGTH) AS MAX_LENGTH, A.FISH_TYPE
FROM FISH_INFO AS A INNER JOIN LENGTH AS B ON A.FISH_TYPE = B.FISH_TYPE
GROUP BY A.FISH_TYPE
ORDER BY A.FISH_TYPE;