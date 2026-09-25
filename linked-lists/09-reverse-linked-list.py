# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        prev = None
        curr = head
        
        while curr:
            next_temp = curr.next
            curr.next = prev
            prev = curr
            curr = next_temp
            
        return prev

# Local Test Cases
def print_list(head):
    vals = []
    while head:
        vals.append(head.val)
        head = head.next
    print(vals)

solution = Solution()

# Test 1: Typical [1,2,3,4,5] -> [5,4,3,2,1]
head1 = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
print("Test 1 (Typical): ", end="")
print_list(solution.reverseList(head1)) 

# Test 2: Edge (Empty list) [] -> []
print("Test 2 (Edge - Empty): ", end="")
print_list(solution.reverseList(None))