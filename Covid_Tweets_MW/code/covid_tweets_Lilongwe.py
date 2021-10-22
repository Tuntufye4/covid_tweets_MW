import pandas as pd
import snscrape.modules.twitter as sntwitter
import itertools

df = pd.DataFrame(itertools.islice(sntwitter.TwitterSearchScraper(
    'Covid near:"Lilongwe" within:100km').get_items(), 50))[['date', 'content']]

df.to_csv('covid_Lilongwe.csv', index = False)