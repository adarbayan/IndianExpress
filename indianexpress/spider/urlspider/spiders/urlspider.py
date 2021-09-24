import scrapy
import re
import logging
import codecs
import json
from scrapy.utils.log import configure_logging
import logging
from datetime import timedelta, datetime


class QuotesSpider(scrapy.Spider):
    name = "urlspider"
    configure_logging(install_root_handler=False)
    logging.basicConfig(
        filename='urlspiderlog.txt',
        format='%(levelname)s: %(message)s',
        level=logging.INFO
    )

    def start_requests(self):
        #indianExpress =; this variable decrements itself as 1,
        # while we are decremens the page number as 1.
        indianExpress = 318
        url=  'https://indianexpress.com/page/318/?s=archive'
        for i in range(indianExpress):
            indianExpress-=1
            yield scrapy.Request(url=url, callback=self.parse)
            url = "https://indianexpress.com/page/" +str(indianExpress) + "/?s=archive"
           

    def parse(self, response):
        print(response.url)
        urlfilename = re.sub(r"\/|:", r"_", response.url)
           

        urls = response.xpath('//div[@class="details"]/div[@class="picture"]/a/@href').extract()
        filename = 'urls.jl'
        with codecs.open(filename, 'a', 'utf-8') as f:
            for rl in urls:
                line = json.dumps(rl,ensure_ascii=False) + "\n"
                f.write(line)        

