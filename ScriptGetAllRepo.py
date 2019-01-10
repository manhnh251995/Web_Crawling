from sys import argv
import requests
from bs4 import BeautifulSoup

sys,name = argv

def get_repo_github_from_name(name):
    url = "https://github.com/{}?tab=repositories".format(name)
    res = requests.get(url)
    soup = BeautifulSoup(res.text)
    ul = soup.find("ul",{"data-filterable-for":"your-repos-filter"})
    li = ul.findAll("li",{"class":"col-12 d-flex width-full py-4 border-bottom public source"})
    list_repo=[]
    for a in li:
        a = a.find("a")
        repo = a.attrs["href"]
        list_repo.append(repo[repo.rfind("/") + 1:])
    return list_repo

if __name__ == "__main__":
    for repo in get_repo_github_from_name(argv[1]):
        print(repo)
