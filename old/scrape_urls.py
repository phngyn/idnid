import os
import json
from urllib.request import urlopen
from bs4 import BeautifulSoup as bs

BASE_URL = "https://www.idonowidont.com"

dir_path = os.path.dirname(os.path.realpath(__file__))
ring_src = dir_path + "\\ring_src.txt"

markets = []

with urlopen(BASE_URL + "/marketplace/") as client:
    page_html = client.read()
    soup_html = bs(page_html, "html.parser")
    marketplace = soup_html.find_all("div", {"class":"button-cell"})
    for marks in marketplace:
        markets.append(marks.a["href"])

for marks in markets:
    # print(BASE_URL + i)

    #Find the last page on the website to know our loop range
    with urlopen(BASE_URL + marks) as client:
        page_html = client.read()
        soup_html = bs(page_html, "html.parser")
        try:
            last_page_url = soup_html.find("li", {"class":"pager__item pager__item--last"}).a["href"]
            # not sure why last page is off by -1, so we add 1
            last_page = int(last_page_url[-2:]) + 1
        except:
            last_page = 0

    # Loop through list of pages to gather all ring post url
    # and add url to our ring_src if it's not in the file
    for i in range(0, last_page + 1):
        if i == 0:
            MY_URL = BASE_URL + marks
        else:
            MY_URL = BASE_URL + marks + "?page=" + str(i)
        print(MY_URL)

        with urlopen(MY_URL) as client:
            page_html = client.read()
            soup_html = bs(page_html, "html.parser")
            container_posting = soup_html.find_all("div", {"class":"ds-1col"})
            
        for posts in container_posting:
            post_url = posts.div.a["href"]
            with open(ring_src, "r+") as file:
                if post_url in file.read():
                    print( "Exists:", post_url)
                else:
                    file.write(post_url + "\n")
                    print( "Added:", post_url) 