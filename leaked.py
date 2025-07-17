import requests
from bs4 import BeautifulSoup


def search_leaked_tools(query):
    url = f"https://leaked.tools/search?q={query}"

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8",
        "Referer": url,
    }

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()

        soup = BeautifulSoup(response.text, "html.parser")

        print(f"\n--- نتائج البحث في leaked.tools عن: {query} ---")

        results_found = False

        for link in soup.find_all("a", href=True):
            href = link["href"]
            text = link.get_text(strip=True)
            if text and "/search?q=" not in href:
                print(f"- {text}\n{href}\n")
                results_found = True

        if not results_found:
            print(
                "لم يتم العثور على نتائج مرئية (قد تحتاج تخصيص التحليل حسب بنية الموقع)."
            )

    except Exception as e:
        print(f"حدث خطأ أثناء الاتصال بـ leaked.tools : {e}")


if __name__ == "__main__":
    query = input("أدخل عبارة البحث في leaked.tools: ")
    search_leaked_tools(query)
