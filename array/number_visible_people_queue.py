"""
Number of Visible People in a Queue
====================================

PROBLEM:
  Given heights[], for each person i, count how many people to their right
  they can see. Person i sees person j (i < j) if everyone between them is
  shorter than both: min(heights[i], heights[j]) > max(heights[i+1:j]).

PATTERN: Monotonic Stack (decreasing)
  - This is a classic "next greater element" family problem.
  - Recognise it when: you compare elements with others to their left/right
    and shorter/smaller elements get "blocked" or "consumed" by taller/larger ones.

WHEN TO USE A MONOTONIC STACK:
  - "Next greater/smaller element" questions
  - "How many can you see / reach" with blocking
  - Stock span, daily temperatures, trapping rain water, largest rectangle
  - Any time an element invalidates/dominates previous smaller elements

HOW IT WORKS (decreasing stack, right to left):
  1. Process from right to left
  2. For each person i:
     - Pop everyone SHORTER than heights[i] → you can see each of them (+1 per pop)
     - If stack is non-empty after popping → you can also see that taller person (+1)
     - Push heights[i] onto the stack
  3. The stack always stays in decreasing order (tall at bottom, short at top)

WHY POPPING = SEEING:
  - Short people on the stack are between you and taller people further right
  - Since you're taller, you see OVER everyone in between to reach them
  - Once popped, they'll never be visible to anyone further left (you block them)
  
WHY THE STACK TOP AFTER POPPING IS VISIBLE:
  - It's the first person taller than you → you can see them
  - But you can't see past them (they block your view)

COMPLEXITY:
  - O(n) time: each element pushed once, popped at most once
  - O(n) space: the stack

APPROACHES (from brute to optimal):
  1. Brute force O(n³): for each pair (i,j), scan max of heights[i+1:j]
  2. Running max O(n²): track max_between as j moves right, avoid re-scanning
  3. Monotonic stack O(n): each person pushed/popped at most once ← optimal

TEMPLATE:
  stack = []
  for i in range(n - 1, -1, -1):
      count = 0
      while stack and stack[-1] < current:   # pop shorter
          stack.pop()
          count += 1
      if stack:                               # taller person still there
          count += 1
      answer[i] = count
      stack.append(current)

SIMILAR PROBLEMS:
  - Next Greater Element (I, II, III)
  - Daily Temperatures
  - Stock Span
  - Largest Rectangle in Histogram
  - Trapping Rain Water
"""

heights = [10,6,8,5,11,9]

# def can_see(heights):
#     counts = [0] * len(heights)
#     max_between = 0
#     for i in range(len(heights)):
#         count = 0
#         for j in range(i+1, len(heights)):
#             # immediate next person is always visible
#             if j == i + 1:
#                 count += 1
#                 continue
#             else:
#                 print('i', heights[i], 'j', heights[j])
#                 max_between = max(max_between, heights[j-1])
#                 if min(heights[i], heights[j]) > max_between:   
#                     count += 1
        
#         counts[i] = count
#     return counts

# print(can_see(heights))
heights = [10,6,8,5,11,9]
n = len(heights)
counts = [0] * n
stack = []
for i in range(n-1, -1, -1):
    count = 0
    while stack:        
        if heights[i] > stack[-1]:
            count += 1
            stack.pop()
        else:
            break
    if stack: # basically if there is a taller person to the right, they can see that person
        count += 1
    counts[i] = count
    stack.append(heights[i])
    print('stack', stack)
    print('counts', counts)