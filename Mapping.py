import requests
from bs4 import BeautifulSoup
session_requests = requests.session()


# numPages - the number of pages from Kijijii that are parsed
# city - name of the city the listings are being pulled from (must match a name in the dictionary below)
# Returns - an array of strings representing the URLs of each listing (each listing has its own page on Kijiji
def listings(city, numPages):
    arr = []
    
    # retrive general structure of url for kijiji page from city
    value = mapping[city]
    
    # array of url of pages that contain listings
    pages = map(lambda y: value[0] + str(y) + value[1], range(1, numPages + 1)) 
    
    # iterate through every page
    for x in pages:
        
        kijijii = session_requests.get(x)
        
        soup = BeautifulSoup(kijijii.text,'html.parser')
        
        # grab every tag that represents a listing on the page (tag can change over time)
        postings = soup.find_all("a", class_= "title ")
        
        # add every listing on the page to arr
        arr = arr + list(map(lambda v: "https://www.kijiji.ca" + v["href"], postings))
        
    return arr

# The following is a dictionary maintained to map each city to it's corresponding Kijijii URL
mapping = {
    "Toronto" : ["https://www.kijiji.ca/b-apartments-condos/gta-greater-toronto-area/page-", "/c37l1700272"]
    }