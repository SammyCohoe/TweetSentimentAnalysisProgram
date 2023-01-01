import snscrape.modules.twitter as sntwitter
import pandas as pd

# query search terms
query1 = ""
keywords = []
for i in range(0, len(keywords)):
    query1 +=  "#" + keywords[i] + " OR "


query = "#godofwar"
tweets = []     # list of tweets
limit = 50   # max number of tweets in the tweet array

# scraping
for tweet in sntwitter.TwitterSearchScraper(query).get_items():

        # checking if the tweets list has hit the list length limit
        if len(tweets) == limit:
            break
        else:
            # determining if this user has already said something about the subject
            if (tweet.username not in [tweets]):
                tweets.append(tweet.content.split('http')[0] + " ")
            else:
                continue

# df = pd.DataFrame(tweets, columns=['Tweet'])
# print(df) split('http')[0]
