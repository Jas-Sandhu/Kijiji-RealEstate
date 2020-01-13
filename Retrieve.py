import re

def dateposted(soup):
    try:
        date = soup.find_all("div", class_="datePosted-383942873")
        date = date[0].find("time")["title"]
        date = date.replace(",","")
    except:
        date = "Error"
    return date

def price(soup):
    try:
        price = soup.find_all("span", class_="currentPrice-2842943473")                
        price = price[0].string
        price = price.replace(",","")
        price = price.replace("$","")
    except:
        price = 0
    return str(price)

def postal(address):
    try:
        code = re.search('[A-z][0-9][A-z][0-9][A-z][0-9]|[A-z][0-9][A-z][ ][0-9][A-z][0-9]|[A-z][0-9][A-z]', address).group(0)
        code = code.replace(" ","")
    except:
        code = "Error"
    return code

def location(soup):
    try:
        address = soup.find_all("span", class_='address-3617944557')
        address = address[0].string
        address = address.replace(",","")
    except:
        address = "Error"
    return address

def datapoints(soup):
    info = {}
    
    data = soup.find_all("dt", class_="twoLinesLabel-3766429502")
    
    for point in data:
        
        check = point.string
        
        if (check) == "Unit Type":
            info["UnitType"] = point.nextSibling.string
        
        elif (check) == "Bedrooms":
            info[check] = point.nextSibling.string        
        
        elif (check) == "Bathrooms":
            info[check] = point.nextSibling.string        
            
        elif (check) == "Parking Included":
            info["Parking"] = point.nextSibling.string
            
        elif (check) == "Agreement Type":
            info["AgreementType"] = point.nextSibling.string
        
        elif (check) == "Move-In Date":
            info["MoveInDate"] = point.nextSibling.string  
            
        elif (check) == "Pet Friendly":
            info["PetFriendly"] = point.nextSibling.string          
        
        elif (check) == "Size (sqft)":
            info['SquareFeet'] = point.nextSibling.string.replace(",","")         
        
        elif (check) == "Furnished":
            info[check] = point.nextSibling.string       
            
        elif (check) == "Air Conditioning":
            info["AirConditioning"] = point.nextSibling.string
        
        elif (check) == "Smoking Permitted":
            info["Smoking"] = point.nextSibling.string
            
        data = soup.find_all("svg", class_="icon-459822882 yesNoIcon-2594104508")
        data = data + soup.find_all("svg", class_="icon-459822882 yesNoIcon-2594104508 yesIcon-3014691322")

        for point in data:
            
            check = point['aria-label'].split(':')[1].strip()
            
            value = point['aria-label'].split(':')[0].strip()
            
            if check == 'Laundry (In Unit)':
                info["LaundryIn"] = value
            
            elif check == "Laundry (In Building)":
                info["LaundryOut"] = value
            
            elif (check) == "Hydro":
                info["Hydro"] = value
                
            elif (check) == "Heat":
                info["Heat"] = value
                
            elif (check) == "Water":
                info["Water"] = value        
                
            elif (check) == "Cable / TV":
                info["Cable"] = value
            
            elif (check) == "Internet":
                info["Internet"] = value
            
            elif (check) == "Landline":
                info["Landline"] = value
        
            elif (check) == "Yard":
                info["Yard"] = value
                
            elif (check) == "Balcony":
                info["Balcony"] = value
                
    return info
