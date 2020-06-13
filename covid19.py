from plyer import notification
import requests
from bs4 import BeautifulSoup
import time


def notifyMe(title,message):
    notification.notify(
        title=title,
        message =message,
        app_icon="C://Users//prahl//Desktop//ExercisePy//Covid19Notificaation//icon.ico",
        timeout=6
    )

def getData(url):
    r=requests.get(url)
    return r.text

if __name__ =="__main__":
    while True:

       # notifyMe("Prahlad","hello")
        myHtmlData=getData("https://www.mohfw.gov.in/")

        soup = BeautifulSoup(myHtmlData, 'html.parser')
        # print(soup.prettify())
        myDataStr=""
        for tr in soup.find_all('tbody')[0].find_all('tr'):
            myDataStr += tr.get_text()

        myDataStr=myDataStr[1:]

        itemList = myDataStr.split("\n\n")

        states=['Maharashtra','Karnataka']
        for item in itemList[0:35]:
            dataList = item.split('\n')
            if dataList[1] in states:
                nTitle="Cases of Covid-19"
                nText= f"{dataList[1]}:\n Active Cases : {dataList[2]} \n Cured : {dataList[3]} \n Deaths : {dataList[4]}"
                notifyMe(nTitle,nText)
                time.sleep(2)

        time.sleep(3600)


