"""

## 1. Sliding Window Median — Medium/Hard

You have a stream of integers and a window size `k`. For each window position, return the median. You cannot sort the full array each time.

**Input:** `nums = [1, 3, -1, -3, 5, 3, 6, 7]`, `k = 3`
**Output:** `[1.0, -1.0, -1.0, 3.0, 5.0, 6.0]`

**Constraint:** O(n log k) expected. No use of `statistics.median` inside the loop.

**What they're testing:** Two-heap approach (max-heap for lower half, min-heap for upper half). Balancing heaps on each slide, lazy deletion pattern. This is a classic hard problem that appears frequently in CodeSignal GCA at the 800+ score range.

---"""