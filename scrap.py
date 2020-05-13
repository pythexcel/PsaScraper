import argparse, os

import requests

from bs4 import BeautifulSoup

import csv


def ScraperBot(Url):
    print("[+] Success! Scrap Bot Starting!")
    page = requests.get(Url)
    soup = BeautifulSoup(page.text)
    PsaDateData = soup.select(".item-date")
    PsaPriceData = soup.select(".item-price")
    PsaSourceData = soup.select(".item-auctionhouse")
    PsaModelData = soup.select("#body-container li~ li+ li a")
    PsaMakeData = soup.find('h1', class_='title-mobile')
    DateList = [date.text for date in PsaDateData]
    ValueList = [price.text for price in PsaPriceData]
    SourceList = [source.text for source in PsaSourceData]
    if PsaModelData:
        Model = PsaModelData[0].text
    else:
        Model = None
    if Model is not None:
        P_year = Model.split(" ")
        PublicationYear = P_year[0]
    else:
        PublicationYear = None
    Make = PsaMakeData.text
    file = open(Make+'.csv', 'w', newline ='') 
    with file:
        header = ['Month','Day','Year','Value','Year','Make','Model','Source']
        writer = csv.DictWriter(file, fieldnames = header) 
        writer.writeheader() 
        try:
            for indexnum in range(0,len(PsaPriceData)):
                date = DateList[indexnum].split("/")
                Month = date[0]
                Day = date[1]
                Year = date[2]
                writer.writerow({"Month":Month,"Day":Day,"Year":Year,"Value":ValueList[indexnum],"Year":PublicationYear,"Make":Make,"Model":Model,"Source":SourceList[indexnum]}) 
        except Exception:
            print("[-] Faild! Data missing!")
    print("[+] Data Scrap Done check csv file in current directory......>>>>>>>")