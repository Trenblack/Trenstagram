import requests, json
from bs4 import BeautifulSoup

def scrape_data(username):
    r = requests.get(f'https://www.instagram.com/{username}/')
    soup = BeautifulSoup(r.text, 'html.parser')
    data = {'username':username}

    for link in soup.find_all('meta'):
        prop = link.get('property')
        if prop == "og:image":
            data['image'] = link.get('content')
            break

    for script in soup.find_all('script'):
        if script.get('type') == 'application/ld+json':
            new_soup = json.loads(script.encode_contents())
            if "description" in new_soup:
                data['bio'] = new_soup['description']
            else:
                data['bio'] = ""
            break

    return data