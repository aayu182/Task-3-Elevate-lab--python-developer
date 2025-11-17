# 📰 Web Scraper for News Headlines  
### Python Developer Internship – Task 3

This project is a simple **web scraper** that automatically extracts **top news headlines** from a public news website using:

- `requests`
- `BeautifulSoup4`

The script fetches the webpage, parses HTML, extracts `<h2>` tags (common for headlines), and saves them into a text file.

---

## 📌 Features
- Fetches HTML using HTTP GET request  
- Parses webpage using BeautifulSoup  
- Extracts news headlines  
- Saves headlines into `headlines.txt`  
- Fully customizable (change target URL)

---

## 🛠️ Technologies Used
- Python 3  
- requests  
- BeautifulSoup4 (bs4)

---

## 📂 Project Files
| File | Description |
|------|-------------|
| `news_scraper.py` | Main Python script that scrapes the headlines |
| `headlines.txt` | Output file containing extracted headlines |
| `README.md` | Documentation for GitHub |

---

## 🚀 How to Run the Script
### 1. Install required packages
```bash
pip install requests beautifulsoup4
2. Run the script
bash
Copy code
python news_scraper.py
Output will be saved in headlines.txt.
.

🧠 Interview Concepts Covered

HTTP GET request

Installing external packages

User-Agent in HTTP

soup.find_all() usage

Risks of web scraping

HTML tag basics

.text in BeautifulSoup

try–except block

HTTP status codes
```bash
pip install requests beautifulsoup4
