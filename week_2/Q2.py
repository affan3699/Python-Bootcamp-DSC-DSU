import requests
import csv
from bs4 import BeautifulSoup

handlers = []
temp = []

def getFacebookLikes():
    with open('FaceBookHandlers.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            if line_count == 0:
                line_count += 1
                continue
            else:
                handlers.append(row[0])
                line_count += 1

    for i in handlers:
        base_url = "https://www.facebook.com/"
        fbhandler = i
        finalLink = base_url + fbhandler
        response = requests.get(finalLink)
        soup = BeautifulSoup(response.content,'html.parser')
        f = soup.find('div', attrs={'class': '_4-u3 _5sqi _5sqk'})
        likes=f.find('span',attrs={'class':'_52id _50f5 _50f7'})
        print(f"{i} = {likes.text[1:-9]}")
        temp.append(likes.text[1:-9])

    with open('FaceBookHandlersWithLikes.csv', mode='w') as csv_file:
        csv_writer = csv.writer(csv_file, delimiter=',')
        csv_writer.writerow(["FB_PAGE_HANDLE", "LIKES"])
        for i in range(len(temp)):
        	csv_writer.writerow([handlers[i], temp[i]])

getFacebookLikes()