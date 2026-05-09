"""
You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.

Merge all the linked-lists into one sorted linked-list and return it.
"""
import heapq

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def merge_k_lists(lists):
    heap = []

    for i in range(len(lists)):
        if lists[i]:  # Check if the linked list is not empty
            heapq.heappush(heap, (lists[i].val, i, lists[i]))

    dummy = ListNode()
    current = dummy

    while heap:
        value, list_index, node = heapq.heappop(heap)
        current.next = ListNode(value)
        current = current.next
        if node.next:  # Check if there's a next node in the linked list
            heapq.heappush(heap, (node.next.val, list_index, node.next))

    return dummy.next


# Helper: convert a Python list to a linked list
def to_linked_list(arr):
    dummy = ListNode()
    current = dummy
    for val in arr:
        current.next = ListNode(val)
        current = current.next
    return dummy.next

# Helper: convert a linked list to a Python list
def to_list(node):
    result = []
    while node:
        result.append(node.val)
        node = node.next
    return result

lists = [to_linked_list([1,4,5]), to_linked_list([1,3,4]), to_linked_list([2,6])]
print(to_list(merge_k_lists(lists)) == [1,1,2,3,4,4,5,6])