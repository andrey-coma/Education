import scrapy
from scrapy.http import HtmlResponse
from items import JobparserItem

class HhruSpider(scrapy.Spider):
    name = "hhru"
    allowed_domains = ["hh.ru"]
    start_urls = ["https://novosibirsk.hh.ru/search/vacancy?text=Python&salary=&ored_clusters=true&area=4&page=6&searchSessionId=f053b2c4-718e-4dce-8bc3-04fecdb47577"]


    def parse(self, response:HtmlResponse):
        next_page = response.xpath("//a[@data-qa='pager-next']/@href").get()
        if next_page:
            yield response.follow(next_page, callback=self.parse)

        links = response.xpath("//a[@data-qa='serp-item__title']/@href").getall()
        for link in links:
            yield response.follow(link, callback=self.vacancy_parse)


    def vacancy_parse(self, response:HtmlResponse):
        name = response.xpath("//h1/text()").get()
        salary = response.xpath("//div[@data-qa='vacancy-salary']//text()").getall()
        url = response.url

        yield JobparserItem(name=name, salary=salary, url=url)