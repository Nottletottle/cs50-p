import re


def main():
    print(parse(input("HTML: ")))


def parse(s):
    pattern = r"\"https?://(?:www\.)?youtube\.com/embed/(.[^\"']+)"
    if matches := re.search(pattern, s, re.IGNORECASE):
        video_id = matches.group(1)
        return f"https://youtu.be/{video_id}"
    return None


if __name__ == "__main__":
    main()
