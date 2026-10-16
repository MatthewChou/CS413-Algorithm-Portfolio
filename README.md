# Pioneer Delivery Company — Part I: Greedy Algorithms

**Course:** CS 413 — Analysis of Algorithms  
**Programming language:** Python 3  
**Student:** [Fill in your name]

## Files

- `main.py`: Tasks A, B, and C, plus file parsing and formatted output
- `deliveries.txt`: example delivery request data
- `test_main.py`: six required test cases for each of Tasks A, B, and C

## Run the program

No additional libraries are needed. From this folder, run:

```bash
python main.py deliveries.txt
```

Run the test cases:

```bash
python -m unittest -v test_main.py
```

## Input format

Each nonblank, noncomment line contains three whitespace-separated fields:

```
DELIVERY_ID START_TIME FINISH_TIME
```

Times are integers and `START_TIME < FINISH_TIME`. IDs must be unique. Lines beginning with `#` are comments.

Example:

```
D01 10 13
D02 2 5
D03 4 7
```

A delivery that finishes exactly when another starts does not overlap with it.

## Program organization

- `Delivery`: stores ID, start time, and finish time.
- `read_deliveries`: reads and validates the input file.
- `maximum_deliveries`: Task A greedy interval scheduling.
- `minimum_drivers`: Task B greedy interval partitioning with a min-heap.
- `minimum_rejections`: Task C, using the result of Task A.
- `main`: handles command-line input and displays results.

## Task A — Maximum deliveries for one driver

**Greedy choice:** Sort intervals by increasing finish time. Select the next delivery whose start time is at least the previous selected delivery's finish time.

**Why optimal:** Consider the earliest-finishing delivery. In any optimal nonempty schedule, its first selected delivery can be replaced with the earliest-finishing delivery without causing an overlap, because the replacement finishes no later. This leaves at least as much room for subsequent deliveries. Repeating this exchange argument proves the greedy schedule has the maximum number of compatible requests.

**Running time:** Sorting takes `O(n log n)` and the scan takes `O(n)`, giving `O(n log n)` overall.

## Task B — Minimum number of drivers

**Priority queue contents:** Each heap element is `(driver_next_available_time, driver_index)`, and the heap contains one element for each currently allocated driver.

**Selecting a driver:** Process deliveries by increasing start time. If the driver with the smallest finishing time is free by the new delivery's start time, reuse that driver. Otherwise create a new driver. Update the driver's finishing time in the heap.

**Why optimal:** A new driver is created only if the earliest available current driver is still busy at the new delivery's start time. Therefore all existing drivers are busy when the new request begins. These requests overlap at that point, so at least that many drivers are required. The algorithm creates a new driver only when necessary and therefore uses the minimum possible number.

**Running time:** Sorting takes `O(n log n)`. Each of the `n` requests requires at most one heap removal and one insertion, each taking `O(log n)`. Total `O(n log n)`.

## Task C — Minimum rejected deliveries

This is the complement of Task A. If Task A finds a largest compatible subset of size `k` out of `n` total deliveries, at least `n-k` must be rejected, and keeping that subset achieves exactly that many rejections.

**Formula:** `minimum rejected = n - k`.

**Running time:** One invocation of Task A takes `O(n log n)`; subtraction is `O(1)`, so total `O(n log n)`.

## Task D — Counterexample to greedy profit-first scheduling

**Deliveries** (each takes one time slot):

| Delivery | Ready time R | Profit P |
|---|---:|---:|
| A | 0 | 100 |
| B | 0 | 90 |
| C | 1 | 80 |

All profits are positive and distinct; all ready times are nonnegative integers.

**Greedy strategy G:** In decreasing order of profit, schedule each delivery in its earliest available slot:

| Delivery | Slot T | Delay D = T-R | Value P/(1+D) |
|---|---:|---:|---:|
| A | 0 | 0 | 100 |
| B | 1 | 1 | 45 |
| C | 2 | 1 | 40 |

`V(G) = 100 + 45 + 40 = 185`.

**Better schedule S:**

| Delivery | Slot T | Delay D = T-R | Value P/(1+D) |
|---|---:|---:|---:|
| A | 0 | 0 | 100 |
| C | 1 | 0 | 80 |
| B | 2 | 2 | 30 |

`V(S) = 100 + 80 + 30 = 210`.

Both schedules are feasible: each delivery starts no earlier than its ready time, and no two deliveries share a slot. Since `210 > 185`, G does not always maximize total value.

## Required test results

All 18 required cases were checked using `test_main.py`.

| Test | Task A: maximum selected | Task B: minimum drivers | Task C: minimum rejected |
|---:|---:|---:|---:|
| 1 | 0 | 0 | 0 |
| 2 | 1 | 1 | 0 |
| 3 | 3 | 1 | 0 |
| 4 | 1 | 3 | 2 |
| 5 | 3 | 2 | 1 |
| 6 | 2 | 2 | 1 |

**Important:** Each task uses its own six test inputs provided in the handout. Row numbers do not imply the same intervals across different tasks.

## Example run with `deliveries.txt`

```
TASK A: Maximum deliveries for one driver
Selected: D02 (2, 5), D05 (8, 11), D06 (11, 14)
Maximum deliveries: 3

TASK B: Minimum number of drivers
Driver 1: D04 (1, 8), D06 (11, 14)
Driver 2: D02 (2, 5), D05 (8, 11), D07 (13, 16)
Driver 3: D03 (4, 7), D01 (10, 13)
Minimum drivers required: 3

TASK C: Minimum rejected deliveries
Minimum rejected: 4
```
