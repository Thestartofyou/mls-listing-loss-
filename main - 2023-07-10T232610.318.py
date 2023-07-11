import requests
import datetime

def find_expired_listings(api_key):
    # Replace this URL with the endpoint of your MLS data API
    url = "https://example.com/mls-api/listings"

    headers = {"Authorization": api_key}
    today = datetime.date.today().strftime("%Y-%m-%d")

    try:
        response = requests.get(url, headers=headers)
        data = response.json()

        expired_listings = [
            listing for listing in data["listings"]
            if listing["expiration_date"] < today
        ]

        for listing in expired_listings:
            print("Listing ID:", listing["id"])
            print("Address:", listing["address"])
            print("Expiration Date:", listing["expiration_date"])
            print("-" * 40)

        print(f"Total Expired Listings: {len(expired_listings)}")

    except requests.exceptions.RequestException as e:
        print("An error occurred while accessing the MLS API:", str(e))

# Example usage:
api_key = "YOUR_API_KEY"
find_expired_listings(api_key)
