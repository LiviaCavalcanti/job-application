"""
Merge Intervals
================

PROBLEM:
  Given intervals [[start, end], ...], merge all overlapping intervals.
  Return non-overlapping intervals covering all input.

PATTERN: Sort + Sweep (Interval Merging)
  - Sort by start time → overlaps can only happen with the previous interval
  - Sweep left to right, maintaining one "active" interval
  - Decide per element: merge with active, or start a new one

WHY SORT FIRST:
  - Unsorted intervals can overlap in any direction → O(n²) pairwise checks
  - Sorting guarantees: if interval[i] doesn't overlap with active, nothing
    after it will either (since all future starts are >= current start)
  - Reduces problem to a single O(n) pass

TEMPLATE:
  intervals.sort()
  result = [intervals[0]]
  for start, end in intervals[1:]:
      if start <= result[-1][1]:              # overlaps → merge
          result[-1][1] = max(result[-1][1], end)
      else:                                   # gap → new interval
          result.append([start, end])

COMPLEXITY:
  - O(n log n) time (sorting dominates)
  - O(n) space (result list)

SIMILAR PROBLEMS (same sort + sweep pattern):
  Problem                          | Sort by | Decision at sweep
  ---------------------------------+---------+------------------------------------
  Merge intervals                  | start   | Overlap → extend end; else new
  Insert interval                  | sorted  | Find overlap region, merge, keep rest
  Meeting rooms (can attend all?)  | start   | Any overlap → return False
  Meeting rooms II (min rooms)     | start   | Count concurrent (min-heap of ends)
  Non-overlapping (min removals)   | end     | Greedy: keep earliest-ending
  Interval intersection            | both    | Two-pointer sweep
  Employee free time               | start   | Merge all, gaps = free time

KEY INSIGHT:
  The only thing that changes across interval problems is WHAT YOU DO
  at the decision point (merge, count, remove, etc.). The sort + sweep
  structure stays the same.

Example:
Input:  [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
"""

intervals = [[1,3],[2,6],[8,10],[15,18]]
intervals = [[1,4],[4,5]]
intervals = [[4,7],[1,4]]
i= 0

intervals.sort(key=lambda x: x[0])
# while i < len(intervals):
#     j = i + 1
#     while j <  len(intervals):
#         if intervals[i][1] >= intervals[j][0] :
#             if intervals[i][1] <= intervals[j][1]:
#                 intervals[i][1] = intervals[j][1]
#                 intervals.pop(j)
#             elif intervals[i][1] > intervals[j][1] and intervals[i][1] > intervals[j][1]:
#                 if intervals[i][0] > intervals[j][0]:
#                     intervals[i][0] = intervals[j][0]
#                 intervals.pop(j)

#         else:
#             j += 1
#     i += 1

# print(intervals)

merged = [intervals[0]]
for i in intervals[1:]:
    if merged[-1][1] >= i[0]:
        merged[-1][1] = max(merged[-1][1], i[1])
    else:
        merged.append(i)
print(merged)