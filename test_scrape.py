import unittest
from pathlib import Path

from scraper import scrape


class ScrapeTestCase(unittest.TestCase):
    def test_scrape(self):
        data = scrape(Path('testdata.csv'), True)
        print(data)


if __name__ == '__main__':
    unittest.main()
