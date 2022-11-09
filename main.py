from bs4 import BeautifulSoup
import requests
from lxml import etree
import pandas as pd

url= "http://books.toscrape.com/catalogue/sophies-world_966/index.html"
# expresion xpath para traer la descripcion del producto
#//article[@class= 'product_page']//p[not(@id) and not(@class)]
page = requests.get(url)
#print(page)

soup = BeautifulSoup(page.content, 'html.parser')
documentObjectModel = etree.HTML(str(soup))
product_description = documentObjectModel.xpath("//article[@class='product_page']//p[not(@id) and not(@class)]")

product_description = product_description[0].text


#expresion para traer datos de la tabla
# //table[@class='table table-striped']//tr//text()

table_data = documentObjectModel.xpath("//table[@class='table table-striped']//tr//text()")
print(type(table_data))

print(table_data)


clean_data = []
for elemento in table_data:
    if elemento != '\n':
        clean_data.append(elemento)
        
print("LISTA DE ITEMS DE LA TABLA")
print(clean_data)

table_data_dict = {}

it = iter(clean_data)
res_dct = dict(zip(it, it))

print("DICCIONARIO ESTRUCTURADO")
res_dct["product_description"] = product_description
df = pd.DataFrame(res_dct, index=[0])
df.to_csv("RESULTADOS_FINALES.csv")

