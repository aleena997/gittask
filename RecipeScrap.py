import scrapy
from ..items import contentItem

class RecipeScraper(scrapy.Spider):
	name='recipes'
	start_urls=['http://www.bbc.co.uk/food/recipes/search?cuisines[]=british']
			
	def parse(self, response):
		recipe_with_image=response.css('li.article.with-image')
		for recipe in recipe_with_image:
			for href in recipe.css('div.left.with-image h3 a::attr(href)'):
				url=response.urljoin(href.extract())
				yield scrapy.Request(url,callback=self.parse_contents)
				next_page_url=response.css('li.pagInfo-page-numbers-next a::attr(href)')
				nextpage=next_page_url.extract_first()
				next_page=response.urljoin(nextpage)
				yield scrapy.Request(url=next_page,callback=self.parse)
	def parse_contents(self, response):
		item= contentItem()
		name= response.css('.gel-trafalgar.content-title__text::text').extract_first()
		image= response.css('.recipe-media__image').xpath('@src').extract_first()
		prep_time=response.css('.recipe-metadata__prep-time::text').extract_first()
		cook_time=response.css('.recipe-metadata__cook-time::text').extract_first()
		serves=response.css('.recipe-metadata__serving::text').extract_first()
		cook=response.css('.chef__link::text').extract_first()
		discription=response.css('p.recipe-description__text::text').extract()
		s=response.css('.recipe-ingredients__list-item::text,.recipe-ingredients__link::text').extract()
		ingredients=""
		ingredients=ingredients.join(s)
		imageUrl=response.css('.chef__image-link').xpath('@href').extract()
		item['name']=name
		item['image']=image
		item['prep_time']=prep_time
		item['cook_time']=cook_time
		item['serves']=serves
		item['cook']=cook
		item['discription']=discription
		item['ingredients']=ingredients
		item['imageurl']=imageUrl
		yield item

