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

def datapoints(data):
    info = {}
    
    for point in data:
        check = point.string
        
        if (check) == "Unit Type":
            info["Type"] = point.nextSibling.string
        
        if (check) == "Bedrooms":
            info[check] = point.nextSibling.string        
        
        elif (check) == "Bathrooms":
            info[check] = point.nextSibling.string
            
        elif (check) == "Utilities Included":
            info["Hydro"] = point.nextSibling.string
            info["Heat"] = point.nextSibling.nextSibling.string
            info["Water"] = point.nextSibling.nextSibling.nextSibling.string        
            
        elif (check) == "Also Included":
            info["Cable"] = point.nextSibling.string
            info["Internet"] = point.nextSibling.nextSibling.string
            info["Landline"] = point.nextSibling.nextSibling.nextSibling.string         
            
        elif (check) == "Parking Included":
            info["Parking"] = point.nextSibling.string
            
        elif (check) == "Agreement Type":
            info["Agreement"] = point.nextSibling.string
        
        elif (check) == "Move-In Date":
            info["MoveInDate"] = point.nextSibling.string  
            
        elif (check) == "Pet Friendly":
            info["Pet"] = point.nextSibling.string          
        
        elif (check) == "Size (sqft)":
            info['Sqft'] = point.nextSibling.string.replace(",","")         
        
        elif (check) == "Furnished":
            info[check] = point.nextSibling.string
            
        elif (check) == "Appliances":
            info["Laundry_In"] = point.nextSibling.string
            info["Laundry_Out"] = point.nextSibling.nextSibling.string         
            
        elif (check) == "Air Conditioning":
            info["AirConditioning"] = point.nextSibling.string
        
        elif (check) == "Smoking Permitted":
            info["Smoking"] = point.nextSibling.string
    
        elif (check) == "Personal Outdoor Space":
            info["Yard"] = point.nextSibling.string
            info["Balcony"] = point.nextSibling.nextSibling.string

    return info