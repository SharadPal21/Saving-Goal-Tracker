import json
import requests

class CurrencyConverter:
    def __init__(self, file_path):
        self.file_path = file_path
        self.exchange_rates = self._load_exchange_rates()

    def _load_exchange_rates(self):
        try:
            with open(self.file_path, "r") as file:
                return json.load(file)
        except FileNotFoundError:
            return {}

    def convert(self, amount, from_currency, to_currency):
        if from_currency not in self.exchange_rates or to_currency not in self.exchange_rates:
            raise ValueError("Currency not supported.")

        rate = self.exchange_rates[to_currency] / self.exchange_rates[from_currency]
        return round(amount * rate, 2)

    def update_exchange_rates(self, api_url):
        response = requests.get(api_url)
        if response.status_code == 200:
            self.exchange_rates = response.json()["rates"]
            with open(self.file_path, "w") as file:
                json.dump(self.exchange_rates, file, indent=4)
