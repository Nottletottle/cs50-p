def main():
    time = input("What time is it? ")
    time_24h = convert(time.strip())

    if 7 <= time_24h < 9:
        print("breakfast time")
    elif 12 <= time_24h < 14:
        print("lunch time")
    elif 18 <= time_24h < 20:
        print("dinner time")
    else:
        return

def convert(time):
    if "a.m." in time or "p.m." in time:
        time, period = time.split()
        hour, minute = map(int, time.split(":"))
        if period == "p.m." and hour != 12:
            hour += 12
        if period == "a.m." and hour == 12:
            hour = 0
    else:
        hour, minute = map(int, time.split(":"))

    return hour + minute / 60

if __name__ == "__main__":
    main()
