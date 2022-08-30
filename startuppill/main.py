import requests
from bs4 import BeautifulSoup
from collections import namedtuple
import csv


class Scraper:
    def __init__(self, path, headers) -> None:
        self.url = path
        self.headers = headers

    @staticmethod
    def _load_page(url: str) -> BeautifulSoup:
        PAYLOAD = {"Content-Type": "text/html; charset=UTF-8"}
        target_url = url
        r = requests.get(target_url, headers=PAYLOAD)
        html = r.text
        # print(html)
        return BeautifulSoup(html, "lxml")

    @staticmethod
    def _scrape_startups(soup_data) -> set:
        StartUp = namedtuple(
            "StartUp",
            ["name", "crunchbase_url", "website_url", "linked_url", "description"],
        )
        results = set()

        div_entry_content = soup_data.find(
            "div", {"class": "entry-content g1-typography-xl"}
        )
        div_startup_cards = div_entry_content.find_all(
            "div",
            {
                "class": "wp-block-cover alignwide has-black-background-color has-background-dim is-position-center-center"
            },
        )

        for card in div_startup_cards:
            startup_name = card.find("h3").text
            startup_crunchbase_url = card.a["href"]
            startup_url = card.find_all("a")[1]["href"]
            startup_linkedin_url = card.find_all("a")[4]["href"]
            startup_description = card.find_all("p")[1].text
            results.add(
                StartUp(
                    startup_name,
                    startup_crunchbase_url,
                    startup_url,
                    startup_linkedin_url,
                    startup_description,
                )
            )

        return results

    def get_startups(self) -> set:
        page = self._load_page(self.url)
        data = self._scrape_startups(page)
        # print(len(data))
        return data

    def export_data_to_csv(self) -> None:
        with open("results.csv", "w+", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(self.headers)
            results = self.get_startups()
            # print(results)
            for name, crunchbase_url, website_url, linked_url, description in results:
                writer.writerow(
                    [name, crunchbase_url, website_url, linked_url, description]
                )


if __name__ == "__main__":
    url = "https://startupill.com/101-best-california-business-intelligence-startups-innovating-data-led-decisions/"
    headers = ["name", "crunchbase", "website", "linkedin", "description"]
    # Scraper(url).get_startups()
    Scraper(url, headers).export_data_to_csv()
