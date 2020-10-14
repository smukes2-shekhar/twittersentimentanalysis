
import pandas as pd
import numpy as np

#Reading the dataset in csv
tweets = pd.read_csv('C:/Users/13126/Downloads/Tweets.csv', sep=',')

#showing the first 10 lines
tweets.head(10)

#Filtering for the category (as is done in SQL by using order BY)
positive = tweets['airline_sentiment'].str.contains("positive")
negative = tweets['airline_sentiment'].str.contains("negative")
neutral = tweets['airline_sentiment'].str.contains("neutral")
positive_tweets = tweets[positive]
positive_tweets.shape
negative_tweets = tweets[negative]
negative_tweets.shape
neutral_tweets = tweets[neutral]
neutral_tweets.shape


# In[34]:
worst_airline = negative_tweets[['airline','airline_sentiment_confidence','negativereason']]
worst_airline

# Creating a ranking system for the worst airline
cnt_worst_airline = worst_airline.groupby('airline', as_index=False).count()
cnt_worst_airline.sort_values('negativereason', ascending=False)

# Creating a ranking system for the best airline
best_airline = positive_tweets[['airline','airline_sentiment_confidence']]
cnt_best_airline = best_airline.groupby('airline', as_index=False).count()
cnt_best_airline.sort_values('airline_sentiment_confidence', ascending=False)

# Creating a ranking system for the negative reasonings
motivation = negative_tweets[['airline','negativereason']]
cnt_bad_flight_motivation = motivation.groupby('negativereason', as_index=False).count()
cnt_bad_flight_motivation.sort_values('negativereason', ascending=False)

print(worst_airline)
print(best_airline)

