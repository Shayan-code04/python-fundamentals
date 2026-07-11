
import json
import requests

def fetch_post(post_id):
    url = f"https://jsonplaceholder.typicode.com/posts/{post_id}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error: {response.status_code}")
        return None

def save_to_file(data, filename):
    with open(filename, "w") as f:
        json.dump(data, f, indent=4)

def main():
    post_id = 1
    data = fetch_post(post_id)
    if data:
        print(json.dumps(data, indent=4))
        save_to_file(data, "post_1.json")

if __name__ == "__main__":
    main()