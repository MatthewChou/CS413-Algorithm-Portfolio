"""CS 413 PA Part I - greedy delivery scheduling."""
import argparse
import heapq
from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True)
class Delivery:
    id: str
    start: int
    finish: int


def read_deliveries(path: str) -> list[Delivery]:
    """Read lines in the format: ID START FINISH. Blank lines and # comments allowed."""
    deliveries = []
    ids = set()
    for line_number, line in enumerate(Path(path).read_text().splitlines(), 1):
        line = line.split('#', 1)[0].strip()
        if not line:
            continue
        parts = line.split()
        if len(parts) != 3:
            raise ValueError(f"Line {line_number}: expected ID START FINISH")
        id_, start_text, finish_text = parts
        try:
            start, finish = int(start_text), int(finish_text)
        except ValueError as exc:
            raise ValueError(f"Line {line_number}: times must be integers") from exc
        if start >= finish:
            raise ValueError(f"Line {line_number}: start must be before finish")
        if id_ in ids:
            raise ValueError(f"Line {line_number}: duplicate ID {id_}")
        ids.add(id_)
        deliveries.append(Delivery(id_, start, finish))
    return deliveries


def maximum_deliveries(deliveries: list[Delivery]) -> list[Delivery]:
    """Task A: earliest-finish-time interval scheduling, O(n log n)."""
    result = []
    last_finish = float('-inf')
    for job in sorted(deliveries, key=lambda d: (d.finish, d.start, d.id)):
        if job.start >= last_finish:
            result.append(job)
            last_finish = job.finish
    return result


def minimum_drivers(deliveries: list[Delivery]) -> list[list[Delivery]]:
    """Task B: heap of (next_available_time, driver_index), O(n log n)."""
    schedules: list[list[Delivery]] = []
    heap: list[tuple[int, int]] = []
    for job in sorted(deliveries, key=lambda d: (d.start, d.finish, d.id)):
        if heap and heap[0][0] <= job.start:
            _, driver_index = heapq.heappop(heap)
        else:
            driver_index = len(schedules)
            schedules.append([])
        schedules[driver_index].append(job)
        heapq.heappush(heap, (job.finish, driver_index))
    return schedules


def minimum_rejections(deliveries: list[Delivery]) -> int:
    """Task C: total requests minus Task A optimum, O(n log n)."""
    return len(deliveries) - len(maximum_deliveries(deliveries))


def show_jobs(jobs: list[Delivery]) -> str:
    return ', '.join(f'{job.id} ({job.start}, {job.finish})' for job in jobs) or '(none)'


def main() -> None:
    parser = argparse.ArgumentParser(description='Pioneer Delivery greedy scheduling')
    parser.add_argument('input_file', help='Path to delivery request data file')
    args = parser.parse_args()
    deliveries = read_deliveries(args.input_file)
    selected = maximum_deliveries(deliveries)
    schedules = minimum_drivers(deliveries)
    print('TASK A: Maximum deliveries for one driver')
    print('Selected:', show_jobs(selected))
    print('Maximum deliveries:', len(selected))
    print('\nTASK B: Minimum number of drivers')
    for i, schedule in enumerate(schedules, 1):
        print(f'Driver {i}: {show_jobs(schedule)}')
    print('Minimum drivers required:', len(schedules))
    print('\nTASK C: Minimum rejected deliveries')
    print('Minimum rejected:', minimum_rejections(deliveries))


if __name__ == '__main__':
    main()
