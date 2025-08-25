from os import getenv

import requests
from dotenv import load_dotenv
import os

load_dotenv() #loads env variables from .env file into process environment

news_api_key = os.getenv('news_api')
print(news_api_key)


base_url  = 'https://newsapi.org/v2/everything'


params ={
      "q":"bitcoin",
      "from": '2025-08-15',
      "to": "2025-08-25",
      "language" :"en",
      "sortBy" : "popularity",
      "apiKey" :news_api_key

}

print(params)


response = requests.get(base_url, params=params ,timeout=10)

#checking the status code and the full URL. validation check step
print("response code:", response.status_code)
print("requested url:",response.url )


data = response.json()

print(data)

print('length of articles:', len(data.get('articles',[])))

#print("sample title:",data.get('articles',[])[0]['title'] )

articles_list = data.get('articles',[])


for idx, article in enumerate(articles_list):
      print(f"{idx} : Title : {article['title']} \n Description: {article['description']}")


