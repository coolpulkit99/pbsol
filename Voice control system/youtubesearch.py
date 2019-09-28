from bs4 import BeautifulSoup as bs
import requests as rs
import webbrowser
searchq="king of the clouds"
#if(1):
def playyt(searchq):
    searchq=searchq.replace(" ","+")

    url="https://www.youtube.com/results?search_query="+searchq#+"&page=&utm_source=opensearch"
    playstart(url)
def playstart(url):
    client=rs.get(url,'html.content')
    page = bs(client.content, 'html.parser')
    lis=page.find("a", {"class":"yt-uix-sessionlink spf-link"}) #,{"id":"contents"})
    webbrowser.open("https://www.youtube.com"+lis.get('href'))
