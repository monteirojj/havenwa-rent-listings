import requests
from bs4 import BeautifulSoup

def scrape_gumtree():
    url = "https://www.gumtree.com.au/s-property-for-rent/perth/c18364l3008303"
    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    try:
        response = requests.get(url, headers=headers, timeout=10)
        soup = BeautifulSoup(response.text, "html.parser")

        listings = []
        cards = soup.select("a.listing-link")  # Fallback selector for listing links

        for card in cards[:10]:  # Limit to 10 for speed
            title_tag = card.select_one("span.title")
            price_tag = card.select_one("span.price")
            title = title_tag.get_text(strip=True) if title_tag else "N/A"
            price = price_tag.get_text(strip=True) if price_tag else "N/A"
            link = f"https://www.gumtree.com.au{card['href']}" if card.has_attr("href") else "#"

            listings.append({
                "title": title,
                "price": price,
                "link": link
            })

        # If nothing was scraped, return diagnostic info
        if not listings:
            return [{"error": "No listings found. Gumtree may have blocked the server or changed layout."}]

        return listings

    except Exception as e:
        return [{"error": f"Scraping failed: {str(e)}"}]
