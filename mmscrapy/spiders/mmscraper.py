import scrapy
import re
from mmscrapy.items import MmScrapyItem

class MmScraperSpider(scrapy.Spider):
  name = 'mmscraper'
  start_urls = ['https://the start url/category']

  def parse(self, response):
    items = response.xpath('//ul/li[@class="card--product-block__wrapper"]/a')

    for item in items:
      href = item.xpath('@href').extract_first()
      absolute_url = response.urljoin(href)
      yield scrapy.Request(absolute_url, callback=self.parse_detail_page_test)

    next_page = response.css('nav.pager ul li.pager__item--next a::attr(href)').extract_first()
    if next_page:
      yield scrapy.Request(
          response.urljoin(next_page), 
          callback=self.parse
      )

  def parse_detail_page_test(self, response):
    item = MmScrapyItem()
    item['title'] = response.css('h1::text').extract_first()
    item['description'] = response.xpath('normalize-space(//*[@id="description"]/p[2]/text())').extract_first()
    item['ean'] = response.xpath('normalize-space(.//*[@id="details"]/table/tbody/tr[1]/td[2]/text())').extract_first()
    #regex to scrape a background-image url
    src = response.xpath("//div[contains(@class, 'product-detail__slide-wrapper')]//@style").re_first(r'url\(([^\)]+)')
    img = response.urljoin(src)
    item['file_urls'] = [img]
    yield item