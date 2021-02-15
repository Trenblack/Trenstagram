from urllib.request import urlopen
from bs4 import BeautifulSoup
from json import loads


def scrape(username: str) -> dict:

    with urlopen(f"https://www.instagram.com/{username}/") as response:
        soup = BeautifulSoup(response.read(), "html.parser")

    images = [link.get("content") for link in soup.find_all("meta")
              if link.get("property") == "og:image"]

    bios = [new_soup["description"] for script in soup.find_all("script")
            if script.get("type") == "application/ld+json"
            and "description" in (new_soup := loads(script.encode_contents()))]

    return dict(username=username,
                bio=bios[0] if len(bios) else None,
                images=images[0] if len(images) else None)
