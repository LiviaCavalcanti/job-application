"""
You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.

Merge all the linked-lists into one sorted linked-list and return it.
"""
import heapq


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def merge_k_lists(lists: list[ListNode]) -> ListNode:
    heap = []

    for number_lists in range(len(lists)):
        if lists[number_lists]:  # Check if the list is not empty
            heapq.heappush(heap, (lists[number_lists].pop(0), number_lists, 0))

    
    result = []
    while heap:
        value, list_index, index = heapq.heappop(heap)
        result.append(value)
        if lists[list_index]:  # Check if the list is not empty after popping
            heapq.heappush(heap, (lists[list_index].pop(0), list_index, 0))

        print(result)    

    return result

lists = [[1,4,5],[1,3,4],[2,6]]
print(merge_k_lists(lists) == [1,1,2,3,4,4,5,6])