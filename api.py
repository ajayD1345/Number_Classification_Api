import os
from flask import Flask, request, jsonify
from flask_cors import CORS
import requests
from number_utils import is_prime, is_armstrong, is_perfect, digit_sum, get_parity

app = Flask(__name__)
CORS(app)  # Enable Cross-Origin Resource Sharing

@app.route('/api/classify-number', methods=['GET'])
def classify_number():
    num_str = request.args.get('number')

    # Ensure the response is always JSON
    response_headers = {"Content-Type": "application/json"}

    # Validate input and allow negative numbers
    try:
        number = float(num_str)  # Accept float values
        if number.is_integer():  # Convert valid floats (e.g., 4.0 -> 4)
            number = int(number)
        else:
            return jsonify({"number": num_str, "error": "Only integer values are supported."}), 400
    except (ValueError, TypeError):
        return jsonify({"number": num_str, "error": "Invalid input. Please enter a valid number."}), 400

    # Compute properties using helper functions
    prime_status = is_prime(number)
    armstrong_status = is_armstrong(number)
    perfect_status = is_perfect(number)
    sum_of_digits = digit_sum(number)
    parity = get_parity(number)

    properties = ["armstrong", parity] if armstrong_status else [parity]

    # Fetch a fun fact from Numbers API
    fun_fact = ""
    try:
        fact_response = requests.get(f"http://numbersapi.com/{number}/math?json", timeout=3)
        if fact_response.status_code == 200:
            fact_data = fact_response.json()
            fun_fact = fact_data.get("text", "")
    except Exception:
        fun_fact = "Fun fact not available at the moment."

    # Ensure fun_fact comes last in JSON
    result = {
        "number": number,
        "is_prime": prime_status,
        "is_perfect": perfect_status,
        "properties": properties,
        "digit_sum": sum_of_digits,
        "fun_fact": fun_fact  # Moved to the end
    }

    return jsonify(result), 200, response_headers

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
