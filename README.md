# Twitter-Sentiment-Analysis
Sentiment Analysis is a technique used in text mining. It may, therefore, be described as a text mining technique for analyzing the underlying sentiment of a text message, i.e., a tweet. Twitter sentiment or opinion expressed through it may be positive, negative or neutral. However, no algorithm can give you 100% accuracy or prediction on sentiment analysis.
<p>
We used Python, Tweepy and TextBlob to perform sentiment analysis of a selected twitter account using  twitter API and Natural Processing Language. 
 Importing  Python Modules:
textblob
sys
tweepy
matplotlib.pyplot
pandas
numpy
PIL
wordcloud
re

Getting Tweets using twitter API.
Printing 5 most recent tweets of Bill Gates.
Creating Dataframe with column tweets.
Cleaning and filtering Text:
 Removing hashtags from the fetched tweets . Removing hasgtags, removing retweets    ,removing hyperlinks and filtering text by removing stopwords  (such as “the”, “a”, “an”, “in”) for masking wordcloud .  


 Plotting the Wordcloud by masking it with a twitter logo image
Analyzing the filtered tweets and calculating percentage of positive , negative and neutral.
Plotting the piechart based on the analysis.
</p>


## Screenshots
Printing the wordcloud masked by a twitter logo image for better visualization.
![tsa1](https://user-images.githubusercontent.com/68144680/160224000-6bdf8887-10cd-4bc6-8221-dbffdb534400.png)
Entering keyword and number of tweets from user for analyzing data
![tsa2](https://user-images.githubusercontent.com/68144680/160224052-ce54c0c2-7d33-4451-b285-4c0224be9258.png)

Plotting piechart
![tsa2](https://user-images.githubusercontent.com/68144680/160224072-59c05e8a-cb18-4d19-a2a3-99d7895df84f.png)

