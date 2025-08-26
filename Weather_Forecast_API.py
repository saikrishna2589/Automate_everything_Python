#base url, params, extract json object, extract city,time,temperature, condition
import  requests
import pandas as pd
from dotenv import load_dotenv
import os



load_dotenv()


openweather_api_key = os.getenv('OPENWEATHER_API_KEY')
city_name = input('Enter the city name : ')

def weather_extract_info(city_name, openweather_api_key):
    base_url = 'https://api.openweathermap.org/data/2.5/forecast'
    params = {
        'q' : city_name,
        'appid' : openweather_api_key
    }
    print('API key: ', openweather_api_key)
    response = requests.get(base_url, params=params, timeout=10)
    content = response.json()
    print('response_status_code: ', response.status_code)
    print('response text : ', response.text)
    print('response url : ', response.url)
    #print('json content : ', content)
    return content




#url = f"https://api.openweathermap.org/data/2.5/forecast?q={city_name}&appid={openweather_api_key}"


json_temp_data = weather_extract_info(city_name,openweather_api_key)

temp_data =[] #empty list to store dictionary of temp values

list_of_dict= json_temp_data['list']

#print('length')
#print('list : ', json_temp_data['list'])

for idx, temp_each_day in enumerate(list_of_dict):

    temp_data.append(
        {             "s.no:" : idx,
                      "city:" : city_name,
                      "time:" : temp_each_day.get('dt_txt',[]),
                      "temperature:": temp_each_day['main']['temp'],
                      "condition:" : temp_each_day['weather'][0]['description']
                      } )

#for data in temp_data:
   # print(data)

#convert the temp_data list into df
temp_dataframe = pd.DataFrame(temp_data)


#save to csv
temp_dataframe.to_csv('weather_forecast_5day_3hr_data.csv',index=False)