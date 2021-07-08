# importing the libraries
from bs4 import BeautifulSoup
import re
import csv
import time
import requests

def run(url,pageNum):
    fw=open('reviews_interstellar.txt','w',encoding='utf8')
    
    writer=csv.writer(fw,lineterminator='\n')
    
    for p in range(1,pageNum+1):
        
        print('page',p)
        html='None'
        
        if p==1: pageLink=url # url for page 1
        else: pageLink=url+'?type=&sort=&page='+str(p)# make the page url
        
        for i in range(5):
            response=requests.get(pageLink,headers = { 'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36', })
            if response: # explanation on response codes: https://realpython.com/python-requests/#status-codes
                break # we got the file, break the loop
            else:time.sleep(2) # wait 2 secs
        if not response: return None
            
        html=response.text
        
        soup = BeautifulSoup(html,'lxml')
        
        reviews=soup.findAll('div', {'class':'row review_table_row'}) # get all the review divs
        
        for review in reviews:
            
            #Critic name
            critic,rating,source,text,date='NA','NA','NA','NA','NA'
            criticChunk=review.find('a',{'href':re.compile('/critic/')})
            if criticChunk: critic=criticChunk.text.strip() 
            
            #ratings
            
            ratingChunk=review.find('div',{'class':re.compile('fresh')})
            if ratingChunk: rating='fresh'
            
            ratingChunk=review.find('div',{'class':re.compile('rotten')})
            if ratingChunk: rating='rotten'
            
            #Source
            
            sourceChunk=review.find('em',{'class':'subtle critic-publication'})
            if sourceChunk: source=sourceChunk.text.strip()
            
            #Text
            
            textChunk=review.find('div',{'class':'the_review'})
            if textChunk: text=textChunk.text.strip()
            
            #date
            
            dateChunk=review.find('div',{'class':'review-date subtle small'})
            if dateChunk: date=dateChunk.text.strip()
            
            writer.writerow([critic, rating, source, text, date]) # write to file 
            
    fw.close()
    
    
url='https://www.rottentomatoes.com/m/interstellar_2014/reviews'
run(url,2)