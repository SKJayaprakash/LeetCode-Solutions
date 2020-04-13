# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        
        result = ListNode()
        carry = 0
        resultHead = result
        # print(result)
        
        while l1 != None or l2 != None :
            
            s = carry
            if l1 != None :
                s += l1.val
                l1 = l1.next
            if l2 != None :
                s += l2.val
                l2 = l2.next
            
            print( carry + (s % 10 ) )
            result.next = ListNode( s % 10 )
            result = result.next
            carry = s//10
            
            
        if carry != 0 :
            result.next = ListNode( carry )
            
        return resultHead.next
