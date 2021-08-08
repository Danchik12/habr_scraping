#loading libraries
import requests
from fake_useragent import UserAgent
from bs4 import BeautifulSoup
import dubl
import csv
import numpy as np

UserAgent().chrome
def response(page_link):
    #Returns links to articles and their titles
    response=requests.get(page_link)
    html=response.content
    soup=BeautifulSoup(html,"html.parser")
    obj=soup.findAll(lambda tag:tag.name=="a" and tag.get("class")==['tm-article-snippet__title-link'])
    post_link=["https://habr.com"+link.attrs['href'] for link in obj]
    text=[post.text for post in obj]
    print(text)
    return post_link,text


def main():
    
    page_number=1
    
    #Passes through all pages    
    for page_number in range(60):
        page_link="https://habr.com/ru/page{}/".format(page_number)
        post_link,text=response(page_link)
        #   Saves information to csv file with delimiter ','
        with open('data.csv', 'a+',newline="",encoding="utf-8-sig") as f:
            writer = csv.writer(f)
            writer.writerows(zip(text, post_link))
                
    #Remove duplicates in csv file         
    dubl.write_lines("data.csv")

            
   
if __name__=="__main__":
    main()
    
    

