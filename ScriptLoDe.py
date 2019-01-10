from sys import argv
import requests
from bs4 import BeautifulSoup

sys,name = argv

url = "https://ketqua.net/"

def result_lo_de(url):
    res = requests.get(url)
    soup = BeautifulSoup(res.text)
    tbody = soup.find("tbody")
    tr = tbody.findAll("tr")
    l = []
    for td in tr:
        td = td.findAll("td")
        l2 =[]
        for rs in td:
            if rs.text.isdigit():
                l2.append(rs.text[-2:])
            else:
                l2.append(rs.text)           
        l.append(l2)
    for kq in l:
        if kq[0] == '':
            kq[0] = l[l.index(kq)-1][0]
    return l

def get_number_from_result_lo_de(url):
    tmp = result_lo_de(url)
    list_tmp = []
    for i in tmp:
        for num in i:
            if num.isdigit():
                list_tmp.append(num)
    return list_tmp

def check_number_have_in_result(number,url):
    list_number= get_number_from_result_lo_de(url)
    list_kq_and_number = result_lo_de(url)
    if str(number) in list_number:
        for i in list_kq_and_number:
            if str(number) in i:
                print("chicken dinner ban đa trúng lô đề với số  {} và giải {}".format(number,i[0]))
                print("Truy cập đườn dẫn {} để xem thông tin chi tiết và các giải khác".format(url)) 
            else:
                continue
    else:
        print("Rất tiếc hôm nay bạn đã tạch lô đề .Chúc bạn may mắn lần sau")
        for i in list_kq_and_number:
            print(i)
if __name__ == "__main__":
    check_number_have_in_result(argv[1],url)
                  
