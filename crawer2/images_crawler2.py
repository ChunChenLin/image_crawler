import requests
from bs4 import BeautifulSoup
import shutil

sample_page = raw_input("Please enter an URL of the sample images page:")
product_name = sample_page.split('/')[-2]

print("Please enter type(ex: JPG,CR2,RAW...)")
type1 = raw_input("TYPE1:")
type2 = raw_input("TYPE2:")

res = requests.get(sample_page)
#print res.text
soup = BeautifulSoup(res.text)

url = 'http://216.18.212.226/PRODS/' + product_name + '/FULLRES/'
for img in soup.select('img'):
    if "."+type1 in img['src'].split('/')[-1]:
        fname = img['src'].split('/')[-1]
        img_url = url + fname
        print img_url
        res2 = requests.get(img_url, stream=True)
        f = open(fname, 'wb')
        shutil.copyfileobj(res2.raw, f)
        f.close()
        del res2
for img in soup.select('a'):
    if "."+type2 in img['href']:
        #print img['href'].split('.')[0]+".CR2"
        fname = img['href'].split('.')[0]+".CR2"
        img_url = url + fname
        print img_url
        res2 = requests.get(img_url, stream=True)
        f = open(fname, 'wb')
        shutil.copyfileobj(res2.raw, f)
        f.close()
        del res2