from .datacleaning import DataCleaning
from .datasummary import DataSummary
import pandas as pd
# import class from module xmlparser
from .xmlparser import SitemapParser
from .webapi import APIDataFetch as adf
from .edawebapi import EDAWebAPI
from .webscrapping import WebScrape
import requests
import matplotlib.pyplot as plt
from bs4 import BeautifulSoup
import urllib.request as req

def main():
    
    print("XML Parser")
    website_url = "https://www.epicurious.com"
    # create the object for class SitemapParser
    sitemap_parser = SitemapParser(website_url)  
    # method extract_sitemaps call to get exactly how many sitemaps contains a certain website_url (using object call).
    sitemap_parser.extract_sitemaps()
    # converted xml of all 3 sitemaps into dataframe
    sitemap_parser.run()
    # Reading the API from the website
    base_url = f'https://newsdata.io/api/1/news?apikey={api_key}&q=education&country=us&language=en&category=business'
    # object created for class
    obj_adf = adf(base_url)
    # method call using object, to get the data as dataframe
    data = obj_adf.fetch_data()
    data
    obj_datacleaning = DataCleaning(data)
    data = obj_datacleaning.feild_drop()
    data
    obj_summary = DataSummary(data)
    obj_summary.show()
    obj_summary.shape()
    obj_summary.usecase()
    obj_summary.num_attributes()
    obj_summary.data_types()
    obj_summary.check_null()
    obj_eda = EDAWebAPI(data)
    obj_eda.creator_bargraph()
    URL="http://www.dictionary.com/wordoftheday/"
    obj_WebAPI = WebScrape(URL)
    obj_WebAPI.get_soup()
    obj_WebAPI.TodaysDate()
    obj_WebAPI.WordOfTheDay()
    obj_WebAPI.PronunciationWord()
    obj_WebAPI.WordTypeAndMeaning()
    obj_WebAPI.MoreWordInfo()
    obj_WebAPI.ExamplesWord()
    
if __name__ == "__main__":
    main()
