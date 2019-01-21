import requests
import time
import json

url = "https://graph.facebook.com"

def Get_token_key(Path):
    with open("token","r") as f:
        token = f.read()
    return token

def Get_list_place(oj,lng,lat,radius):
    token_key = Get_token_key("./token")
    url_version = "/v3.2"
    url_endpoint = "/search?type=place&q={}&center={},{}&distance={}&limit=100&fields=name,checkins,picture,link,location&access_token={}".format(oj,lng,lat,radius,token_key)
    get_requests = requests.get( url + url_version + url_endpoint )
    json_file = get_requests.json()
    list_result = []
    for i in json_file["data"]:
        list_result.append(i)

    return list_result

def List_result_place(l):
    list_result = []
    for i in l :
        try:
            data = "Name: \"{}\" ----- have -------Adress: \"{}\"-----linkFacebook-----{} \n".format(i["name"] ,i["location"]["street"],i["link"])
        except KeyError as e:
            data = "Name: \"{}\" ----- not find Adress-----linkFacebook-----{} \n".format(i["name"],i["link"])
            continue
        else:
            list_result.append(data)
        
    return list_result

def import_value_into_json(l):
    tmp = {"type": "FeatureCollection", "features": []}
    for i in l:
        try :
            tmp2 = {"type": "Feature", "geometry": {"type": "Point", "coordinates": [i["location"]["longitude"],i["location"]["latitude"]]}, "properties": {"Address": i["location"]["street"], "name": i["name"]}}
        except KeyError as e:
            tmp2 = {"type": "Feature", "geometry": {"type": "Point", "coordinates": [i["location"]["longitude"],i["location"]["latitude"]]}, "properties": {"Address": i["link"], "name": i["name"]}}
            continue
        else:
            tmp["features"].append(tmp2)

    return tmp


if __name__=="__main__":
    menu = ["coffee", "tea", "lau", "BBQ", "tra da"]
    for food in menu:
        with open("{}".format(food),"w") as f:
            f.write("-------------{}---------------\n".format(food))
            for data in  List_result_place(Get_list_place(food,"20.999838","105.807647","1000")):
                f.write(data)
    for food in menu:
        with open("facebook_google_map_{}.geojson".format(food),"w") as f:
            json.dump(import_value_into_json(Get_list_place(food,"20.999838","105.807647","1000")),f,ensure_ascii=False,indent=2)

       
