import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
import json
from bs4 import BeautifulSoup

class Recipespider(CrawlSpider):
    name = 'zoodpaz'
    allowed_domains = ["kalleh.com"]
    start_urls = ["https://kalleh.com/book/recipe"]

    rules = (
        # Rule(LinkExtractor(), callback='parse_item', follow=True),
        Rule ( LinkExtractor ( allow = ('book/recipe/*' ,) ) , callback = 'parse_item', follow=True ),
    )

    def parse_item(self , response):
        try:
            with open("recipe.json", "r") as f:
                file_data = json.load(f)
        except:
            file_data = []
        recipeCategory = response.xpath ( '//div[@itemprop="recipeCategory"]/text()').get ()
        hardshipLevel = response.xpath ( '//i[@class="icon-hardship"]/parent::*/parent::*/div[@class="text"]/text()' ).get ()
        personNumber = response.xpath ( '//i[@class="icon-persons"]/parent::*/parent::*/div[@class="text"]/text()' ).get ()
        prepTime = response.xpath ( '//div[@itemprop="prepTime"]/text()' ).get ()
        cookTime = response.xpath ( '//div[@itemprop="cookTime"]/text()' ).get ()
        photoAddress = response.xpath('//img[@class="attachment-full size-full wp-post-image"]/@data-src').get()
        foodTitle = response.xpath ( '//h1[@itemprop="name"]/text()' ).get ()
        descriptionFood = response.xpath ( '//div[@itemprop="description"]/p/text()').get()
        recipeIngredient = response.xpath ('//div[@itemprop="recipeIngredient"]/span/text()' ).getall ()
        recipeIngredientName = response.xpath ( '//div[@itemprop="recipeIngredient"]/span[@class="name"]/text()' ).getall ()
        recipeIngredientQuantity = response.xpath ('//div[@itemprop="recipeIngredient"]/span[@class="quantity"]/text()' ).getall()
        # recipeInstructions = response.xpath('//span[@itemprop="recipeInstructions"]/p/text()').getall()
        recipeInstructionstemp = response.xpath ( '//span[@itemprop="recipeInstructions"]/p' ).getall ()
        recipeInstructions = []
        for tagtemp in recipeInstructionstemp:
            soup = BeautifulSoup(tagtemp)
            recipeInstructions.append(soup.text)
        referenceslink = response.xpath('//div[@class="col-12 col-md-7 references"]/a/@href').get()
        referencesName = response.xpath('//div[@class="col-12 col-md-7 references"]/a/text()').get()
        keywordFood = response.xpath('//span[@class="tag"]/a/text()').getall()

        personNumber = personNumber if personNumber != None else "-"

        idFood = len(file_data)+1
        dic = {
            "ID": idFood,
            "url": response.request.url ,
            "recipeCategory" : recipeCategory,
            "hardshipLevel":hardshipLevel,
            "personNumber":personNumber,
            "prepTime":prepTime,
            "cookTime":cookTime,
            "photoAddress":photoAddress,
            "foodTitle":foodTitle,
            "descriptionFood":descriptionFood,
            "recipeIngredient":recipeIngredient,
            "recipeIngredientName":recipeIngredientName,
            "recipeIngredientQuantity":recipeIngredientQuantity,
            "recipeInstructions":recipeInstructions,
            "referenceslink":referenceslink,
            "referencesName":referencesName,
            "keywordFood":keywordFood


        }

        print(recipeIngredientName)


        file_data.append(dic)
        if len(recipeIngredientName) > 0:
            with open("recipe.json", "w",encoding="utf-8") as f:
                json.dump(file_data,f, ensure_ascii = False,indent = 4 )
        print(idFood)
        # print(recipeCategory,hardship,prepTime,cookTime,title_of_food,description_of_food)
        # print(recipeIngredient_name,recipeIngredient_quantity)
        # print ( response.request.url )
        # print(recipeIngredient)
        # print ( "yyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy" )
        # print ( response.request.url )
        # print(personNumber)

        # print(references_food_link)
        # print(references_food_name)
