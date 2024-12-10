import scrapy
from scrapy.http import HtmlResponse
from parsing.les_6.img_download.items import ImgDownloadItem
from scrapy.loader import ItemLoader


class UnsplashcomSpider(scrapy.Spider):
    name = "unsplashcom"
    allowed_domains = ["unsplash.com"]
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.start_urls = [f"https://unsplash.com/s/photos/{kwargs.get('query')}"]


    def parse(self, response: HtmlResponse):
        try:
            if response.status == 200:
                links = response.xpath("//figure//a[@class='zNNw1']")
                for link in links:
                    yield response.follow(link, callback=self.parse_unsplash_img)

        except Exception as e:
            print(e)


    def parse_unsplash_img(self, response: HtmlResponse):
        loader = ItemLoader(item=ImgDownloadItem(), response=response)
        loader.add_xpath('title', "//h1[@class='vev3s']/text()")
        loader.add_xpath('category', "//div[@class='zb0Hu atI7H']//a/text()")
        loader.add_value('url', response.url)
        loader.add_xpath('image', "//button[@type='button']//div[@class='wdUrX']"
                                  "//img[@class='I7OuT DVW3V L1BOa']/@srcset")

        yield loader.load_item()