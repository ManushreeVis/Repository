import requests

from flask import Flask, jsonify, render_template

def fetch_random_quote():
    """Fetch a random quote from the quotable API."""
    response = requests.get("https://api.quotable.io/random", verify=False)

    if response.status_code == 200:
        data = response.json()
        return data.get("content"), data.get("author")
    else:
        print("Failed to fetch quote!")
        return None, None


app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/quote")
def get_quote():
    """Return a random quote as JSON.

    Ensures the returned object is JSON serializable (dict with keys 'quote' and 'author').
    """
    quote, author = fetch_random_quote()
    if quote is None or author is None:
        return jsonify({"error": "failed to fetch quote"}), 502

    # Return a JSON-serializable dict (not a set)
    return jsonify({"quote": quote, "author": author})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)
