"""Required tests from the assignment (Tasks A, B, and C)."""
import unittest
from main import Delivery, maximum_deliveries, minimum_drivers, minimum_rejections

A_CASES = [([], 0), ([(1,3)], 1), ([(1,3),(3,5),(5,7)], 3),
           ([(1,5),(2,6),(3,7)], 1), ([(5,7),(1,3),(3,5),(2,4)], 3),
           ([(1,4),(2,4),(4,6)], 2)]
B_CASES = [([], 0), ([(1,3)], 1), ([(1,3),(3,5),(5,7)], 1),
           ([(1,5),(2,6),(3,7)], 3), ([(1,4),(2,5),(4,7),(5,8)], 2),
           ([(5,8),(1,4),(2,5),(4,6),(6,9)], 2)]
C_CASES = [([], 0), ([(1,3)], 0), ([(1,3),(3,5),(5,7)], 0),
           ([(1,5),(2,6),(3,7)], 2), ([(5,7),(1,3),(3,5),(2,4)], 1),
           ([(1,2),(2,3),(3,4),(1,3)], 1)]


def deliveries_from_pairs(pairs):
    return [Delivery(f'D{i:02d}', s, f) for i, (s, f) in enumerate(pairs, 1)]


class RequiredTests(unittest.TestCase):
    def test_task_a(self):
        for i, (pairs, expected) in enumerate(A_CASES, 1):
            with self.subTest(test=i):
                self.assertEqual(len(maximum_deliveries(deliveries_from_pairs(pairs))), expected)

    def test_task_b(self):
        for i, (pairs, expected) in enumerate(B_CASES, 1):
            with self.subTest(test=i):
                jobs = deliveries_from_pairs(pairs)
                schedules = minimum_drivers(jobs)
                self.assertEqual(len(schedules), expected)
                self.assertEqual(sum(map(len, schedules)), len(jobs))
                for schedule in schedules:
                    for a, b in zip(schedule, schedule[1:]):
                        self.assertLessEqual(a.finish, b.start)

    def test_task_c(self):
        for i, (pairs, expected) in enumerate(C_CASES, 1):
            with self.subTest(test=i):
                self.assertEqual(minimum_rejections(deliveries_from_pairs(pairs)), expected)


if __name__ == '__main__':
    unittest.main(verbosity=2)
