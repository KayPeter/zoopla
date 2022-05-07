from zoopla.items import ZooplaItem
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class HousesSpider(CrawlSpider):
    name = 'houses'
    allowed_domains = ['www.zoopla.co.uk']
    start_urls = ['https://www.zoopla.co.uk/for-sale/property/london']

    rules = (
        Rule(LinkExtractor(restrict_xpaths=(
            "//a[@data-testid='listing-details-link']")), callback='parse_item', follow=True),
        Rule(LinkExtractor(restrict_xpaths=(
            "//li[contains(@class, 'PaginationItemNext')]/a"))),
    )

    def parse_item(self, response):
        item = ZooplaItem()
        item['agent'] = response.xpath("//p[contains(@class, 'css-lnx84k-AgentName e5vsiog3')]/text()").get()
        item['agent_logo_url'] = response.xpath("//img[contains(@class, 'AgentImage')]/@src").get()
        item['price'] = response.xpath("//p[@data-testid='price']/text()").get()
        item['postcode'] = response.xpath("//address[@data-testid='address-label']/text()").get()
        item['city'] = response.xpath("//ol[contains(@class, 'css-acjyh-StyledBreadcrumbWrapper')]/li[3]/a/text()").get()

        return item
