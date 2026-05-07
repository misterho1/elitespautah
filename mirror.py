"""Mirror elitespautah.com from Squarespace to local static files.

Fetches sitemap.xml, downloads each page, saves as <slug>.html at repo root,
and copies home.html to index.html so / works.
"""
import os
import re
import sys
import urllib.request
import urllib.error
from xml.etree import ElementTree as ET

UA = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0 Safari/537.36"
BASE = "https://www.elitespautah.com"
OUT_DIR = os.path.dirname(os.path.abspath(__file__))


def fetch(url: str) -> bytes:
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    with urllib.request.urlopen(req, timeout=30) as r:
        return r.read()


def get_sitemap_urls() -> list[str]:
    raw = fetch(f"{BASE}/sitemap.xml")
    ns = {"sm": "http://www.sitemaps.org/schemas/sitemap/0.9"}
    root = ET.fromstring(raw)
    return [loc.text for loc in root.iterfind(".//sm:loc", ns) if loc.text]


def slug_from_url(url: str) -> str:
    path = url.rstrip("/").split("/")[-1]
    return path or "home"


def save_page(url: str) -> tuple[str, bool]:
    slug = slug_from_url(url)
    try:
        html = fetch(url)
    except urllib.error.HTTPError as e:
        return slug, False
    path = os.path.join(OUT_DIR, f"{slug}.html")
    with open(path, "wb") as f:
        f.write(html)
    return slug, True


def main():
    print("Fetching sitemap...")
    urls = get_sitemap_urls()
    print(f"Found {len(urls)} URLs in sitemap")

    saved = []
    failed = []
    for url in urls:
        slug, ok = save_page(url)
        if ok:
            saved.append(slug)
            print(f"  saved {slug}.html")
        else:
            failed.append(url)
            print(f"  FAILED {url}")

    # Try a few extra pages that aren't in sitemap but appear in nav
    for slug in ["services", "cart"]:
        try:
            html = fetch(f"{BASE}/{slug}")
            with open(os.path.join(OUT_DIR, f"{slug}.html"), "wb") as f:
                f.write(html)
            saved.append(slug)
            print(f"  saved {slug}.html (off-sitemap)")
        except urllib.error.HTTPError:
            pass

    # Copy home.html to index.html so / works
    home_path = os.path.join(OUT_DIR, "home.html")
    if os.path.exists(home_path):
        with open(home_path, "rb") as f:
            home = f.read()
        with open(os.path.join(OUT_DIR, "index.html"), "wb") as f:
            f.write(home)
        print("  copied home.html -> index.html")

    print(f"\nDone. {len(saved)} pages saved, {len(failed)} failed.")
    if failed:
        for u in failed:
            print(f"  failed: {u}")


if __name__ == "__main__":
    main()
