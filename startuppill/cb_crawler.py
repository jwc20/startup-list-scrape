import requests
from bs4 import BeautifulSoup
from collections import namedtuple
import csv


class CBCrawler:
    def __init__(self, path, headers) -> None:
        self.data = path
        self.headers = headers

    @staticmethod 
    def _parse_csv(data):
        cb_links = []
        with open(data, "r") as file:
            start_urls = [line.split(",")[1] for line in file][1:]
            print(start_urls)
            print(len(start_urls))
            cb_links.append(start_urls)
            
        return cb_links



    @staticmethod
    def _load_page(links):
        PAYLOAD = {"Content-Type": "text/html; charset=UTF-8"}

        for item in data:
            cb_url = item
            print(cb_url)

        target_url = url
        r = requests.get(target_url, headers=PAYLOAD)
        html = r.text
        return BeautifulSoup(html, "lxml")




    @staticmethod
    def _scrape_page():
        pass

    def get_rank(self):
        csv_data = self._parse_csv(self.data)
        page = self._load_page(csv_data)
        cb_data = self._scrape_page(page)

    def export_to_csv(self):
        pass


if __name__ == "__main__":
    headers = ["name", "cb_rank", "total_funding_amount"]
    CBCrawler("results.csv", headers).get_rank()
