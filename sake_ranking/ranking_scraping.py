import requests
from bs4 import BeautifulSoup

def get_sake_ranking(page_url):
    ranking=[]
    try:
        response=requests.get(page_url,timeout=10)
        response.encoding=response.apparent_encoding
        soup=BeautifulSoup(response.text, "html.parser")

    except Exception as e:
        print("hi")
    return 0


if __name__=="__main__":
    data=get_sake_ranking("https://www.saketime.jp/ranking/")
    print(len(data)+"件取得しました")
    for i in data:
        print(i)