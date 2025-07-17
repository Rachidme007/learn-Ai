def extract_links_from_saved_file(filepath):
    """
    Reads an HTML file, extracts specific href values, constructs full URLs, and prints them.
    """
    base_url = "https://leaked.tools/"
    extracted_links = []

    try:
        with open(filepath, "r", encoding="utf-8") as file:
            html_content = file.read()

        search_pattern = "href='"
        end_pattern = "' target"

        index = 0
        while True:
            start_index = html_content.find(search_pattern, index)
            if start_index == -1:
                break  # انتهى البحث

            start_index += len(search_pattern)
            end_index = html_content.find(end_pattern, start_index)
            if end_index == -1:
                break  # لم يتم العثور على نهاية

            link_part = html_content[start_index:end_index].strip()

            # إزالة أي شرطات مائلة زائدة (اختياري حسب التنسيق)
            if link_part.startswith("/"):
                link_part = link_part[1:]

            full_url = base_url + link_part
            extracted_links.append(full_url)

            index = end_index + len(end_pattern)  # متابعة البحث

        if extracted_links:
            print("\n✅ روابط مستخرجة:")
            for url in extracted_links:
                print(url)
        else:
            print("\n❌ لم يتم العثور على أي روابط باستخدام النمط المحدد.")

    except Exception as e:
        print(f"\n❌ فشل أثناء قراءة الملف أو المعالجة: {e}")

    return extracted_links
