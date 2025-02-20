class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not k:
            return head
        
        curr = head
        length = 0

        while curr:
            length+=1
            curr = curr.next
        
        k = k % length

        if k == 0:
            return head

        curr = head

        for _ in range(1,length - k):
            curr = curr.next

        temp = curr.next
        curr.next = None
        temp_head = temp

        while temp.next:
            temp = temp.next

        temp.next = head
        return temp_head