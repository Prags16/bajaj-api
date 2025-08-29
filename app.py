
from flask import Flask, request, jsonify

app = Flask(__name__)

# === YOUR DETAILS (EDIT THESE 4 LINES) ===
FULL_NAME = "pragnya_neerukonda"      # full name in lowercase with underscore, e.g., "john_doe"
DOB_DDMMYYYY = "16112004"   # date of birth in ddmmyyyy format, e.g., "17091999"
EMAIL = "pragnyaneerukonda@gmail.com"
ROLL_NUMBER = "22BCE7277"
# =========================================

@app.route('/bfhl', methods=['POST'])
def bfhl():
    try:
        body = request.get_json(silent=True) or {}
        items = body.get("data", [])
        if not isinstance(items, list):
            return jsonify({"is_success": False, "error": "'data' must be a list"}), 400

        odd_numbers = []
        even_numbers = []
        alphabets = []
        special_characters = []
        total_sum = 0

        # For concat_string: collect ALL alphabetic characters from every item
        letters_for_concat = []

        for item in items:
            s = str(item)

            # accumulate alphabetic characters for concat_string (from anywhere)
            for ch in s:
                if ch.isalpha():
                    letters_for_concat.append(ch)

            if s.isdigit():
                n = int(s)
                total_sum += n
                (even_numbers if n % 2 == 0 else odd_numbers).append(s)
            elif s.isalpha():
                alphabets.append(s.upper())
            else:
                special_characters.append(s)

        # build concat_string: reverse all collected letters, then alternating caps
        alpha_reversed = ''.join(letters_for_concat)[::-1]
        concat_string = ''.join(
            ch.upper() if i % 2 == 0 else ch.lower()
            for i, ch in enumerate(alpha_reversed)
        )

        response = {
            "is_success": True,
            "user_id": f"{FULL_NAME}_{DOB_DDMMYYYY}",
            "email": EMAIL,
            "roll_number": ROLL_NUMBER,
            "odd_numbers": odd_numbers,
            "even_numbers": even_numbers,
            "alphabets": alphabets,
            "special_characters": special_characters,
            "sum": str(total_sum),
            "concat_string": concat_string
        }
        return jsonify(response), 200

    except Exception as e:
        return jsonify({"is_success": False, "error": str(e)}), 500


@app.route('/', methods=['GET'])
def health():
    return jsonify({"status": "ok", "message": "Use POST /bfhl"}), 200


if __name__ == '__main__':
    # Local dev
    app.run(host='0.0.0.0', port=5000, debug=True)
