import scrapy
from ..items import ProductBotItem
import re
class amazonSpider(scrapy.Spider):
	name = "product"

	start_urls = ['https://www.amazon.in/s?k=books']

	def parse(self, response):

		product_title = response.css("span.a-size-medium.a-color-base.a-text-normal::text").getall()
		author = response.css("a.a-size-base.a-link-normal::text").getall()
		price = response.css("span.a-price-whole::text").getall()
		image_urls = response.css("img.s-image::attr(src)").getall()
		#print("Total Product in First page-",len(image_urls))
		author_list = []
		#print(image_urls)
		#print("Total Product in First page-",len(product_title))
		
		#authorRegex = re.compile(r'\w')
		for j in range(len(author)):
			#print(author[j])
			writer = re.sub('\n\r+','',author[j].strip())
			#print("---Writer---",writer)
			check_list = ['Paperback','Kindle Edition','Hardcover','']
			if writer in check_list:
				pass
			else:
				author_list.append(writer)
		#print("====Author=====", author_list)
		#print(len(author_list))
			
		for i in range(len(image_urls)):
			products = ProductBotItem()
			products['product_title'] = product_title[i]
			products['author'] = author_list[i]			
			products['price'] = price[i]
			#products['images'] = image[i]
			products['image_urls'] = image_urls[i]
			yield products
		
	
		'''	
		yield { 
				"product_title" : product_title,
				"author" : author,
				"price" : price
				}
		'''