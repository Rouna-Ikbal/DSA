# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
def mergeTwoLists( list1: [ListNode], list2: [ListNode]) -> [ListNode]:
    #create a list
    #current pointer to traverse this list and add elements
    head = ListNode()
    current = head  # original list will start from head.next 
    while list1 and list2:
        if list1.val < list2.val:
            current.next = list1
            list1 = list1.next
        else:
            current.next = list2
            list2 = list2.next
        current = current.next  #go to next node
    
    current.next = list1 or list2  #append the remaining list, either list1 or list2
    return head.next
    
print(mergeTwoLists([1,2,4], [1,3,4]))