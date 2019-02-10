import scrapy
from ..items import contentItem

class RecipeScraper(scrapy.Spider):
	name='recipes'
	allowed_domain=['http://www.bbc.co.uk/food/recipes/search?cuisines[]=british']
	start_urls=['http://www.bbc.co.uk/food/recipes/bunny_chow_38916']
	def parse(self, response):
		item= contentItem()
		name= response.css('.gel-trafalgar.content-title__text::text').extract_first()
		image= response.css('.recipe-media__image').xpath('@src').extract_first()
		prep_time=response.css('.recipe-metadata__prep-time::text').extract_first()
		cook_time=response.css('.recipe-metadata__cook-time::text').extract_first()
		serves=response.css('.recipe-metadata__serving::text').extract_first()
		item['name']=name
		item['image']=image
		item['prep_time']=prep_time
		item['cook_time']=cook_time
		item['serves']=serves
		yield item
