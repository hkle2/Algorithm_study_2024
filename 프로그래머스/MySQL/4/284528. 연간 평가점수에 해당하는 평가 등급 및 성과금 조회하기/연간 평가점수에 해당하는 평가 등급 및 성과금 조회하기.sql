-- 코드를 작성해주세요
WITH AVG_SCORE AS (
SELECT A.EMP_NO, A.EMP_NAME, AVG(B.SCORE) AS SCORE, A.SAL
FROM HR_EMPLOYEES AS A INNER JOIN HR_GRADE AS B
ON A.EMP_NO = B.EMP_NO
GROUP BY A.EMP_NO)
SELECT EMP_NO, EMP_NAME,
    CASE
        WHEN SCORE >= 96 THEN 'S'
        WHEN SCORE >= 90 THEN 'A'
        WHEN SCORE >= 80 THEN 'B'
        ELSE 'C'
    END AS GRADE,
    CASE
        WHEN SCORE >= 96 THEN SAL * .2
        WHEN SCORE >= 90 THEN SAL * 0.15
        WHEN SCORE >= 80 THEN SAL * 0.1
        ELSE 0
    END AS BONUS
FROM AVG_SCORE
ORDER BY EMP_NO;
