import scrapy


class JewelSpider(scrapy.Spider):
    name = "jewelbot"
    allowed_domain = ['https://www.houseofindya.com/zyra/cat?depth=1&label=Jewelry']
    start_urls = ['https://www.houseofindya.com/zyra/cat?depth=1&label=Jewelry']

    # location of csv file
    custom_settings = {'FEED_URI': 'new1/csvFiles.csv'}

    def parse(self, response):
        necklace_sets = response.css('.catgName p::text')
        #images = response.css('img::attr(data-original)').extract()
        #price = response.css('.catgName.fal.fal-rupee-sign i::text').extract()
        #description = response.css('.prodecbox.current::text').extract_first()

        for item in zip(necklace_sets):
            scraped_info = {
                'necklace_sets': item[0],
            }

            yield scraped_info

            next_page_url = response.xpath('//*[@class="next"]/a/@href').extract_first()
            absolute_next_page_url = response.urljoin(next_page_url)
            yield scrapy.Request(absolute_next_page_url)
