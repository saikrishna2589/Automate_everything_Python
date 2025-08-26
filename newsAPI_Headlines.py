import requests
import os
from dotenv import load_dotenv
import pandas as pd

#Load API Key from env variable
load_dotenv() # load current variable
API_Key = os.getenv("news_api")
print("API_Key", API_Key)


#base url
base_url = ' https://newsapi.org/v2/top-headlines'

user_input_country =input("enter abbreviation of country (2 small letters) : ")

#builing query parameters based on documentation https://newsapi.org/docs/endpoints/top-headlines

params ={
    "country" : user_input_country,
    "apiKey" :API_Key
}

response = requests.get(base_url, params=params, timeout=10)

data = response.json()

print("response status : " , response.status_code)
print("response url : ", response.url)

print("response text : ", response.text )

print("data : ", data)

data_articles = data.get('articles', [])
#print("sample article data : ", data.get('articles',[])[0])
#print("length of articles : ",len(data["articles"]) )
print('data_articles : ', data_articles )

list_of_articles =[]

dict_of_articles ={}
for idx, article in enumerate(data_articles):
    #list_of_articles.append(f"{idx} :  {article['title']} :  {article['url']} \n")
    list_of_articles.append({
        "id" : idx,
        "title" : article.get("title"),
        "url" : article.get("url")

    })
    #if article['title'] not in dict_of_articles:
      #  dict_of_articles[article['title']] = article['url']


#for article in list_of_articles:
 #   print(article)

#print(f"dict_of_articles :  {dict_of_articles}")


print(f"list of articles:", list_of_articles)

#convert list of articles (list of dictionaries) to dataframe

df = pd.DataFrame(list_of_articles)

print(df)

#export data to csv

df.to_csv("us_headlines.csv",index=False)