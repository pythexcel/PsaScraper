# PsaScraper

# Setup

* Install Python any version of python 3.6 + `https://www.python.org/downloads/`
* Clone scraper repo from git by cammand `git clone https://github.com/pythexcel/PsaScraper.git`
* go into project directory.
* Install requirements by cammand `pip3 install -r requirements.txt`
* Run script with url `python3 main.py -u https://www.psacard.com/auctionprices/baseball-cards/topps/ron-negray-gray-back/values/674398`



Note: In example i used python3 because if multiple python installed
 ### Examples

 * `python3 main.py -u https://www.psacard.com/auctionprices/baseball-cards/topps/ron-negray-gray-back/values/674398`
 
 * `python3 main.py -u https://www.psacard.com/auctionprices/baseball-cards/topps/warren-spahn-gray-back/values/674402`
 
 * `python3 main.py -u https://www.psacard.com/auctionprices/baseball-cards/topps/ernie-banks-white-back/values/179866`
 


# Psa_scrape

This is a script based on [this] Bs4.

### Prerequisites
* [Python3](https://www.python.org/)
* [BeautifulSoup](https://pypi.org/project/beautifulsoup4/)


### Usage

```
usage: main.py [-u] [--Url URL] 

```

##### Platforms

Linux: 
  * It works for linux by default you need to setup python version 3.6 +
  * Install BeautifulSoup and requests.

Note:
* Url: This is requred for the `-u` parameter for the run script.
 

