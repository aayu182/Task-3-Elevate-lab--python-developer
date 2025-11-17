import requests
from bs4 import BeautifulSoup

def scrape_headlines(url):
    try:
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
        }

        response = requests.get(url, headers=headers)

        if response.status_code != 200:
            print("Failed to fetch page. Status Code:", response.status_code)
            return []

        soup = BeautifulSoup(response.text, "html.parser")

        # Extract headlines (h2 tags for most news sites)
        headlines = soup.find_all("h2")

        extracted = [h.text.strip() for h in headlines if h.text.strip()]

        return extracted

    except Exception as e:
        print("Error occurred:", e)
        return []


def save_to_file(headlines, filename="headlines.txt"):
    with open(filename, "w", encoding="utf-8") as file:
        for h in headlines:
            file.write(h + "\n")
    print(f"Saved {len(headlines)} headlines to {filename}")


if __name__ == "__main__":
    URL = "https://www.bbc.com/news"   # You can change to any news website

    print("Scraping top news headlines...")
    headlines = scrape_headlines(URL)

    if headlines:
        save_to_file(headlines)
        print("Done!")
    else:
        print("No headlines found.")
