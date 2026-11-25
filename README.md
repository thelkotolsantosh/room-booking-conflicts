# Room Booking Conflicts

Facilities coordinators can check a single day's meeting-room export for double bookings before distributing the schedule. Each finding identifies both bookings, their shared room and the overlap in minutes.

## Run locally

Download the repository and open its directory with Python 3.10 or newer installed. All dependencies ship with Python.

```sh
python bookings.py examples/day.csv
python -m unittest discover -s tests -v
```

The sample flags training and review in Cedar for 15 minutes. Planning starts when review ends and remains clear.

## Export format

Use the exact CSV header in examples/day.csv. Each booking needs a unique ID, a room and two same-day local times in HH:MM format. Use one timezone and one date per export. Supply the file path as the sole argument. Aliases for the same room must be normalized before export.

## Implementation and output

bookings.py validates the entire file, groups intervals by room and sorts each group by start time. For each new booking it compares still-active reservations and emits one JSON record per overlapping pair. An empty JSON list means the schedule passed. Parse errors go to stderr with exit status 2. Findings are a successful report and return status 0.

Tests live under tests/ and synthetic data under examples/. Run locally on trusted exports. Protect the output because it includes booking identifiers. Dense calendars can produce quadratically many pairs. Recurring events and overnight bookings require preprocessing. Future extensions could group records by date. See faq.md for examples of boundary behavior and CONTRIBUTING.md for development guidance. MIT license.
