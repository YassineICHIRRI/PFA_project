from bs4 import BeautifulSoup as bs
import requests 

url = "http://www.wikicfp.com/cfp/home"
response = requests.get(url)
html = response.content
soup = bs(html, 'lxml')

table = soup.find('table', {'cellpadding': '3','width':'100%'})
rows = table.find_all('tr')[1:]

for row in rows:
    cols = row.find_all('td')
    title0 = cols[0].text.strip()
    title1 = cols[1].text.strip()
    title2 = cols[2].text.strip()
    print(title0,title1,title2 ,"\n")
