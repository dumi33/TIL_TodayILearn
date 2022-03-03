def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if (not list1) or (list2 and list1.val > list2.val) : # l1의 첫번째 노드를 최솟값으로 만들기 # not list1이 있는 이유는 l1이 비었을 경우 l2를 최솟값으로 만들기 위해서 
            list1, list2 = list2, list1
        if list1 : # l1의 첫번째 원소는 이미 최솟값이므로 그 다음값부터 다시 최소값을 만들어 붙인다. 
            list1.next = self.mergeTwoLists(list1.next,list2 )
            
        return list1
