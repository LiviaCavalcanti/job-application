
"""## 4. SQL: Session Attribution — Hard

You have a table `events(user_id, event_type, event_ts)`. 
Define a **session** as a sequence of events from the same user where no two consecutive events are more than 30 minutes apart. 
Write a query that:

1. Assigns a unique `session_id` to each event
2. Returns the number of sessions per user
3. Returns the average session length (in minutes) per user

**Constraint:** PostgreSQL. No procedural code, pure SQL.

**What they're testing:** `LAG()` to detect session boundaries, conditional `SUM()` with `OVER` to assign session IDs, then aggregation. 
The tricky part is that `session_id` must be derived purely from window functions before aggregating.

---
"""

"""
SOLUTION:

Step 1: Use LAG() to get the previous event timestamp per user.
Step 2: Flag a new session when the gap > 30 minutes (or it's the first event).
Step 3: Running SUM() of that flag gives each event a session_id.
Step 4: Aggregate to get session count and avg session length per user.

-- Step 1 & 2: Detect session boundaries
WITH with_prev AS (
    SELECT
        user_id,
        event_type,
        event_ts,
        LAG(event_ts) OVER (PARTITION BY user_id ORDER BY event_ts) AS prev_ts
    FROM events
),
with_session_flag AS (
    SELECT
        *,
        CASE
            WHEN prev_ts IS NULL
              OR EXTRACT(EPOCH FROM (event_ts - prev_ts)) / 60 > 30
            THEN 1
            ELSE 0
        END AS new_session
    FROM with_prev
),

-- Step 3: Assign session_id via running sum of the flag
with_session_id AS (
    SELECT
        *,
        SUM(new_session) OVER (PARTITION BY user_id ORDER BY event_ts) AS session_id
    FROM with_session_flag
),

-- Step 4: Get session boundaries, then aggregate per user
session_stats AS (
    SELECT
        user_id,
        session_id,
        MIN(event_ts) AS session_start,
        MAX(event_ts) AS session_end
    FROM with_session_id
    GROUP BY user_id, session_id
)

SELECT
    user_id,
    COUNT(*)                                                          AS num_sessions,
    AVG(EXTRACT(EPOCH FROM (session_end - session_start)) / 60)       AS avg_session_length_min
FROM session_stats
GROUP BY user_id;

---

KEY CONCEPTS:
  - LAG() to compare each row with its predecessor within a partition
  - Conditional CASE to flag session boundaries (gap > 30 min or first event)
  - Running SUM() of a 0/1 flag to assign incrementing session IDs
  - This "gap-and-island" pattern is reusable for any sessionization problem

PATTERN: Gap and Island
  1. LAG() to find gaps between consecutive rows
  2. Flag rows where a new group starts (gap exceeds threshold)
  3. Running SUM() of flags = group ID
  4. Aggregate within groups
"""
