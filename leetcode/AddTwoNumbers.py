# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    
        
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:

        def addList(l1, l2, overflow) :    
            if l1 == None and l2 == None and not overflow:
                return None
            l1Value = 0
            l2Value = 0
            
            if l1 != None : 
                l1Value = l1.val
                l1 = l1.next
                
            if l2 != None : 
                l2Value = l2.val
                l2 = l2.next
                
            if overflow :
                overflow = False
                l1Value += 1
                
            nlist = ListNode()
                
            nlist.val = l1Value + l2Value
            if nlist.val > 9 :
                nlist.val = nlist.val - 10
                overflow = True
                
            nlist.next = addList(l1, l2, overflow)
            
            return nlist
        
        return addList(l1, l2, False)