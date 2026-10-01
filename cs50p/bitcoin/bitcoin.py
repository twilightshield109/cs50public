import requests
import sys
import json


if len(sys.argv) == 2:
    url = 'https://rest.coincap.io/v3/assets/bitcoin?apiKey=75a9f29bdc08a8e94a98186523cb55c402496612d34961ad69f03e74661e7976'
    try:
        r = requests.get(url)
        json = r.json()
        n = float(sys.argv[1])
    except ValueError:
        sys.exit("Command-line argument is not a number")
    except requests.RequestException:
        sys.exit("Requests don't work")
    else:
        coin = float(json['data']['priceUsd'])
        amount = n * coin
        print(f"${amount:,.4f}")

if len(sys.argv) == 1:
    sys.exit("Missing command-line argument")


