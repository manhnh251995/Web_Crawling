import requests
import json
import time

def Get_token_key(Path):
    with open("token","r") as f:
        token = f.read()
    return token 

def Get_list_from_place(lng,lat,radius,obj):
    token_key = Get_token_key("./token")
    while True :
        request_excute = requests.get("https://maps.googleapis.com/maps/api/place/nearbysearch/json?location={},{}&radius={}&type={}&key={}".format(lng,lat,radius,obj,token_key))
        page1 = request_excute.json()
        if "next_page_token" in page1.keys():
            l = page1["results"]
            break
    next_token = page1["next_page_token"]
    while True:
        time.sleep(10)
        while True :
            request_excute_tmp = requests.get("https://maps.googleapis.com/maps/api/place/nearbysearch/json?location={},{}&radius={}&type={}&key={}&pagetoken={}".format(lng,lat,radius,obj,token_key,next_token))
            page_tmp = request_excute_tmp.json()
            if "next_page_token" in page_tmp.keys():
                l2 = page_tmp["results"]
                break
        for i in l2:
            l.append(i)
        break
    return l
    
def List_result_place(l):
    list_result = []
    for i in l :
        data = "Name: \"{}\" ----- have -------Adress: \"{}\"  \n".format(i["name"] ,i["vicinity"])
        list_result.append(data)
    return list_result

def Get_list_all_point(key):
    while True:
        r3 = requests.get("https://maps.googleapis.com/maps/api/place/nearbysearch/json?location=21.021645,105.792128&radius=2000&type=restaurant&key={}".format(key))
        page3 = r3.json()
        if "next_page_token" in page3.keys():
            l = page3["results"]
            break
    time.sleep(10)
    while True:
        r4 = requests.get("https://maps.googleapis.com/maps/api/place/nearbysearch/json?location=21.021645,105.792128&radius=2000&type=bar&key={}".format(key))
        page4 = r4.json()
        if "next_page_token" in page4.keys():
            l1 = page4["results"]
            break
    for i in l1:
        l.append(i)
        time.sleep(10)
    while True:
        r5 = requests.get("https://maps.googleapis.com/maps/api/place/nearbysearch/json?location=21.021645,105.792128&radius=2000&type=beer&key={}".format(key))
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
        tmp2 = {"type": "Feature", "geometry": {"type": "Point", "coordinates": [i["geometry"]["location"]["lng"],i["geometry"]["location"]["lat"]]}, "properties": {"Address": i["vicinity"], "name": i["name"]}}
        tmp["features"].append(tmp2)
    return tmp

if __name__ == "__main__":
    lng = input("Enter longitude:  ")
    lat = input("Enter latitudei:  ")
    distance = input("Enter distance:  ")
    type_obj = input("Enter type:  ")
    print("Watting for load.....")
    with open("result","w") as f:
        for data in  List_result_place(Get_list_from_place(lng,lat,distance,type_obj)):
            f.write(data)
    with open("goole_map_bar_restaurant_beer22.geojson","w") as f:
        json.dump(import_value_into_json(Get_list_from_place(lng,lat,distance,type_obj)),f,ensure_ascii=False,indent=2)
