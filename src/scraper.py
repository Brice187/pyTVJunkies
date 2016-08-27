import requests, bs4
res = requests.get('http://serienjunkies.org/xml/feeds/episoden.xml')
res.raise_for_status()
sJSoup = bs4.BeautifulSoup(res.text,"html.parser")

def scrape_mainpage():
    titlesAndLinksdict = {}
    to_ignore=['[DEUTSCH]','[ENGLISCH]','[TV-FILM]']
    for entry in sJSoup.find_all('item'):
        title_string = entry.title.string
        for item in to_ignore:
            title_string=title_string.replace(item,'')
            title_string=title_string.split('.')
            title_string=' '.join(title_string)
            titlesAndLinksdict[title_string]=entry.link.string
    return titlesAndLinksdict

def scrape_subpage(subpage):
    hoster='ul_'                    #ul_ = Uploaded / so_ = share-online
    quality='1080p'
    downloadLinks=[]
    subRes=requests.get(subpage)
    subRes.raise_for_status()
    subSoup = bs4.BeautifulSoup(subRes.text,"html.parser")
    
    for item in subSoup.find_all('a'):
        actualLink=item.get('href')
        if actualLink.startswith('http://download'):
            if hoster in actualLink:
                if quality in actualLink:
                    downloadLinks.append(actualLink)
                
    print (downloadLinks)
    # open the showpage and present the downloadlinks
    

availableShows=scrape_mainpage()
desiredShow=input("Please put in a (part-)title of the Show: ")

for show in availableShows:
    if desiredShow in show:
        scrape_subpage(availableShows[show])
        break


"""  

    
for key in wantedShows:
    print (wantedShows[key])"""