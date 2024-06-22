-- 코드를 작성해주세요
SELECT A.ITEM_ID, A.ITEM_NAME, A.RARITY
FROM ITEM_INFO AS A INNER JOIN ITEM_TREE AS B ON A.ITEM_ID = B.ITEM_ID INNER JOIN ITEM_INFO AS C ON C.ITEM_ID = B.PARENT_ITEM_ID
WHERE C.RARITY = 'RARE'
ORDER BY A.ITEM_ID DESC;

# SELECT A.ITEM_ID, A.ITEM_NAME, A.RARITY
# FROM ITEM_INFO AS A INNER JOIN ITEM_TREE AS B ON A.ITEM_ID = B.ITEM_ID
# WHERE PARENT_ITEM_ID IN (SELECT ITEM_ID
# FROM ITEM_INFO
# WHERE RARITY = 'RARE')
# ORDER BY A.ITEM_ID DESC;