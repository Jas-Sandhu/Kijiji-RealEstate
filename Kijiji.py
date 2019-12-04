import RealEstate
import pandas

def main():
    file = "INSERT FILE PATH HERE"
    city = "Toronto"
    pages = 10
    
    data = RealEstate.kijiji(city, pages)
    
    pandas.DataFrame(data[1:], columns=data[0]).to_csv(file, index = False)


if __name__ == "__main__":
    main()