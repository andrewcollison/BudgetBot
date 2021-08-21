import feedparser
import re

def usd2aud(usd):
    # Fetch data from RBA via RSS feed
    NewsFeed = feedparser.parse("https://www.rba.gov.au/rss/rss-cb-exchange-rates.xml")
    valueStr = NewsFeed['entries'][0]['title_detail']['value']
    
    excRate = float(re.findall('[0-9].[0-9][0-9][0-9][0-9]', valueStr )[0])
    aud = usd/excRate
    
    return aud


