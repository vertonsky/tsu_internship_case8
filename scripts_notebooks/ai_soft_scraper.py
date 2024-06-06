import os
import urllib.parse
from dotenv import load_dotenv, dotenv_values
import urllib

import numpy as np
import pandas as pd

from openai import OpenAI

# load_dotenv()
# client = OpenAI(api_key=os.getenv('API_KEY'), base_url='https://api.vsegpt.ru/v1/')

# responce = client.chat.completions.create(
#   model = 'perplexity/pplx-70b-online',
#   messages = messages
# )

uni_data = pd.read_csv(r'./data/1.2_uni_data_w_soft.csv')

uni_data['SoftInfo'] = ''

for i in uni_data.index:
    site = uni_data['PathToSoft'][i]
    main_site = uni_data['WebSite'][i]

    print(site, main_site)
    if site != 'nan':
        messages = [
        {
            "role": "system",
            "content": (
                "В ответе только список"
                "Без пояснений"
            ),
        },
        {
            "role": "user",
            "content": (
                f"Зайди на сайт '{urllib.parse.quote(str(site))}' и составь список ПО, используемого в университете. Дополни этот список ПО данными с '{urllib.parse.quote(str(main_site))}' Перечисли ПО через запятую"
            ),
        },
        ]
    else:
        messages = [
        {
            "role": "system",
            "content": (
                "Give list only"
                "No explanations"
            ),
        },
        {
            "role": "user",
            "content": (
                f"Зайди на сайт '{urllib.parse.quote(str(main_site))}' и составь список ПО, используемого в университете. Перечисли ПО через запятую"
            ),
        },
        ]
    load_dotenv()
    client = OpenAI(api_key=os.getenv('API_KEY'), base_url='https://api.vsegpt.ru/v1/')

    responce = client.chat.completions.create(
        model = 'perplexity/llama-3-sonar-large-32k-online',
        messages = messages
    )

    print(responce.choices[0].message.content)

    uni_data["SoftInfo"][i] = responce.choices[0].message.content

uni_data.to_csv('./data/batches/_0.1_llama3_large_w_testing_batch.csv', index=False)