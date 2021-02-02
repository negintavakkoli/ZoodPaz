import scrapy
from urllib.parse import urlparse
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
import json
from bs4 import BeautifulSoup
# import Preprocess
#
# f = open("raw-text-irancook.text")
#
# for item in f:
#     op = Preprocess.Preprocess ()
#     clrtext = op.text_normalazation ( item )
#     print ( clrtext )
#     print(item)
# f.close()

# class Recipespider(CrawlSpider):
#     name = 'others'
#     allowed_domains = ["irancook.ir"]
#     start_urls = ["https://irancook.ir/"]
#
#     rules = (
#         Rule(LinkExtractor(), callback='parse_item', follow=True),
#         # Rule ( LinkExtractor ( allow = ('01/*' ,) ) , callback = 'parse_item', follow=True ),
#     )
#
#     def parse_item(self , response):
#
#         urls = urlparse ( response.request.url )
#         allowed_urls = urls.path.split ( "/" )[1]
#
#         if allowed_urls.isdigit():
#             print ( "_________________________________" )
#             print ( response.request.url )
#
#         try:
#             with open("recipe.json", "r") as f:
#                 file_data = json.load(f)
#         except:
#             file_data = []
#         # if response contain recipe then continue
#
#         recipeCategory = response.xpath ( '//div[@class="content-full boxinc instructions print-only content-gray"]').get ()
#         foodTitle = response.xpath ('//h1[@class="title fn print-only"/text()]').get()
#
#         if recipeCategory != None:
#             soup = BeautifulSoup(recipeCategory)
#
#             print("*******************8")
#             print(soup.text)
#         else:
#             print("_________________________________")
#             print("WE Have not any food :)")

            # foodTitle = response.xpath ( '//h1[@itemprop="name"]/text()' ).get () # Get the title of food