def isPalindrome(self, head: Optional[ListNode]) -> bool:
        slow = fast = head 
        rev = None
        while fast and fast.next :
            fast = fast.next.next # fast는 2칸 씩 
            slow ,rev, rev.next = slow.next, slow , rev # rev는 역으로 저장, slow는 한칸 씩 
        if fast : slow = slow.next # 노드의 개수가 홀수일경우 
        
        while rev and rev.val == slow.val : 
            rev, slow = rev.next, slow.next
        return not rev 
