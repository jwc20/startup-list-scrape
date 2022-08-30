import requests
from bs4 import BeautifulSoup
from collections import namedtuple
import csv


class Scraper:
    def __init__(self, path) -> None:
        self.data = path

    @staticmethod
    def _load_page(url):
        PAYLOAD = {"Content-Type": "text/html; charset=UTF-8"}
        target_url = url
        r = requests.get(target_url, headers=PAYLOAD)
        html = r.text
        # print(html)
        return BeautifulSoup(html, "lxml")

    @staticmethod
    def _scrape_startups(soup_data):
        StartUp = namedtuple("StartUp", ["name", "crunchbase_url", "description"])

        div_entry_content = soup_data.find("div", {"class": "entry-content g1-typography-xl"})
        div_startup_cards = div_entry_content.find_all("div", {"class": "wp-block-cover alignwide has-black-background-color has-background-dim is-position-center-center"})

        for card in div_startup_cards:
            startup_name = card.find("h3").text
            # print(startup_name)
            startup_crunchbase_url = card.a["href"]
            print(startup_crunchbase_url)

        return div_startup_cards



    def get_startups(self):
        page = self._load_page(self.data)
        data = self._scrape_startups(page)
        # print(data)


    def export_data_to_csv():
        pass

if __name__ == "__main__":
    url = "https://startupill.com/101-best-california-business-intelligence-startups-innovating-data-led-decisions/"
    Scraper(url).get_startups()
