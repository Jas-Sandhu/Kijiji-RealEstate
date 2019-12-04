import requests
import Mapping
import Retrieve
from bs4 import BeautifulSoup

session_requests = requests.session()

def kijiji(city, pages): 

    listings = Mapping.listings(city, pages)
    
    condodata = []
    
    #Headers for condodata array
    condodata.append(['URL', 'Address', 'Price', 'Date', 'Bedroom', 
                      'Bathroom', 'Furnished', 'PostalCode', 'Postal_Top', 'Postal_Bottom', 
                      'Square Feet'])
    
    # Pulls "market data" from each listing
    for post in listings:
        
        kijijii = session_requests.get(post)
        
        soup = BeautifulSoup(kijijii.text,'html.parser')
        
        data = soup.find_all("dt", class_="twoLinesLabel-3766429502")
        
        info = Retrieve.datapoints(data)
        
        x = Retrieve.location(soup)
        print(x)
        
        postalcode = Retrieve.postal(x)
    
        y = Retrieve.price(soup)
        
        z = Retrieve.dateposted(soup)
        
        condodata.append([post, x, y, z, info.setdefault('Bedrooms','Error'), 
                          info.setdefault('Bathrooms','Error'), info.setdefault('Furnished','Error'), postalcode, postalcode[:3], postalcode[-3:], 
                          info.setdefault('Sqft','Error')])
        
    return condodata
