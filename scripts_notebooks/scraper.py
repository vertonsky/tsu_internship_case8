import pandas as pd
from duckduckgo_search import DDGS
import time

data = pd.read_csv('./data/1.0_uni_data_cleared.csv')
sites = data['WebSite']
data['PathToSoft'] = ''

for i in data.index:
  site = data['WebSite'].iloc[i]
  print(i, site)
  results = DDGS().text("Список программного обеспечения site:" + site, region='ru-ru', max_results=1)
  if results: 
    data['PathToSoft'].iloc[i] = results[0]['href']
    print(results[0]['href'])

  time.sleep(5)



data.to_csv('./data/1.2_uni_data_w_soft.csv', index=False)