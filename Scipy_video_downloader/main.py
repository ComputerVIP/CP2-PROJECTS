#https://docs.scrapy.org/en/latest/topics/spiders.html

#TO RUN THIS!
#cd C:\Users\***\Downloads\CP2-PROJECTS\Scipy_video_downloader IN THE TERMINAL HERE
#python -m scrapy runspider main.py TO MAKE SURE IT RUNS THROUGH PYTHON, ELSE IT WILL NOT WORK
#THEN DOWNLOAD "Live Preview" BY MICROSOFT TO PREVIEW HTML FILES

#python -m scrapy startproject video_scraper


from pathlib import Path

import scrapy


class QuotesSpider(scrapy.Spider):
    name = "quotes"

    def start_requests(self):
        urls = [
            "https://www.nationalgeographic.com/history/history-magazine/article/infamous-missouri-outlaw-jesse-james?rid=43177150C295DEB2D967AAD61A2EB054&cmpid=org=ngp::mc=crm-email::src=ngp::cmp=editorial::add=Daily_NL_Monday_History_20250317"
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        page = response.url.split("/")[-2]
        filename = f"quotes-{page}.html"
        Path(filename).write_bytes(response.body)
        self.log(f"Saved file {filename}")