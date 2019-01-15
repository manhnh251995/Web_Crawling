from collections import Iterable
import requests
from sys import argv
lable = argv[2]
number = argv[1]

def Get_json_from_lable(lable):
    url = "https://api.stackexchange.com/2.2/questions?order=desc&max=1&sort=votes&tagged={}&site=stackoverflow".format(lable)
    res = requests.get(url)
    file_json = res = res.json()
    return file_json

def Get_number_question_high_vote(number,lable): 
    file_json = Get_json_from_lable(lable)
    l = []
    if file_json["items"] == [] :
        print("No questions found matching {}".format(lable))
    else:
        for i in file_json["items"] :
            title = i["title"]
            link = i["link"]
            l.append((title,link))
    return l[:int(number) + 1]

if __name__ == "__main__":
    print("Top {} Questions {} have hight vote ".format(number,lable))
    print("\n")
    for title,link in Get_number_question_high_vote(number,lable):
        print("Questions: {}----link :{}".format(title,link))
