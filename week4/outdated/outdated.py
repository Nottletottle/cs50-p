import re

def outdated():
    months = [
        "January", "February", "March", "April", "May", "June", 
        "July", "August", "September", "October", "November", "December"
    ]
    month_to_number = {month: i + 1 for i, month in enumerate(months)}

    pattern = r"[/,\s]"

    while True:
        try:
            user_input = input("Date: ").strip()
            date_parts = [part.strip() for part in re.split(pattern, user_input) if part.strip()]

            if len(date_parts) != 3:
                raise ValueError("Invalid date format. Expected format: 'Month Day, Year' or 'Day/Month/Year'.")

            if date_parts[0].isalpha():  
                if "," not in user_input:
                    raise ValueError("Invalid format. Missing comma between Day and Year.")
                month_str, day_str, year_str = date_parts
                if month_str not in month_to_number:
                    raise ValueError("Invalid month name.")
                month = month_to_number[month_str]
                day = int(day_str)
                year = int(year_str)
            else:  
                month_str, day_str, year_str = date_parts
                day = int(day_str)
                month = int(month_str)
                year = int(year_str)
                if not (1 <= month <= 12):
                    raise ValueError("Month out of range.")                
                
            if day > 31 or month > 12:
                raise ValueError("Invalid date. Make sure to use 'Day/Month/Year' format.")

            if day > 28 and month == 2:
                raise ValueError("Day out of range for February.")
            if day > 30 and month in [4, 6, 9, 11]:
                raise ValueError(f"Day out of range for {months[month-1]}.")

            print(f"{year:04}-{month:02}-{day:02}")
            return

        except (ValueError, KeyError) as e:
            print(e)
            continue

outdated()
