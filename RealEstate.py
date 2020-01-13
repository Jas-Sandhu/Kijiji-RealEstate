import requests
import Mapping
import Retrieve
from bs4 import BeautifulSoup

def kijiji(city, pages): 

    listings = Mapping.listings(city, pages)
    
    condodata = []
    
    #Headers for condodata array
    condodata.append(['URL', 'Address', 'UnitType', 'AgreementType', 'Price', 'Date', 'MoveInDate', 'SquareFeet', 
                      'Bedrooms', 'Bathrooms', 'Furnished', 'PostalCode', 'PostalTop', 'PostalBottom',   
                      'Hydro', 'Heat', 'Water', 'Cable', 'Internet', 'LaundryIn', 'LaundryOut', 
                       'Parking', 'Landline', 'AirConditioning', 'PetFriendly', 'Smoking', 'Yard', 'Balcony'])
    
    # Pulls "market data" from each listing
    for post in listings:
        
        kijijii = requests.get(post)
        
        soup = BeautifulSoup(kijijii.text,'html.parser')
        
        info = Retrieve.datapoints(soup)
        
        address = Retrieve.location(soup)
        
        print(address)
        
        postalcode = Retrieve.postal(address)
    
        price = Retrieve.price(soup)
        
        date = Retrieve.dateposted(soup)
        
        condodata.append([post, address, info.setdefault(condodata[0][2],'NA'), info.setdefault(condodata[0][3],'NA'), price,
                          date, info.setdefault(condodata[0][6],'NA'), info.setdefault(condodata[0][7],'NA'),
                          
                          info.setdefault(condodata[0][8],'NA'), info.setdefault(condodata[0][9],'NA'), info.setdefault(condodata[0][10],'NA'),
                          postalcode, postalcode[:3], postalcode[-3:],
                          
                          info.setdefault(condodata[0][14],'NA'), info.setdefault(condodata[0][15],'NA'), info.setdefault(condodata[0][16],'NA'),
                          info.setdefault(condodata[0][17],'NA'), info.setdefault(condodata[0][18],'NA'), info.setdefault(condodata[0][19],'NA'),
                          
                          info.setdefault(condodata[0][20],'NA'), info.setdefault(condodata[0][21],'NA'), info.setdefault(condodata[0][22],'NA'),
                          info.setdefault(condodata[0][23],'NA'), info.setdefault(condodata[0][24],'NA'), info.setdefault(condodata[0][25],'NA'),
                          
                          info.setdefault(condodata[0][26],'NA'), info.setdefault(condodata[0][27],'NA')])
    return condodata
