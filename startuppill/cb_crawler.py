import requests
from bs4 import BeautifulSoup
from collections import namedtuple
import csv


class CBCrawler:
    def __init__(self, path, headers) -> None:
        self.data = path
        self.headers = headers

    # @staticmethod
    # def _parse_csv(data):
    #     pass


    @staticmethod
    def _load_page(link):
        PAYLOAD = {"Content-Type": "text/html; charset=UTF-8"}
        target_url = link
        r = requests.get(target_url, headers=PAYLOAD)
        html = r.text
        return BeautifulSoup(html, "lxml")

    @staticmethod
    def _scrape_ranking(soup_data):
        pass

    @staticmethod
    def _scrape_total_funding(soup_data):
        pass

    def get_rank(self):
        # csv_data = self._parse_csv(self.data)
        # page = self._load_page(csv_data)
        # cb_data = self._scrape_page(page)

        cb_set = set()
        CrunchBase = namedtuple(
            "CrunchBase", ["name", "link", "ranking", "total_funding"]
        )
        with open(self.data, "r") as file:
            cb_data = [line for line in file][1:]
            for cb_item in cb_data:
                cb_name = cb_item.split(",")[0]
                cb_url = cb_item.split(",")[1]
                print(self._load_page(cb_url))
                cb_ranking = self._scrape_ranking(self._load_page(cb_url))
                cb_total_funding = self._scrape_total_funding(self._load_page(url))
                # cb_set.add(CrunchBase())

        return cb_set

    def export_to_csv(self):
        pass


if __name__ == "__main__":
    headers = ["name", "cb_rank", "total_funding_amount"]
    CBCrawler("results.csv", headers).get_rank()
