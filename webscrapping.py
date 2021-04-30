#project 2: web scrapping  using beautifulSoup 4 and requests

import requests
from bs4 import BeautifulSoup
import pandas
import argparse
import connect

parser=argparse.ArgumentParser()
parser.add_arguement("--page_num_max", help="enter the number of pages to parse", type=int)
parser.add_arguement("--dbname", help="Enter the name of db", type=str)
args=parser.parse_args()

oyo_url ="https://www.oyorooms.com/hotels-in-mumbai/?page="
page_num_MAX=3
scrapped_info_list=[]
connect.connect(args.dbname)

for page_num in range (1,page_num_MAX):
    url=oyo_url+ str(page_num)
    print("GET Requests for:"+url)
    req= requests.get(url)
    content=req.content

    soup = BeautifulSoup(content,"html.parser")

    all_hotels = soup.find_all("div",{"class":"hotelCardListing"})

    for hotel in all_hotels:
        hotel_dict = {}
        hotel_dict["name"]=hotel.find("h3",{"class":"listingHotelDescription__hotelName"}).text
        hotel_dict["address"]=hotel.find("span",{"itemprop":"streetAddress"}).text
        hotel_dict["price"]=hotel.find("span",{"class": "listiingPrice__finalPrice"}).text
        #try ... except
        try:
            hotel_dict["rating"]=hotel.find("span",{"class":"hotelRating__ratingSummary"}).text
        except AttributeError:
            hotel_dict["rating"]=None
        parent_amenities_elements= hotel.find("div",{"class":"amenityWrapper"})
        amenities_list=[]
        for amenity in parent_amenities_elements.find_all("div",{"class":"amenityWrapper__amenity"}):
            amenities_list.append(amenity.find("span", {"class":"d-body-smd-textEllipsis"}).text.strip())
        hotel_dict["amenities"]=','.join(amenities_list[:-1])
        scrapped_info_list.append(hotel_dict)
        connect.insert_into_table(args.dbname,tuple(hotel_dict.value()))
        # print(hotel_name,hotel_address,hotel_price,hotel_rating)
dataFrame = pandas.DataFrame(scrapped_info_list)
print("creating csv file...")
dataFrame.to_csv("Oyo.csv")
connect.get_hotel_info(args.dbname)
