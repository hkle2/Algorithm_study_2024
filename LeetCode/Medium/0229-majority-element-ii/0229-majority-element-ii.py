class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        from collections import Counter
        answer = []
        # 1. n / 3을 내림한 숫자 m 구하기
        # 2. nums 리스트의 각 숫자들의 등장 횟수를 집계한 딕셔너리 만들기
        # 3. 딕셔너리를 순회하면서 m보다 많이 등장한 숫자를 answer에 추가하기
        n = len(nums)
        m = math.floor(n / 3)
        nums_counter = Counter(nums)
        for num, cnt in nums_counter.items():
            # cnt가 m보다 크면 answer에 num을 append
            if cnt > m:
                answer.append(num)
        # nums_dict = {}
        # for num in nums:
        #     if num not in nums_dict:
        #         nums_dict[num] = 0
        #     nums_dict[num] += 1
        # for key in nums_dict.keys():
        #     if nums_dict[key] > m:
        #         answer.append(key)

        # for i in nums:
        #     if nums.count(i) > len(nums) / 3:
        #         answer.append(i)
        # answer = set(answer)
        return answer
        
        