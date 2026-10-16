# CS 413 Pioneer Delivery Company Part I: Greedy Algorithms in Python

# Files

- `main.py`
- `deliveries.txt`
- `test_main.py`

# Run the program

python main.py deliveries.txt

## Run the test cases:

python -m unittest -v test_main.py

## Task A — Maximum deliveries for one driver

1. the greedy choice made by my algorithm is that it selects the next delivery whose start time is at least the previous selected delivery's finish time.

2. this is optimal because in any optimal nonempty schedule, it first selected delivery can be replaced with the earliest-finishing delivery without causing an overlap, because the replacement finishes no later. This leaves at least as much room for subsequent deliveries. If we repeat this, the exchange argument proves the greedy schedule has the maximum number of compatible requests.

3. The running time for this algorithm is that the sorting takes O(n log n) and the scan takes O(n), giving O(n log n) overall.

## Task B — Minimum number of drivers

1. The priority queue will store each driver's finish time and driver ID. It is then organized as a min heap so that the driver who finishes earliest can be found quickly and then assigned to the next compatible delivery.

2. For each delivery, the greedy algorithm will check the driver with the earliest finish time using the min heap and then if that driver finishes before or right at a new delivery starts, it will reuse that driver. Otherwise, a new driver is created and assigned.

3. The algorithm uses the minimum number of drivers because it reuses whichever available driver whenever they are able to be reused. A new driver is only added if all existing drivers are busy so the algorithm only creates the amount of drivers necessary to complete all deliveries.

4. The running time for this is O(n log n) since sorting the deliveries by start time is O(n log n). Then deliveries require priority queue that also takes O(n log n) time. Since there are n deliveries depending on the input, the total running time is O(n log n).

## Task C — Minimum rejected deliveries

1. Task C uses the same greedy algorithm as task A. While A finds the maximum amount of non overlapping deliveries, C uses that result to find the minimum number that has to be rejected.

2. The minimum rejected deliveries are n-k where n is the amount of total deliveries and k is the maximum number of compatible deliveries found with task A.

3. The running time for the algoritm is once again O(n log n). Sorting deliveries by finis time is O(n log n) and selecting the compatible deliveries is O(n) while calculating the number of rejected deliveries is O(1)


## Task D: When a Greedy Choice Fails

1. Counterexample

Consider three deliveries:

respectively,

Delivery: A, B, C

Ready time: 0, 0, 1

Profit: 100, 90, 80


2. Greedy Schedule

The greedy algorithm selects deliveries in decreasing order of profit: A, B, C.

- A is scheduled at time 0: 100 / (1 + 0) = 100 since it has the highest profit
- B is scheduled at time 1: 90 / (1 + 1) = 45
- C is scheduled at time 2: 80 / (1 + 1) = 40

Total value is 100 + 45 + 40 = 185

3. Better Schedule S

Instead, schedule deliveries in the order A, C, B.

- A is scheduled at time 0: 100 / (1 + 0) = 100
- C is scheduled at time 1: 80 / (1 + 0) = 80
- B is scheduled at time 2: 90 / (1 + 2) = 30

Total value is 100 + 80 + 30 = 210 

4. 

The greedy strategy is not always optimal because choosing the highest profit delivery first might  delay other deliveries and reduce their values. For this example, the greedy schedule has a total value of 185 and the better schedule produces 210. Since 210 is more than 185, this is a counterexample of how the greedy strategy does not always produce best total value.

## Required test results

Task A: maximum selected: 1, 2, 3, 4, 5, 6
Task B: minimum drivers selected: 0, 1, 3, 1, 3, 2
Task C: minimum rejected: 0, 0, 0, 2, 1, 1


## Example run with `deliveries.txt`

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


Github link: https://github.com/MatthewChou/CS413-Algorithm-Portfolio