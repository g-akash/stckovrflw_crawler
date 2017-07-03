import scrapy


class StackSpider(scrapy.Spider):
	name = "stack"
	def start_requests(self):
		start_url = "https://stackoverflow.com/questions/tagged/"+self.tag
		print "printing start url"
		print start_url
		urls = [start_url]
		for url in urls:
			yield scrapy.Request(url,self.parse)

	def parse(self,response):
		filename = "stack.html"
		responses = response.css('.excerpt::text').extract()
		ans = {}

		
		for i in range(len(responses)):
			yield{
			i:responses[i]
			}
		next_url = str(response.xpath('//*[@id="mainbar"]/div[4]/a[6]/@href').extract_first())
		if next_url is not None:
			

			next_url = response.urljoin(next_url)
			print "printed len"
			print next_url

			yield scrapy.Request(next_url, callback=self.parse)