
# https://pypi.org/project/beautifulsoup4/

import requests
from bs4 import BeautifulSoup

URL = "https://en.wikipedia.org/wiki/Python_(programming_language)"

def get_h2_headers(url):
    
    headers = {
        "User-Agent" : (
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
            "AppleWebKit/537.36 (KHTML, like Gecko) "
            "Chrome/138.0.0.0 Safari/537.36" 
        )
    }
    
    try:
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()
    except requests.RequestException as e:
        print(f"Failed to fetch page : \n {e}")
        return []

    soup = BeautifulSoup(response.text, "html.parser")
    h2_tags = soup.find_all("h2")
    headers = [h2.get_text(strip=True) for h2 in h2_tags]
    return headers

headers = get_h2_headers(URL)
    

for header in headers:
    print(header)