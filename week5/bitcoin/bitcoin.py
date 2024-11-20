import requests
import sys

url = "https://api.coindesk.com/v1/bpi/currentprice.json"

try:
    if len(sys.argv) != 2:
        sys.exit("Missing Commandline Argument")
    coins = sys.argv[1]
    coins = float(coins)
    response = requests.get(url).json()
    total_price = coins * float(response["bpi"]["USD"]["rate_float"])
    print(f"${total_price:,.4f}")

except ValueError as e:
    sys.exit(e)
except requests.RequestException:
    ...
