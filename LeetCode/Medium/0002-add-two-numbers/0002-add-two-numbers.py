# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        answer_lst = ListNode() #정답을 답은 링크드 리스트
        curr_answer = answer_lst 
        
        curr_l1 = l1 
        curr_l2 = l2
        
        while True:
        	# 첫번째 리스트도 비고 두번째 리스트도 비었으면 더이상 할 게 없으므로 그만
            if not curr_l1 and not curr_l2:
                break
            
            # 이 전 노드에서 합이 10이 넘어가면 뒤로 1을 넘겨주는데
            # 그 넘겨받은 1이 있으면 고려해주기 위해
            _sum = curr_answer.val
            
            # 첫번 째 리스트가 비지않았으면
            if curr_l1:
            	# 값을 더해줌
                _sum += curr_l1.val
                
                # 다음 노드 가리키게
                curr_l1 = curr_l1.next
            
            # 두번 째 리스트가 비지않았으면
            if curr_l2:
            	# 값을 더해줌
                _sum += curr_l2.val
                # 다음 노드 가리키게 
                curr_l2 = curr_l2.next
            
            
            # 더한 값을 10으로 나눈 나머지 == 현재 정답 노드의 값이 됨
            remainder = _sum % 10
            
            # 더한 값을 10으로 나눈 몫 (승수, 뒤로 넘겨줄 수)
            share = _sum // 10
            
            # 현재 정답 노드의 값을 
            curr_answer.val = remainder
            
            # 이 조건을 걸지 않으면 7->0->8->0 이렇게 뒤에 쓸 데 없이 0이 생김
            # 어떤 리스트에도 다음으로 탐색해야할 노드가 없으면 추가할 필요가 없음
            # 즉 위의 예에서 두 리스트에 3번 째 노드들(3,4)을 더할 때는 다음 노드가 없으니까
            # 정답 노드에 뒤에 노드를 더 추가할 필요가 없음
            # 단, 이런 경우라도 승수가 있을 경우에는 넘겨줘야 하기 때문에 share 조건 추가
            if share or curr_l1 or curr_l2:
                curr_answer.next = ListNode(share)  
                curr_answer = curr_answer.next
       
        print(answer_lst)
        
        return answer_lst