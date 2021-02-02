import scrapy
from urllib.parse import urlparse
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
import json
from bs4 import BeautifulSoup
import sys
sys.path.append("/home/negin/PycharmProjects/ZoodPaz/Scrapy/zoodpaz/zoodpaz/spiders")
import Preprocess




class Recipespider(CrawlSpider):
    name = 'irancook'
    allowed_domains = ["irancook.ir"]
    start_urls = ["https://irancook.ir/"]

    rules = (
        # Rule(LinkExtractor(), callback='parse_item', follow=True),
        Rule ( LinkExtractor ( allow = () ) , callback = 'parse_item', follow=True ),
    )

    def parse_item(self , response):
        try:
            with open("recipe.json", "r") as f:
                file_data = json.load(f)
        except:
            file_data = []
        # if response contain recipe then continue
        recipeInstructions = response.xpath ( '//div[@class="content-full boxinc instructions print-only content-gray"]').get()
        if recipeInstructions != None: #Check the page is cooking recipe or not

            soup = BeautifulSoup(recipeInstructions)
            recipeInstructions = soup.text
            cleaner = Preprocess.Preprocess()
            clean_recipeInstructions = cleaner.text_normalazation(recipeInstructions)
            print("------------------------------")
            print ( response.request.url )
            print(clean_recipeInstructions)





        # recipeInstructions = []
        #
        # idFood = len(file_data)+1
        # dic = {
        #     "ID": idFood,
        #     "url": response.request.url ,
        #     "foodTitle":foodTitle,
        #     "recipeInstructions":recipeInstructions,
        #     "recipeInstructions":recipeInstructions,



        # }
        #
        # print(recipeIngredientName)
        #
        #
        # file_data.append(dic)
        # if len(recipeIngredientName) > 0:
        #     with open("recipe_irancook.json", "w",encoding="utf-8") as f:
        #         json.dump(file_data,f, ensure_ascii = False,indent = 4 )
        # print(idFood)
        # print(recipeCategory,hardship,prepTime,cookTime,title_of_food,description_of_food)
        # print(recipeIngredient_name,recipeIngredient_quantity)
        # print ( response.request.url )
        # print(recipeIngredient)
        # print ( "yyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy" )
        # print ( response.request.url )
        # print(personNumber)

        # print(references_food_link)
        # print(references_food_name)
