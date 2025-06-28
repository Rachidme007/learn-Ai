import time

import requests
from bs4 import BeautifulSoup

visited = set()
found_links = []


def duckduckgo_search(dork, max_pages=3):
    base_url = "https://duckduckgo.com/html/"
    links = []

    for page in range(max_pages):
        params = {"q": dork, "s": page * 50}
        try:
            r = requests.get(base_url, params=params, timeout=10)
            r.raise_for_status()
            soup = BeautifulSoup(r.text, "html.parser")
            results = soup.find_all("a", class_="result__a")

            if not results:
                break

            for a in results:
                href = a.get("href")
                if href and href.startswith("http"):
                    links.append(href)
            time.sleep(1)
        except Exception as e:
            print(f"Error fetching search results: {e}")
            break

    return links


def crawl(site_url, keywords):
    if site_url in visited:
        return
    visited.add(site_url)

    print(f"[+] Visiting: {site_url}")

    try:
        r = requests.get(site_url, timeout=10)
        r.raise_for_status()

        page_text = r.text.lower()
        for keyword in keywords:
            if keyword.lower() in page_text:
                print(f" => Found keyword '{keyword}' at {site_url}")
                found_links.append((site_url, keyword))
                break
    except Exception as e:
        print(f"Error visiting {site_url} -- {e}")


# ======= الإعدادات =======

sites = [
    "mega.nz",
    "mediafire.com",
    "anonfiles.com",
    "gofile.io",
    "zippyshare.com",
    "dropmefiles.com",
    "send.cm",
    "uploadfiles.io",
    "file.io",
    "transfer.sh",
    "ufile.io",
    "cloud.mail.ru",
    "1fichier.com",
    "filefactory.com",
    "rapidgator.net",
    "uploadhaven.com",
    "bayfiles.com",
    "tusfiles.com",
    "racaty.net",
    "pixeldrain.com",
    "files.fm",
]

keywords_for_search = ["password", "config", "backup"]

# توليد dorks
dorks = []
for site in sites:
    for keyword in keywords_for_search:
        dorks.append(f"site:{site} {keyword}")

print(f"\n==== بدء البحث باستخدام dorks ====\n")

for dork in dorks:
    print(f"\n==== البحث عن dork: {dork} ====\n")
    visited.clear()
    found_links.clear()

    result_links = duckduckgo_search(dork)

    print(f"[!] تم جمع {len(result_links)} رابط من DuckDuckGo.\n")

    for link in result_links:
        crawl(link, keywords_for_search)
        time.sleep(1)

    print(f"\n==== نتائج البحث للدورك: {dork} ====\n")
    if found_links:
        for url, kw in found_links:
            print(f"URL: {url} (وجدت كلمة: '{kw}')")
    else:
        print("لا توجد نتائج تحتوي الكلمات المفتاحية.")

print("\n==== البحث انتهى ====\n")
