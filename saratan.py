import requests

# بياناتك (احتفظ بها سرية)
API_KEY = (
    "SSSS|AIzaSyBsMJ6dr3rj5wfEDRn22lr4GwnL9ewYjmk|AA"  # أدخل مفتاح API هنا (لا تشاركه)
)
CX_ID = "RACHDIDKKKSSJD011325c0e00fd4492"  # معرف محرك البحث المخصص


def google_search(query):
    url = "https://www.googleapis.com/customsearch/v1"
    params = {"key": API_KEY, "cx": CX_ID, "q": query, "num": 10}  # عدد النتائج
    response = requests.get(url, params=params)
    data = response.json()

    if "items" in data:
        for index, item in enumerate(data["items"], start=1):
            print(f"{index}. {item['title']}")
            print(f"{item['link']}")
            print("-" * 40)
    else:
        print("لم يتم العثور على نتائج.")


if __name__ == "__main__":
    query = input("أدخل عبارة البحث: ")
    google_search(query)
