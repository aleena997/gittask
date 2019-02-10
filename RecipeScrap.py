import scrapy
from ..items import contentItem

class RecipeScraper(scrapy.Spider):
	name='recipes'
	allowed_domain=['http://www.bbc.co.uk/food/recipes/search?cuisines[]=british']
	start_urls=['http://www.bbc.co.uk/food/recipes/bunny_chow_38916']
	def parse(self, response):
		item= contentItem()
		name= response.css('.gel-trafalgar.content-title__text::text').extract_first()
		item['name']=name
		yield item
