from datetime import date
import inflect
import re
import sys


def calculate_age_in_minutes(birth_date):
    """Calculate the age in minutes given a birth date."""
    today = date.today()
    age = today - birth_date
    # Convert age to minutes
    age_in_minutes = age.days * 24 * 60
    return age_in_minutes


def number_to_words(number):
    """Convert a number to words using the inflect library, formatted as required."""
    p = inflect.engine()
    words = p.number_to_words(number).replace("-", " ")

    # Remove "and"
    words = words.replace(" and ", " ")

    # Replace occurrences of "ty " with "ty-" using regex
    words = re.sub(r"\b(\w*ty)\s", r"\1-", words)

    return words.strip()


def is_valid_date(year, month, day):
    """Check if a date is valid, considering leap years."""
    try:
        date(year, month, day)
        return True
    except ValueError:
        return False


def main():
    birth_date_input = input("Enter your date of birth (YYYY-MM-DD): ")

    try:
        # Convert input string to date object
        year, month, day = map(int, birth_date_input.split("-"))

        if not is_valid_date(year, month, day):
            print(f"The date {birth_date_input} is not valid.")
            sys.exit(1)

        birth_date = date(year, month, day)
    except ValueError:
        print("Invalid date format. Please use YYYY-MM-DD.")
        sys.exit(1)

    age_in_minutes = calculate_age_in_minutes(birth_date)

    age_in_words = number_to_words(age_in_minutes)

    print(f"{age_in_words.capitalize()} minutes")


if __name__ == "__main__":
    main()
