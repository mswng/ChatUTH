import requests
from bs4 import BeautifulSoup

def crawl_data_from_url(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (compatible; ChatUTHBot/1.0; +http://yourdomain.com/bot)"
    }

    try:
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()
    except requests.RequestException as e:
        return {"error": str(e)}

    soup = BeautifulSoup(response.text, "html.parser")

    # Thu thập dữ liệu
    data = {
        "titles": [h.get_text(strip=True) for h in soup.find_all(['h1', 'h2', 'h3'])],
        "paragraphs": [p.get_text(strip=True) for p in soup.find_all("p")],
        "links": [{"text": a.get_text(strip=True), "href": a.get("href")} for a in soup.find_all("a", href=True)],
        "tables": []
    }

    # Thu thập bảng
    for table in soup.find_all("table"):
        rows = []
        for tr in table.find_all("tr"):
            cells = [td.get_text(strip=True) for td in tr.find_all(["td", "th"])]
            rows.append(cells)
        data["tables"].append(rows)

    return data
