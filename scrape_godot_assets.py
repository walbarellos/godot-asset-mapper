#!/usr/bin/env python3
import requests
from bs4 import BeautifulSoup
import json
import time

BASE_URL = "https://godotengine.org/asset-library/asset"
OUTPUT = "godot_assets.json"

def scrape_page(page=1):
    url = f"{BASE_URL}?page={page}&sort=updated"
    r = requests.get(url, timeout=15)
    if r.status_code != 200:
        print(f"⚠️ Erro {r.status_code} ao acessar {url}")
        return []
    soup = BeautifulSoup(r.text, "html.parser")
    assets = []
    for item in soup.select("li.asset-item"):
        header = item.select_one("a.asset-header")
        title = item.select_one(".asset-title")
        author = item.select_one(".asset-footer a")
        tags = item.select_one(".asset-tags-container")
        url_asset = header["href"] if header else None
        assets.append({
            "title": title.get_text(strip=True) if title else None,
            "author": author.get_text(strip=True) if author else None,
            "tags": tags.get_text(" ", strip=True) if tags else None,
            "url": f"https://godotengine.org{url_asset}" if url_asset else None
        })
    return assets, soup

def has_next_page(soup, page):
    nav = soup.select_one("ul.pagination")
    if not nav:
        return False
    active = nav.select_one("li.active")
    if not active:
        return False
    return active.find_next_sibling("li") is not None

def main():
    all_assets = []
    page = 1
    while True:
        print(f"🔎 Página {page}...")
        assets, soup = scrape_page(page)
        if not assets:
            break
        all_assets.extend(assets)
        if not has_next_page(soup, page):
            break
        page += 1
        time.sleep(1)
    print(f"✅ Total de assets coletados: {len(all_assets)}")
    with open(OUTPUT, "w", encoding="utf-8") as f:
        json.dump(all_assets, f, ensure_ascii=False, indent=2)
    print(f"📂 Relatório salvo em {OUTPUT}")

if __name__ == "__main__":
    main()
