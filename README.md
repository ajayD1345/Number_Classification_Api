# Number_Classification_Api

## Overview

The **Number_Classification_Api** is a simple RESTful service that accepts an integer as input and returns interesting mathematical properties of that number. The API determines if the number is:
- **Prime**
- **An Armstrong number** (narcissistic number)
- **A Perfect number** (equal to the sum of its proper divisors)
- Its **digit sum**
- Its **parity** (odd or even)

In addition, the API retrieves a fun math fact from the [Numbers API](http://numbersapi.com).

## Features

- **Prime Check:** Verifies if the number is a prime.
- **Armstrong Check:** Determines if the number is an Armstrong (narcissistic) number.
- **Perfect Check:** Checks if the number is perfect.
- **Digit Sum:** Calculates the sum of all the digits.
- **Parity:** Identifies if the number is odd or even.
- **Fun Fact:** Fetches a fun mathematical fact using an external API.
- **CORS Enabled:** Configured to support Cross-Origin Resource Sharing (CORS).
- **JSON Responses:** All responses are returned in JSON format.
- **Error Handling:** Returns meaningful error messages with appropriate HTTP status codes for invalid inputs.

## Technology Stack

- **Language:** Python 3.x
- **Framework:** Flask
- **HTTP Client:** requests
- **CORS:** flask_cors
- **Version Control:** Git & GitHub

## Getting Started

Follow these instructions to set up the project locally.

### Prerequisites

- Python 3.x installed on your machine
- `pip` package manager

### Installation

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/yourusername/number-classification-api.git
   cd number-classification-api
   ```
2. **Set Up a Virtual Environment (Recommended):**

   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows, use: venv\Scripts\activate
   ```
3. **Install Dependencies:**

   Ensure you have a requirements.txt file with the following (or similar) content:

   ```text
   Flask
   flask_cors
   requests
   ```
   Then run:

   ```bash
   pip install -r requirements.txt
   ```

### Running the API Locally

1. **Start the Flask Server:**

   ```bash
   python api.py
   ```
2. **Access the API:**

   The API should now be running on http://localhost:5000. You can test the endpoint using your browser or tools like curl or Postman.

   Example Request:

   ```bash
   curl "http://localhost:5000/api/classify-number?number=371"
   ```
   Expected JSON Response:

   ```json
   {
       "number": 371,
       "is_prime": false,
       "is_perfect": false,
       "properties": ["armstrong", "odd"],
       "digit_sum": 11,
       "fun_fact": "371 is an Armstrong number because 3^3 + 7^3 + 1^3 = 371"
   }
   ```

### API Specification

## Endpoint
   GET /api/classify-number?number=<number>

## Query Parameters
   - number (required): An integer value that will be classified

## Success Response (HTTP 200)
   ```json
   {
      "number": 371,
      "is_prime": false,
      "is_perfect": false,
      "properties": ["armstrong", "odd"],
      "digit_sum": 11,
      "fun_fact": "371 is an Armstrong number because 3^3 + 7^3 + 1^3 = 371"
   }
   ```
## Error Response (HTTP 400)
   If the number parameter is missing or invalid:

   ```json
   {
      "number": "invalid_input",
      "error": true
   }
   ```

### Deployment

   This API can be deployed to any cloud hosting platform that supports Python (such as Heroku, Render, or AWS). The application reads the port from the environment variable PORT, making it deployment-ready.
   For example, on Heroku, the application will automatically use the port provided by the platform.

   **Public Endpoint:**
   Once deployed, the API will be available at a public URL (e.g., https://your-deployed-app.herokuapp.com).

### Testing
   Be sure to test the API thoroughly:

   - Use valid integer inputs.
   - Test boundary cases (e.g., 0, 1, negative numbers).
   - Try invalid inputs (e.g., alphabetic strings) to confirm error handling.

### Contributing
   Contributions are welcome! Please fork the repository and submit a pull request with your enhancements. For major changes, please open an issue first to discuss your ideas.

### License
   This project is licensed under the MIT License.

### Contact
   For any inquiries, please contact [your-email@example.com].



