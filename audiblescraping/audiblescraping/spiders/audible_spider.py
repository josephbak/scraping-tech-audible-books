import scrapy
from ..items import AudiblescrapingItem
from bs4 import BeautifulSoup
import requests

class AudibleSpider(scrapy.Spider):
    name = 'audible'
    page_number = 2

    start_urls = [
        "https://www.audible.com/search?keywords=book&node=18573211011&page=1&ref=a_search_c4_pageNum_0&pf_rd_p=1d79b443-2f1d-43a3-b1dc-31a2cd242566&pf_rd_r=1EB8HQ54VTDJMKKSZEG7"
    ]


    def parse(self, response):
        items = AudiblescrapingItem()

        book_name = [s.strip() for s in response.css('ul li h3').css(':first-child::text').extract()]
        # book_name = list(map(str.strip, response.css('ul li h3').css('::text').extract()))
        book_author = response.css('.authorLabel .bc-color-link').css(':first-child::text').extract()
        book_narrator = response.css('.narratorLabel .bc-color-link').css(':first-child::text').extract()
        # book_price = response.css('p span+ span').css('::text').extract()

        #Beautiful soup code
        respon = requests.get(f"https://www.audible.com/search?keywords=book&node=18573211011&page={AudibleSpider.page_number-1}&ref=a_search_c4_pageNum_0&pf_rd_p=1d79b443-2f1d-43a3-b1dc-31a2cd242566&pf_rd_r=2BH9QDWK6AZNJ37XWE3M")
        amazon_webpage = respon.text

        soup = BeautifulSoup(amazon_webpage, "html.parser")
        prices = soup.find_all(name="span", class_="bc-text bc-size-base bc-color-base")
        new_price = [ele.getText().strip() for ele in prices if "$" in str(ele)]
        book_price = new_price

        ###

        book_imagelink = response.css('.adbl-impression-container img').css(':first-child::attr(src)').extract()
        # book_imagelink = response.css('.adbl-impression-container img').css('::attr(src)').extract()[::2]


        for i in range(len(book_name)):
            items['book_name'] = book_name[i]
            items['book_author'] = book_author[i]
            items['book_narrator'] = book_narrator[i]
            items['book_price'] = book_price[i]
            items['book_imagelink'] = book_imagelink[i]

            yield items


        next_page = f'https://www.audible.com/search?keywords=book&node=18573211011&page={AudibleSpider.page_number}&ref=a_search_c4_pageNum_0&pf_rd_p=1d79b443-2f1d-43a3-b1dc-31a2cd242566&pf_rd_r=1EB8HQ54VTDJMKKSZEG7'

        if AudibleSpider.page_number < 32:
            AudibleSpider.page_number += 1
            yield response.follow(next_page, callback=self.parse)
