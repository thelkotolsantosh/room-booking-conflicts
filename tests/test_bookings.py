from io import StringIO
import unittest

from bookings import conflicts


def audit(rows):
    return conflicts(StringIO("room,booking,start,end\n" + rows))


class BookingTests(unittest.TestCase):
    def test_nested(self):
        hits = audit("A,c,10:05,10:10\nA,a,09:00,12:00\nA,b,10:00,11:00")
        self.assertEqual([r["overlap_minutes"] for r in hits], [60, 5, 5])

    def test_boundary_and_rooms(self):
        self.assertEqual(audit("A,a,09:00,10:00\nA,b,10:00,11:00\nB,c,09:00,10:00"), [])

    def test_bad_rows(self):
        for row in ["A,id,25:00,26:00", "A,id,12:00,11:00", "A,,09:00,10:00",
                    "A,id,09:00,10:00\nB,id,10:00,11:00"]:
            with self.subTest(row=row), self.assertRaises(ValueError):
                audit(row)

    def test_empty_day(self):
        self.assertEqual(audit(""), [])
