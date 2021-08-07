#https://leetcode.com/explore/challenge/card/july-leetcoding-challenge-2021/610/week-3-july-15th-july-21st/3818/
# Definition for singly-linked list.
from typing import List
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if k == 1:
            return head
        Stack = []
        newHead = None
        current = None
        while head != None:
            i = k
            prev = head
            while head != None and i>0:
                i-=1
                Stack.append(head.val)
                head = head.next
            if i != 0:
                if newHead == None:
                    return head
                while prev:
                    current.next = prev.val
                    prev = prev.next
                    current = current.next
                
        
        return newHead
            

        


        
        
if __name__ == '__main__':
    Head = ListNode(1)
    Head.next = ListNode(2)
    Head.next.next = ListNode(3)
    Head.next.next.next = ListNode(4)
    Head.next.next.next.next = ListNode(5)
    Head.next.next.next.next.next = ListNode(6)
    Solution().reverseKGroup(Head,3)
