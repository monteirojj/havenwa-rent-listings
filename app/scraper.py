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

        for card in soup.select("article[data-testid='listing-card']")[:10]:
            title_tag = card.select_one("h3[data-testid='listing-title']")
            price_tag = card.select_one("span[data-testid='listing-price']")
            link_tag = card.find("a", href=True)

            title = title_tag.get_text(strip=True) if title_tag else "N/A"
            price = price_tag.get_text(strip=True) if price_tag else "N/A"
            link = f"https://www.gumtree.com.au{link_tag['href']}" if link_tag else "#"

            listings.append({
                "title": title,
                "price": price,
                "link": link
            })

        return listings

    except Exception as e:
        return [{"error": f"Scraping failed: {str(e)}"}]
