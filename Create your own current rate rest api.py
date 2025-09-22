from flask import Flask, jsonify
from bs4 import BeautifulSoup
import requests

app = Flask(__name__)

HEADERS = {
    "User-Agent": "Mozilla/5.0",
    "Accept-Language": "en-US,en;q=0.9"
}

def exchange_rates(in_cur, out_cur):
    # Per-1 rate (you multiply by amount later)
    url = f"https://www.x-rates.com/calculator/?from={in_cur}&to={out_cur}&amount=1"
    r = requests.get(url, headers=HEADERS, timeout=10)
    r.raise_for_status()

    soup = BeautifulSoup(r.content, "html.parser")
    el = soup.find("span", class_="ccOutputRslt")
    if not el:
        # Helpful hint printed to your console to see what you actually got
        print("DEBUG: .ccOutputRslt not found. First 200 bytes:", r.text[:200])
        raise ValueError("Rate element not found on the page (blocked/changed markup).")

    raw_text = el.get_text()               # e.g. "0,91 EUR" or "88.070821 INR"
    # --- normalise for float() ---
    txt = raw_text.replace("\xa0", " ")    # NBSP -> space
    token = txt.split()[0]                 # first token before the unit
    # keep digits and separators, then handle comma vs dot
    token = "".join(ch for ch in token if ch.isdigit() or ch in ".,-")
    if "," in token and "." not in token:
        token = token.replace(",", ".")    # comma used as decimal
    else:
        token = token.replace(",", "")     # comma as thousands separator

    rate_per_1 = float(token)
    return rate_per_1

@app.route("/")
def home():
    return '<h1>Currency Rate API</h1><p>Example URL: /api/v1/usd_eur_100</p>'

@app.route("/api/v1/<in_cur>_<out_cur>_<amount>")
def currency_input_output(in_cur, out_cur, amount):
    try:
        amt = float(amount)
    except ValueError:
        return jsonify({"error": "amount must be numeric"}), 400

    try:
        rate = exchange_rates(in_cur, out_cur)
    except requests.RequestException as e:
        # Network/HTTP issue
        return jsonify({"error": "Upstream request failed", "details": str(e)}), 502
    except Exception as e:
        # Parsing/any other issue
        return jsonify({"error": str(e)}), 502

    converted = rate * amt
    return jsonify({
        "from_currency": in_cur,
        "to_currency": out_cur,
        "exchange_rate": rate,              # per 1 <in_cur>
        "amount_to_convert": amt,
        "amount_after_conversion": converted
    }), 200

if __name__ == "__main__":
    app.run(debug=True)
