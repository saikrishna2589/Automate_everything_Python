
from bs4 import BeautifulSoup
import requests

from_currency =input('Enter the from currency(3 letters): ')
to_currency =input('Enter the to currency(3 letters): ')

amount = float(input("Enter the amount to convert: "))

url = f"https://www.x-rates.com/calculator/?from={from_currency}&to={to_currency}&amount={amount}"

#for URL, response object below gets the source code.so we use.text method from requests library
response = requests.get(url)

response_content = response.text
#debugging
#length
print(response.status_code , len(response.text))

#quick keyword sanity check

#print('<span' in response.text)
#print('ccOutputRslt' in response.text)
#converting the response i.e source code to BeautifulSoup object

bs4_object = BeautifulSoup(response_content,features='html.parser')


search_value = bs4_object.find('span',class_='ccOutputRslt')
print(search_value is not None)
print(search_value)

print(type(search_value))
#print(search_value.prettify())

#print(search_value.get_text("", strip=True))
#extract child elements in the tag
for i, child in enumerate(search_value.contents):
    print(i, repr(child), type(child))

#extract only top level text node
#this is top level text only. recursive =False prevents diving itno nested spans.
raw_number_text = search_value.find(string = True, recursive=False)
print(repr(raw_number_text))

output = float(raw_number_text.replace(",","").strip())

print(f"{amount}{from_currency} is equal to {output}{to_currency}")