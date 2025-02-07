# api.py

import os
from flask import Flask, request, jsonify
from flask_cors import CORS
import requests

# Import our core software logic
from number_utils import is_prime, is_armstrong, is_perfect, digit_sum, get_parity

app = Flask(__name__)
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True
CORS(app)

@app.route('/api/classify-number', methods=['GET'])
def classify_number():
    # Get the 'number' query parameter from the request URL
    num_str = request.args.get('number')

    # Validate input: ensure it can be converted to an integer
    try:
        number = int(num_str)
    except (ValueError, TypeError):
        return jsonify({"number": num_str, "error": True}), 400


    # use our core logic functions
    prime_status = is_prime(number)
    armstrong_status = is_armstrong(number)
    perfect_status = is_perfect(number)
    sum_of_digits = digit_sum(number)
    parity = get_parity(number)


    # Determine the 'properties' field
    if armstrong_status:
        properties = ["armstrong", parity]
    else:
        properties = [parity]


    # Call the Numbers API to get a fun math fact
    fun_fact = ""
    try:
         fact_response = requests.get(f"http://numbersapi.com/{number}/math?json", timeout=5)
         if fact_response.status_code == 200:
            fact_data = fact_response.json()
            fun_fact = fact_data.get("text", "")
    except Exception:
        fun_fact = "Fun fact not available at the moment." 


    # Create the response JSON
    result = {
        "number": number,
        "is_prime": prime_status,
        "is_perfect": perfect_status,
        "properties": properties,
        "digit_sum": sum_of_digits,
        "fun_fact": fun_fact
    }

    return jsonify(result), 200

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
