import os
import time

import requests
from bs4 import BeautifulSoup


def download_gallery(gallery_url, save_folder="gallery_images"):
    headers = {"User-Agent": "Mozilla/5.0"}

    # Create directory if it doesn't exist
    if not os.path.exists(save_folder):
        os.makedirs(save_folder)

    print(f"[+] Accessing: {gallery_url}")
    response = requests.get(gallery_url, headers=headers)
    if response.status_code != 200:
        print("[-] Failed to access the gallery.")
        return

    soup = BeautifulSoup(response.text, "html.parser")

    # Get all gallery page links (thumb pages)
    gallery_page_links = []
    while True:
        thumbs = soup.select("div.gdtm a, div.gdtl a")
        gallery_page_links += [a["href"] for a in thumbs]
        # Check for "next" page
        next_button = soup.find("a", text=">")
        if next_button:
            next_url = next_button["href"]
            print(f"[~] Next page: {next_url}")
            response = requests.get(next_url, headers=headers)
            soup = BeautifulSoup(response.text, "html.parser")
            time.sleep(1)
        else:
            break

    print(f"[+] Found {len(gallery_page_links)} gallery pages.")

    for i, page_url in enumerate(gallery_page_links):
        print(f"[{i+1}/{len(gallery_page_links)}] Getting image from: {page_url}")
        try:
            r = requests.get(page_url, headers=headers)
            s = BeautifulSoup(r.text, "html.parser")
            img = s.select_one("#img")  # Main image ID
            if img and "src" in img.attrs:
                img_url = img["src"]
                img_data = requests.get(img_url, headers=headers).content
                img_name = os.path.join(
                    save_folder, f"{i+1:03d}_{os.path.basename(img_url)}"
                )
                with open(img_name, "wb") as f:
                    f.write(img_data)
                print(f"    Saved: {img_name}")
            else:
                print("    [-] Failed to find image.")
        except Exception as e:
            print(f"    [!] Error: {e}")
        time.sleep(1)

    print("[✓] Done downloading all images.")


# ========== USAGE ========== #
if __name__ == "__main__":
    gallery_input = input("Enter e-hentai gallery URL: ").strip()
    download_gallery(gallery_input)
