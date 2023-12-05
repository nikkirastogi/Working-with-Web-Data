import requests
from bs4 import BeautifulSoup
import pandas as pd

class SitemapParser:
    def __init__(self, base_url):
        self.base_url = base_url
        self.sitemaps = []

    def fetch_robots_txt(self):
        robots_url = f"{self.base_url}/robots.txt"
        response = requests.get(robots_url)
        if response.status_code == 200:
            return response.text
        else:
            print(f"Failed to fetch robots.txt. Status code: {response.status_code}")
            return None

    def extract_sitemaps(self):
        robots_txt = self.fetch_robots_txt()
        sitemap_lines = [line.strip() for line in robots_txt.split('\n') if line.strip().lower().startswith('sitemap:')]
        self.sitemaps = [line.split(': ', 1)[1] for line in sitemap_lines]
        return self.sitemaps
    
    def parse_sitemaps_to_dataframe(self):
        all_data = []
        for sitemap_url in self.sitemaps:
            response = requests.get(sitemap_url)
            if response.status_code == 200:
                soup = BeautifulSoup(response.text, 'xml')
                # Assuming XML structure, modify accordingly if it's different
                urls = soup.find_all('url')
                data = {
                    'url': [url.find('loc').text for url in urls],
                    'last_modified': [url.find('lastmod').text if url.find('lastmod') else None for url in urls]
                }
                all_data.append(pd.DataFrame(data))

        if all_data:
            return pd.concat(all_data)
        else:
            return None
    """
    def run(self):
        robots_txt = self.fetch_robots_txt()
        if robots_txt:
            self.extract_sitemaps()
            df = self.parse_sitemaps_to_dataframe()
            return df
    """
    def run(self):
        pd.set_option('display.max_rows', 100)  # Set the option to display all rows
        robots_txt = self.fetch_robots_txt()
        if robots_txt:
            self.extract_sitemaps()
            df = self.parse_sitemaps_to_dataframe()
            return df
