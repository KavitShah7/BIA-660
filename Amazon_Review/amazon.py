from selenium import webdriver
import time
import csv
import operator
import re

def scrape(url):
    driver=webdriver.Chrome("./chromedriver")
    driver.get(url)
    time.sleep(3)
    
    fw=open("reviews.csv", "w", encoding="utf8")
    writer=csv.writer(fw, lineterminator= "\n")
    
    driver.find_element_by_partial_link_text("ratings").click()
    time.sleep(3)
    driver.find_element_by_partial_link_text("See all reviews").click()
    time.sleep(3)
    newLink=True
    while newLink:
        reviews=driver.find_elements_by_css_selector('div[data-hook="review"]')
        
        
        for review in reviews:
            txt,star="N/A","N/A"
            try:
                txt= review.find_element_by_css_selector("div.a-row.a-spacing-small.review-data").text
            except:
                print("no text")
                
            try:
                try:
                    stars= review.find_element_by_css_selector('i[data-hook="review-star-rating"]')
                    star=stars.get_attribute("class")
                    star = str(star)[26:27]
                
                except:
                    stars = review.find_element_by_css_selector('i[data-hook="cmps-review-star-rating"]')
                    star = stars.get_attribute("class")
                    star = str(star)[26:27]
                    
            except:
                print("No Text")
                
            writer.writerow([txt,star])
        
        try:
            driver.find_element_by_partial_link_text("Next page").click()
            time.sleep(3)
        except:
            newLink = False
    fw.close()
    
    
scrape("https://www.amazon.com/Sennheiser-Momentum-Cancelling-Headphones-Functionality/dp/B07VW98ZKG")
                







  
  
    