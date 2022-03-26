from textblob import TextBlob
import sys
import tweepy
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from wordcloud import WordCloud , STOPWORDS
import re
import os
from PIL import Image



def percentage(part , whole):
    return 100 * float(part)/float(whole)


consumerKey = 'MbbK8DtX30LmUPlxKxHRJGJ7n'
consumerSecret = 'QeRTu87szkJTJDt2REBbfSmhzyoRNVUw6FA9fmq1EBFWFNOxI4'
AccessToken = '1104734383292870656-HCCU8djsPygywmk7IbuV6PcD3dwKrR'
AccessTokenSecret  = 'h6BG881NpJGlXz2FansTelcCb28NaKi177evhQidtXavD'


auth = tweepy.OAuthHandler(consumerKey ,consumerSecret)
auth.set_access_token(AccessToken , AccessTokenSecret)
api=tweepy.API(auth)



posts = api.user_timeline(screen_name = "BillGates", count = 100, lang = "en" , tweet_mode = "extended")

#print last 5 tweets from this account 
print("show 5 recent tweets\n")

i=1
for tweet in posts[0:5]:
    print(str(i) + ')' + tweet.full_text + '\n')
    i=i+1


#Create a dataframe with a column tweets

df = pd.DataFrame([tweet.full_text for tweet in posts] , columns= ['Tweets'])
 



#cleaning text

def cleanTxt(text):
    text = re.sub(r'@[A-Za-z0-9]+' ,'',text ) #removes @mentions
    text = re.sub(r'#','',text)#removing hastags
    text = re.sub(r'RT[\s]+','',text) #removing RT
    text = re.sub(r'https?:\/\/\S+','',text) #remove hyperlinks

    return text

df['Tweets'] = df['Tweets'].apply(cleanTxt)

#show cleaned text
df



#Create a fun to get subjectivity
def getSubjectivity(text):
    return TextBlob(text).sentiment.subjectivity

def getPolarity(text):
    return TextBlob(text).sentiment.polarity

#creating columns for polarity and subjectivity
df['Subjectivity'] = df['Tweets'].apply(getSubjectivity)
df['Polarity'] = df['Tweets'].apply(getPolarity)




#Plotting Wordcloud

all_words = ' '.join([twts for twts in df['Tweets']])


def color_function(word = None , font_size = None, position = None, orientation = None , font_path =None , random_state = None):
    h = 257# 0-360
    s = 89 # 0-100
    l = random_state.randint(10,20)  # 0-100
    return "hsl({},{}%,{}%)".format(h , s, l)


my_mask = np.array(Image.open(r"C:\Users\adityaraj\Desktop\pro\CLOUD.jpg"))

wc = WordCloud(mask=my_mask, background_color="white", color_func= color_function ,width=500,height=500, max_words=2000,random_state= 42, max_font_size=196,stopwords=STOPWORDS ).generate(all_words)
plt.imshow(wc, interpolation = "bilinear")
plt.axis('off')
print("Printing the word cloud based on the tweets of Bill Gates",)
plt.show()



#for analyzing
searchTerm = input("Enter keyword / hashtag to search about : ")
noOfSearchTerms = int(input("Enter number of tweets to analyze:"))

tweets = tweepy.Cursor(api.search, q = searchTerm, lang = 'en').items(noOfSearchTerms)



positive = 0    #for the positive sentiments
negative = 0    #for the negatuve sentiments
polarity = 0    #for the average sentiments
neutral = 0     #for the neutral sentiments


for tweet in tweets:
    analysis = TextBlob(tweet.text)
    polarity = analysis.sentiment.polarity  + polarity

    if (analysis.sentiment.polarity == 0):
        neutral =neutral + 1
    elif (analysis.sentiment.polarity < 0):
        negative =negative +  1
    elif (analysis.sentiment.polarity > 0):
        positive =positive + 1        
   
   

#calculating percentage



positive = percentage(positive,noOfSearchTerms)
negative = percentage(negative, noOfSearchTerms)
neutral  = percentage(neutral, noOfSearchTerms)



#formatting code according to decimal places


positive = round(positive, 2)
negative = round(positive, 2)
neutral = round(neutral, 2)


#printing

print("SENTIMENTS of People on " + searchTerm + " after analyzing " + str(noOfSearchTerms) + " TWEETS are mostly : ")

if (polarity == 0):
    print("NEUTRAL")
elif (polarity < 0):
    print("NEGATIVE")
elif (polarity > 0):
    print("POSITIVE") 


#Displaying pie chart

#labels = ["Positive[ "+ str(positive) +" %]", "Neutral ["+ str(neutral) + "%]", "Negative [" + str(negative) + "%]" ]
sizes = [positive,neutral,negative]
colors = ['#3573DD', 'yellowgreen', '#E54720'] 
plt.rcParams['font.sans-serif'] = "Comic Sans MS"
explode = (0.1,0,0) #only explode the positive dize

labels = 'Positive' , 'Neutral' , 'Negative'
plt.pie(sizes,explode = explode, colors=colors,labels = labels, autopct='%1.1f%%', shadow=True, startangle=140)

plt.title('How people are reacting on ' +searchTerm+' by analyzing '+str(noOfSearchTerms)+ ' Tweets . ' )
plt.axis('equal')

plt.tight_layout() 
plt.show()    























