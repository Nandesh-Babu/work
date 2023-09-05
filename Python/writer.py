from google.cloud import bigquery
import os
credentials_path='/My Catalogue/Mycode C/pythonjson/pybigquery.json'
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = credentials_path

client = bigquery.Client()
table_id='qwiklabs-gcp-04-2b27879691fe.Fruitshop.Types of Fruit'

rows_to_insert=[
    {u'FruitName':'Apple',u'QuantityinKG': 40, u'PriceperKG':100}
    {u'FruitName':'Apple',u'QuantityinKG': 40, u'PriceperKG':100}
]
errors=client.insert_rows_json(table_id, rows_to_insert)
if errors == []:
    print("added")
else:
    print("not added")
