# -*- coding: utf-8 -*-
import scrapy
from scrapy import Request
from recipes.items import *
from scrapy.selector import Selector
from urllib.parse import urljoin


class RecipeslistSpider(scrapy.Spider):
    name = 'recipesList'
    allowed_domains = ['dietamediterranea.com']
    start_urls = ['https://dietamediterranea.com/recipes/croquetas-de-verduras/']

    def parse(self, response):
        recipe = RecipesItem()
        
        s = Selector(response)

        recipe['name']=s.xpath('//h1[@class="entry-title"]/text()').get()
        recipe['relations']=s.xpath('//span[@class="cooked-servings"]/a/text()').get()
        recipe['preparedTime']=s.xpath('//span[@class="cooked-prep-time cooked-time"]/text()').get()
        recipe['cookedTime']=s.xpath('//span[@class="cooked-cook-time cooked-time"]/text()').get()
        recipe['totalTime']=s.xpath('//span[@class="cooked-total-time cooked-time"]/text()').get()
        ##recipe['ingredients']=s.xpath('//div[@class="cooked-single-ingredient cooked-ingredient"]/span/text()').getall()
        recipe['steps']=s.xpath('//div[@class="cooked-dir-content"]/p/text()').getall()
        recipe['category']=s.xpath('//span[@class="cooked-taxonomy cooked-category"]/a/text()').get()
 
        recipe['ingredients']=[]
        for sel in s.xpath('//div[@class="cooked-recipe-ingredients"]/div'):
            ingredient = IngredientsItem()
            ingredient['amount']=sel.xpath('./span[@class="cooked-ing-amount"]/text()').get()
            ingredient['measurement']=sel.xpath('./span[@class="cooked-ing-measurement"]/text()').get()
            ingredient['nameIngredient']=sel.xpath('./span[@class="cooked-ing-name"]/text()').get()
            recipe["ingredients"].append(ingredient)

        self.log(recipe)

        url =s.xpath('//span[@class="full-link"]/a/@href').get()
        yield Request(urljoin("https://dietamediterranea.com", url), callback=self.parse)

        yield recipe

