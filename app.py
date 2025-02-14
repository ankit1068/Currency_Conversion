from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

ACCESS_KEY = "f4a811d1ab5377ba6e088c48278e8e06"
API_URL = f"http://data.fixer.io/api/latest?access_key={ACCESS_KEY}"

# Fetch exchange rates from Fixer API
def get_exchange_rates():
    response = requests.get(API_URL)
    data = response.json()
    return data.get("rates", {})

@app.route('/convert', methods=['POST'])
def convert_currency():
    data = request.json
    from_currency = data.get("from_currency", "").upper()
    to_currency = data.get("to_currency", "").upper()
    amount = float(data.get("amount", 0))

    rates = get_exchange_rates()

    # Validate currency codes
    if from_currency not in rates or to_currency not in rates:
        return jsonify({"error": "Invalid currency code"}), 400

    # Convert currency
    if from_currency != "EUR":
        amount = amount / rates[from_currency]

    converted_amount = round(amount * rates[to_currency], 2)

    return jsonify({"result": f"{data['amount']} {from_currency} = {converted_amount} {to_currency}"})

if __name__ == '__main__':
    app.run(debug=True)
