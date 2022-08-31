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
        cb_set = set()
        CrunchBase = namedtuple(
            "CrunchBase", ["name", "link", "ranking", "total_funding"]
        )
        with open(data, "r") as file:
            # cb_data = [line.split(",")[1] for line in file][1:]
            cb_data = [line for line in file][1:]
            # print(
            #     [(cb_item.split(",")[0], cb_item.split(",")[1]) for cb_item in cb_data]
            # )
            # cb_links.append(start_urls)
            for cb_item in cb_data:
                cb_set.add(CrunchBase(cb_item.split(",")[0], cb_item.split(",")[1]))

        return cb_set

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
