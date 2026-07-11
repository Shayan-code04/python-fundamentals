import json 
import requests 
def fetch_price(coin_ids):
    url = (
        f"https://api.coingecko.com/api/v3/simple/price"
        f"?ids={coin_ids}&vs_currencies=usd"
    )
    response = requests.get(url)
    if response.status_code==200:
        return response.json()
    else:
        print(f"Error: {response.status_code}")
        return None

def save_to_file(data,filename):
    with open(filename,"w") as f:
        json.dump(data,f,indent=4)


def display_price(data):
    for coin, details in data.items():
        price = details["usd"]
        print(f"{coin.capitalize()}: ${price:,}")

def main():
    coin_ids="bitcoin,ethereum"

    data = fetch_price(coin_ids) 


    if data:
        display_price(data)
        save_to_file(data,"prices.json")


if __name__=="__main__":
    main()