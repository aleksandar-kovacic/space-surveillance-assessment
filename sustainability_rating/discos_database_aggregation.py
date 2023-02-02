import pandas as pd
from pprint import pprint
import requests
import time

URL = 'https://discosweb.esoc.esa.int'
token = 'IjMyYTQwZGMwLTNmMjItNDI1ZC1hNGRjLTM3ZmYwYmZlN2FmZiI.4Dw5fRkISFB-Mpnm7oj1PBSrd0A'

dictionary_list = []

for i in range(1,27):
    response = requests.get(
        f'{URL}/api/objects',
        headers={
            'Authorization': f'Bearer {token}',
            'DiscosWeb-Api-Version': '2',
        },
        params={
            'filter': "ge(reentry.epoch,epoch:'2016-11-01')",
            #'sort': '-reentry.epoch',
            "page[size]":100,
            "page[number]":i
        },
    )

    doc = response.json()
    if response.ok:
        print(i)
        #pprint(len(doc['data']))
        #pprint(doc['meta'])
    else:
        pprint(doc['errors'])

    
    for j in range(len(doc["data"])):
        doc["data"][j]["attributes"]["id"] = doc["data"][j]["id"]
        dic_attributes = doc["data"][j]["attributes"]
        dictionary_list.append(dic_attributes)
    time.sleep(3)
#pprint(dictionary_list)


df = pd.DataFrame(dictionary_list)
pprint(df)
df.to_excel("discos_database_re-entry_epoch_2016-11-01.xlsx")
