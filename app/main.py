from flask import Flask, jsonify
from scraper import scrape_gumtree

app = Flask(__name__)

@app.route("/")
def home():
    return "✅ HavenWA API with live Gumtree data"

@app.route("/api/listings")
def get_listings():
    listings = scrape_gumtree()
    return jsonify(listings)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
