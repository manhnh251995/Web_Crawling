import requests
import json
import time


def Get_list_all_point():
    while True:
        r3 = requests.get("https://maps.googleapis.com/maps/api/place/nearbysearch/json?location=21.021645,105.792128&radius=2000&type=restaurant&key=AIzaSyDGfat_Ogi_Q9maQlwJMipl5R-UTV83W5M")
        page3 = r3.json()
        if "next_page_token" in page3.keys():
            l = page3["results"]
            break
    time.sleep(10)
    while True:
        r4 = requests.get("https://maps.googleapis.com/maps/api/place/nearbysearch/json?location=21.021645,105.792128&radius=2000&type=bar&key=AIzaSyDGfat_Ogi_Q9maQlwJMipl5R-UTV83W5M")
        page4 = r4.json()
        if "next_page_token" in page4.keys():
            l1 = page4["results"]
            break
    for i in l1:
        l.append(i) 
        time.sleep(10)
    while True:
        r5 = requests.get("https://maps.googleapis.com/maps/api/place/nearbysearch/json?location=21.021645,105.792128&radius=2000&type=beer&key=AIzaSyDGfat_Ogi_Q9maQlwJMipl5R-UTV83W5M")
        page5 = r5.json()
        if "next_page_token" in page5.keys():
            l2 = page5["results"]
            break
    for i in l2:
        l.append(i)
    return l

def import_value_into_json(l):
    tmp = {"type": "FeatureCollection", "features": []}
    for i in l:
        tmp2 = {"type": "Feature", "geometry": {"type": "Point", "coordinates": [i["geometry"]["location"]["lng"],i["geometry"]["location"]["lng"]]}, "properties": {"Address": i["vicinity"], "name": i["name"]}}
        tmp["features"].append(tmp2)
    return tmp    

if __name__ == "__main__":
    with open("goole_map_bar_restaurant_beer22.geojson","w") as f:
        json.dump(import_value_into_json(Get_list_all_point()),f,ensure_ascii=False,indent=2)


