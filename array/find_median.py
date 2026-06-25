"""
The median is the middle value in an ordered integer list. 
If the size of the list is even, there is no middle value, and the median is the mean of the two middle values.

For example, for arr = [2,3,4], the median is 3.
For example, for arr = [2,3], the median is (2 + 3) / 2 = 2.5.
"""
import heapq

minheap = []
maxheap = []
def addNum(num: int) -> None:
    if len(minheap) == len(maxheap):
        heapq.heappush(minheap, num)
        heapq.heappush(maxheap, -heapq.heappop(minheap))
    else:
        heapq.heappush(maxheap, -num)
        heapq.heappush(minheap, -heapq.heappop(maxheap))


def findMedian() -> float:
    if len(maxheap) > len(minheap):
        return -maxheap[0]
    else:
        return (-maxheap[0] +  minheap[0]) / 2.0
    
for num in [1,2,3,4, 5, 6]:
    addNum(num)
    print(minheap, maxheap)
    print(findMedian())