import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):
    pattern = r"(^\d{1,2})(?::(\d{2}))? (AM|PM) to (\d{1,2})(?::(\d{2}))? (AM|PM)$"
    if matches := re.search(pattern, s):
        # Extracting hour and minute components
        start_hour = int(matches.group(1))
        start_minute = int(matches.group(2) or 0)
        end_hour = int(matches.group(4))
        end_minute = int(matches.group(5) or 0)

        # Validate hours
        if not (1 <= start_hour <= 12) or not (1 <= end_hour <= 12):
            raise ValueError
        # Validate minutes
        if not (0 <= start_minute <= 59) or not (0 <= end_minute <= 59):
            raise ValueError

        # Convert to 24-hour format
        if matches.group(3) == "PM" and start_hour != 12:
            start_hour += 12
        if matches.group(6) == "PM" and end_hour != 12:
            end_hour += 12
        if matches.group(3) == "AM" and start_hour == 12:
            start_hour = 0
        if matches.group(6) == "AM" and end_hour == 12:
            end_hour = 0

        # Format output
        start_time = f"{start_hour:02}:{start_minute:02}"
        end_time = f"{end_hour:02}:{end_minute:02}"

        return f"{start_time} to {end_time}"

    raise ValueError


if __name__ == "__main__":
    main()
