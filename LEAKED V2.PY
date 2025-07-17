import os

import requests


def search_leaked_tools_and_save_source(query, save_directory, filename):
    base_url = "https://leaked.tools"
    search_url = f"{base_url}/search?q={query}"

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8",
        "Referer": base_url,
        "Accept-Language": "en-US,en;q=0.9",
    }

    print(f"\n--- إرسال استعلام البحث إلى leaked.tools عن: '{query}' ---")

    try:
        response = requests.get(search_url, headers=headers, timeout=20)
        response.raise_for_status()

        html_content = response.text

        os.makedirs(save_directory, exist_ok=True)
        full_path = os.path.join(save_directory, filename)

        with open(full_path, "w", encoding="utf-8") as file:
            file.write(html_content)

        print(f"\n✅ تم حفظ صفحة النتائج في الملف:\n{full_path}")

    except Exception as e:
        print(f"\n❌ حدث خطأ: {e}")


# ==========================================
# مسار ثابت
SAVE_DIRECTORY = r"C:\Users\WIN\Documents\learn Ai"
# ==========================================

if __name__ == "__main__":
    print("Welcome to the Leaked.tools Search Script!")

    while True:
        search_term = input("\nاكتب عبارة البحث (أو 'exit' للخروج): ")
        if search_term.lower() == "exit":
            break
        elif not search_term.strip():
            print("الرجاء إدخال عبارة بحث صحيحة.")
            continue

        filename = input("اكتب اسم الملف مع .html أو .txt لحفظ النتائج: ").strip()
        if not filename:
            print("الرجاء إدخال اسم ملف صحيح.")
            continue

        search_leaked_tools_and_save_source(search_term, SAVE_DIRECTORY, filename)

    print("\nشكراً لاستخدامك السكربت. إلى اللقاء!")
