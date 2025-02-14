# Currency Converter

A simple currency converter web application that allows users to convert amounts between different currencies using real-time exchange rates.

## Features
- Convert currencies using live exchange rates from `fixer.io`
- User-friendly web interface
- Backend API built with Flask
- Frontend built with HTML, CSS, and JavaScript

## Technologies Used
- **Backend:** Python (Flask), `requests` for fetching exchange rates
- **Frontend:** HTML, CSS, JavaScript
- **API Provider:** [Fixer.io](https://fixer.io/)

## Installation & Setup
### Prerequisites
- Python 3.x installed
- Flask installed (`pip install flask`)

### 1. Clone the Repository
```sh
git clone https://github.com/yourusername/currency-converter.git
cd currency-converter
```

### 2. Install Dependencies
```sh
pip install -r requirements.txt
```

### 3. Set Up Fixer.io API Key
- Sign up at [Fixer.io](https://fixer.io/) to get a free API key.
- Open `app.py` and replace `YOUR_ACCESS_KEY` with your actual API key.

### 4. Run the Flask Server
```sh
python app.py
```
- The server will start at `http://127.0.0.1:5000/`

## API Endpoints
### Convert Currency
**Endpoint:** `/convert`  
**Method:** `POST`  
**Request Body (JSON):**
```json
{
    "from_currency": "USD",
    "to_currency": "INR",
    "amount": 100
}
```
**Response (JSON):**
```json
{
    "result": "100 USD = 7420 INR"
}
```

## Usage
1. Open `index.html` in a browser.
2. Enter the source and target currency codes (e.g., USD, INR).
3. Enter the amount and click **Convert**.
4. The converted amount will be displayed.

## Troubleshooting
### "Error: Unable to fetch data. Check server connection."
- Ensure Flask is running: `python app.py`
- Check the browser console (`Ctrl + Shift + J`) for errors.
- Update `fetch('http://127.0.0.1:5000/convert')` in JavaScript.
- Restart Flask and reload the page.

## Contributing
Feel free to fork the repository, submit pull requests, or suggest improvements.

## License
This project is licensed under the MIT License.

---
### Contact
For any issues or suggestions, reach out via GitHub Issues.

