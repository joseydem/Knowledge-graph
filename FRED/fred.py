import requests
import json
import pandas as pd
import time

df = pd.read_csv('bertowy_model_med_food_together.csv')
df.drop('Unnamed: 0', axis=1, inplace=True)

text_list = []
final_list = []

for i in range(len(df)):
    text_list.append(df['text'][i])

headers = {
    "Accept": "application/rdf+xml",
    "Authorization": "Bearer 6ba05c92-fce3-34d2-aeee-44c4cab46dbd",
}

for i in range(len(text_list)):
    print("Numer:", i+1)
    text = text_list[i]
    url = 'http://wit.istc.cnr.it/stlab-tools/fred?text={}'.format(requests.utils.quote(text))
    response = requests.get(url, headers=headers)

    if response.status_code != 500:

        result = response.content
        print(result)

        with open("fred/rdf_xml.xml", "w") as fd:
            fd.write(response.text)

        final_list.append(result)
        print('Dodano do listy')
    else:
        print("Error 500.")

    print("Done.")
    time.sleep(15)

def load_data(file):
    with open(file) as f:
      data = json.load(f)
    return(data)

def save_data(file, data):
    with open(file, 'w', encoding="utf-8") as f:
        json.dump(data, f, indent = 4)

