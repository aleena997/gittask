import scrapy

class contentItem(scrapy.Item):
    name = scrapy.Field()
    image = scrapy.Field()
    prep_time= scrapy.Field()
    cook_time=scrapy.Field()
    serves=scrapy.Field()
    method=scrapy.Field()
    cook=scrapy.Field()
    urlname=scrapy.Field()
    link=scrapy.Field()
    ingredients=scrapy.Field()
    discription=scrapy.Field()
    imageurl=scrapy.Field()
    pass
