## 1. What does the auditor review?

One day of room bookings exported to CSV.

## 2. Who can use the report?

A facilities coordinator can contact the owners of two overlapping bookings.

## 3. What counts as a conflict?

Two bookings for the same room must share at least one minute.

## 4. Can three bookings conflict?

Yes. Each overlapping pair appears once.

## 5. Which language implements the checks?

Python handles both CSV validation and interval comparison.

## 6. Which framework is required?

The CLI uses argparse, csv and json from the standard library.

## 7. What runtime do I need?

Use Python 3.10 or newer and a readable local schedule.

## 8. How do I install the tool?

Download the repository and open a terminal in its directory.

## 9. Where do I configure the schedule?

Pass the CSV path as the command argument each time.

## 10. How do I try it?

Run python bookings.py examples/day.csv.

## 11. Where are the main files?

bookings.py contains the CLI and scorer. examples holds a sample day and tests contains the regression cases.

## 12. How are nested intervals handled?

A longer booking stays active until its end even when shorter meetings finish within it.

## 13. Which columns are required?

Use room,booking,start,end in that order.

## 14. What output can I archive?

Redirect stdout to a JSON file. Each finding includes overlap_minutes.

## 15. How do I customize room names?

Use consistent case and spelling for each physical room in your export.

## 16. What happens on invalid input?

The command exits with status 2 and prints an error to stderr.

## 17. Why was my time rejected?

Write 09:00 with a leading zero. Hours run from 00 to 23.

## 18. How can I diagnose unexpected collisions?

Check that the file contains one date and that room aliases were normalized.

## 19. How do I run tests?

Run python -m unittest discover -s tests -v in the project directory.

## 20. What should a contribution include?

Provide a small schedule, expected pairs and a regression test.

## 21. Can I include overnight meetings?

Split the calendar into supported same-day intervals before analysis. Midnight end boundaries expressed as 24:00 are unsupported.

## 22. Can I use this to prevent bookings live?

It audits a snapshot. A live reservation system needs concurrency controls at booking time.

## 23. What could be added next?

A date column would allow multi-day exports to be grouped before comparison.

## 24. How should I protect meeting details?

Use synthetic or opaque booking IDs and restrict access to the JSON report.

## 25. Where can I check the expected demo result?

The README identifies the conflicting bookings in the example and their shared duration.

