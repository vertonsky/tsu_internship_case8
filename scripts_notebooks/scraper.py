import requests
from bs4 import BeautifulSoup
import pandas as pd
from time import sleep
import random

headers = {
    'User-Agent':
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36'}

# for debug
uni_names = []

for page in range(1, 2): #100
  sleep(random.uniform(5.0, 10.0))

  url = f"https://vuzopedia.ru/vuz?page={page}"

  response = requests.get(url, headers=headers)
  soup = BeautifulSoup(response.text, 'lxml')
  data = soup.find_all('div', class_='vuzesfullnorm')

  for i in data:
    uni_name = i.find('div', class_='itemVuzTitle').text.strip().replace('\n', '')
    uni_names.append(uni_name)

    

df = pd.DataFrame(uni_names)
df.to_csv(r'data\example_all_universities.csv', encoding='utf-8')
