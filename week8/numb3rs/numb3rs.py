import re


def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    if matches := re.match(r"^((?:\d{1,3}\.){3}(?:\d{1,3}))$", ip.strip()):
        octets = matches.group(1).split(".")
        # Check each octet
        for octet in octets:
            if not (0 <= int(octet) <= 255):
                return False
            if octet != str(int(octet)):  # Check for leading zeros
                return False
        return True
    return False


if __name__ == "__main__":
    main()
