import requests
from bs4 import BeautifulSoup
url=""
name=""
price=""
link=""
names=[]
prices=[]
links=[]
full_deatils=""
with requests.session() as r:
    res=r.get("https://www.flipkart.com/",headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:66.0) Gecko/20100101 Firefox/66.0"})
    pop=res.text
    soup=BeautifulSoup(pop,features="html.parser")
    for k in soup.find_all('a',{"class":"_2AkmmA _1eFTEo"}):
        url+=k.get('href')+"\n"
    for n in url.split("\n"):
        if n!="":
            try:
                deal_res=r.get(n,headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:66.0) Gecko/20100101 Firefox/66.0"})
                deal_page=deal_res.text
                soup_deal=BeautifulSoup(deal_page,features="html.parser")
                for page in soup_deal.find_all("a",{"class":"K6IBc- required-tracking"}):
                    lol=r.get("https://www.flipkart.com"+page.get("href"),headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:66.0) Gecko/20100101 Firefox/66.0"})
                    fik=lol.text
                    fik_soup=BeautifulSoup(fik,features="html.parser")
                    for x in fik_soup.find_all("a",{"class":"_2mylT6"}):
                        name=x.text
                        link=x.get("href")
                        names.append(name)
                        links.append("https://www.flipkart.com"+link)
                    for m in fik_soup.find_all("a", {"class": "_2W-UZw"}):
                            count = 0
                            price2 = ""
                            for ter in m.text:
                                if count < 2:
                                    price2 += ter
                                    if ter == "₹":
                                        count += 1
                            price = price2[:-1]
                            prices.append(price)

            except:
                pass
for na,pr,ln in zip(names,prices,links):
    full_deatils+=na+"  "+pr+"\n"+ln+"\n"
print(full_deatils)