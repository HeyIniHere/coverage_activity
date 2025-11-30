from flask import Flask, request, jsonify

app = Flask(__name__)

EXCHANGE_RATE = 0.9  # USD → EUR

def usd_to_eur(amount: float) -> float:
    return round(amount * EXCHANGE_RATE, 2)


@app.route("/convert/usd-to-eur")
def convert():
    amount_str = request.args.get("amount", "")
    try:
        amount = float(amount_str)
    except ValueError:
        return jsonify({"error": "Invalid amount"}), 400

    eur = usd_to_eur(amount)
    return jsonify({"usd": amount, "eur": eur}), 200


@app.route("/check/temperature")
def check_temperature():
    value = request.args.get("value", "")

    try:
        temp = float(value)
    except ValueError:
        return jsonify({"error": "Invalid temperature"}), 400

    if temp >= 25:
        status = "hot"
    else:
        status = "cold"

    return jsonify({"temperature": temp, "status": status}), 200


if __name__ == "__main__":
    app.run(debug=True)
