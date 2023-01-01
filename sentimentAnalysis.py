from collections import Counter

import matplotlib.pyplot as pltNegative
import matplotlib.pyplot as pltPositive
import cohere
import requests
co = cohere.Client('ZL6YNdQVYbCPkVV27peG9NFBVTbChAzexQv1GMzR')
from cohere.classify import Example
from twitterScraper import tweets

# example reviews to determine what is classified as a positive, negative, and neutral review
exampleReviews = [
  Example("This was an amazing experience", "positive"),
  Example("The visuals went above and beyond", "positive"),
  Example("One of the best soundtracks I have ever heard", "positive"),
  Example("This went so hard", "positive"),
  Example("New favourite movie", "positive"),
  Example("This made no sense", "negative"),
  Example("This was a complete miss", "negative"),
  Example("Garbage, trash, bad, shit", "negative"),
  Example("I hated every second of this", "negative"),
  Example("What a waste", "negative"),
  Example("It was okay", "neutral"),
  Example("This album was mediocre", "neutral"),
  Example("I dont know what to think", "neutral")
]

# list of user tweets
userTweets = []
for i in range(0, 45):
  userTweets.append(tweets[i])

response = co.classify(
  inputs = userTweets,
  examples = exampleReviews,
)

full = []
mostPositive = {}
mostNegative = {}
for i in range(0,len(userTweets)):
  full.append([userTweets[i],
               response.classifications[i].confidence,
               response.classifications[i].prediction])
  if response.classifications[i].prediction == 'positive':
    mostPositive[userTweets[i]] = response.classifications[i].confidence
  elif response.classifications[i].prediction == 'negative':
    mostNegative[userTweets[i]] = response.classifications[i].confidence
  else:
    continue

# returning a dictionary of the sorted negative tweets in descending order
sortedMostNegative = sorted(mostNegative.items(), key=lambda x:x[1], reverse = True)
#print(sortedMostNegative)
fiveMostNegative = []

for i in range(2):
  fiveMostNegative.append(sortedMostNegative[i][0])

# returning a dictionary of the sorted positive tweets in descending order
sortedMostPositive = sorted(mostPositive.items(), key=lambda x:x[1], reverse = True)
#print(sortedMostPositive)
fiveMostPositive = []
for i in range(3):
  fiveMostPositive.append(sortedMostPositive[i][0])

# list of confidence values for negative tweets
negativeConfidence = []
for k, v in mostNegative.items():
  negativeConfidence.append(round(v, 1))


# list of all confidence values for positive tweets
positiveConfidence = []
for k, v in mostPositive.items():
  positiveConfidence.append(round(v, 1))


# dictionary with key of confidence, value of number of same confidence
negativeConfidenceCount = dict(Counter(negativeConfidence))
positiveConfidenceCount = dict(Counter(positiveConfidence))


nConfidence = list(negativeConfidenceCount.keys())
nNumber = list(negativeConfidenceCount.values())

pConfidence = list(positiveConfidenceCount.keys())
pNumber = list(positiveConfidenceCount.values())

pltNegative.bar(nConfidence, nNumber, color = "yellow", width = 0.1)

pltNegative.ylabel("Number of Negative Tweets")
pltNegative.xlabel("Confidence Level")
pltNegative.title("Number of Negative Tweets per Confidence Level t")
pltNegative.show()

pltPositive.bar(pConfidence, pNumber, color = "blue", width = 0.1)
pltPositive.ylabel("Number of Positive Tweets")
pltPositive.xlabel("Confidence Level")
pltPositive.title("Number of Positive Tweets per Confidence Level t")
pltPositive.show()


