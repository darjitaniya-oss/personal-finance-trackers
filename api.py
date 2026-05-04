import requests

def get_rate():
    url = "https://api.exchangerate-api.com/v4/latest/USD"
    data = requests.get(url).json()
    print("USD to INR:", data["rates"]["INR"])
