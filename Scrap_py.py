from bs4 import BeautifulSoup as bs
import requests
import csv

url = "http://www.wikicfp.com/cfp/home"
response = requests.get(url)
html = response.content
soup = bs(html, 'lxml')

table = soup.find('table', {'cellpadding': '3','width':'100%'})
rows = table.find_all('tr')[1:]
i=0
Titles = []
Links=[]
Desc= []
Date= []
Location= []
Deadline= []
for row in rows:
    cols = row.find_all('td')
    if i%2==0:
        title= cols[0].text.strip()
        Titles.append(title)
        link=cols[0].find("a").get("href")
        Links.append("http://www.wikicfp.com"+link)
        description=cols[1].text.strip()
        Desc.append(description)
        i+=1
    else:
        date=cols[0].text.strip()
        location=cols[1].text.strip()
        deadline=cols[2].text.strip()
        Date.append(date)
        Location.append(location)
        Deadline.append(deadline)
        i+=1

file_name="CFP.csv"

with open(file_name,"w",encoding='utf-8') as f :
    f.write=csv.writer(f)
    f.write.writerow(['No','Title','Decription','Location','Date','Deadline'])

    for i in range(len(Titles)):
        f.write.writerow([i+1,'=HYPERLINK("{}","{}")'.format(Links[i],Titles[i]),Desc[i],Location[i],Date[i],Deadline[i]])
