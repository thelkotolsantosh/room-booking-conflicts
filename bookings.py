"""Find double bookings in a single day's room schedule."""
import argparse
import csv
import json
import re
from collections import defaultdict


def minutes(value):
    if not re.fullmatch(r"(?:[01][0-9]|2[0-3]):[0-5][0-9]", value):
        raise ValueError(f"invalid 24-hour time {value!r}")
    return int(value[:2]) * 60 + int(value[3:])


def conflicts(stream):
    reader = csv.reader(stream, strict=True)
    if next(reader, None) != ["room", "booking", "start", "end"]:
        raise ValueError("expected header room,booking,start,end")
    rooms = defaultdict(list)
    seen = set()
    for line, row in enumerate(reader, 2):
        if len(row) != 4 or not all(field.strip() for field in row):
            raise ValueError(f"incomplete record {line}")
        room, booking, start, end = map(str.strip, row)
        left, right = minutes(start), minutes(end)
        if left >= right or booking in seen:
            raise ValueError(f"invalid interval or duplicate booking at record {line}")
        seen.add(booking)
        rooms[room].append((left, right, booking))
    result = []
    for room in sorted(rooms):
        active = []
        for start, end, booking in sorted(rooms[room]):
            active = [(stop, name) for stop, name in active if stop > start]
            for stop, name in active:
                result.append(dict(room=room, first=name, second=booking,
                                   overlap_minutes=min(stop, end) - start))
            active.append((end, booking))
    return result


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("schedule")
    args = parser.parse_args()
    try:
        with open(args.schedule, encoding="utf-8-sig", newline="") as source:
            print(json.dumps(conflicts(source), indent=2))
    except (OSError, ValueError, csv.Error) as exc:
        parser.exit(2, f"Schedule error: {exc}\n")
