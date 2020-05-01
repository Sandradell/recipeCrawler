# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class RecipesItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    name = scrapy.Field()
    relations=scrapy.Field()
    preparedTime=scrapy.Field()
    cookedTime=scrapy.Field()
    totalTime=scrapy.Field()
    ingredients=scrapy.Field()
    category=scrapy.Field()
    steps=scrapy.Field()
    
class IngredientsItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    nameIngredient = scrapy.Field()
    measurement=scrapy.Field()
    amount=scrapy.Field()

