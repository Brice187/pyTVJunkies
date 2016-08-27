import requests, bs4
res = requests.get('https://kerick.net/python/episoden.xml')
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
    subRes=requests.get(subpage)
    subRes.raise_for_status()
    subSoup = bs4.BeautifulSoup(subRes.text,"html.parser")
    
    # open the showpage and present the downloadlinks
    
    
wantedShows=scrape_mainpage()
    
for key in wantedShows:
    print (wantedShows[key])