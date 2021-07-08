from bs4 import BeautifulSoup
from google.colab import files
import time
import requests
import csv
import os

existing_vjk_ids = []

def run(url, page_num):
    fw = open('/content/job_ads_ATL.txt', 'w', encoding='utf8')
    writer = csv.writer(fw, lineterminator='\n')
    page_count = -10
    count = 1
    for p in range(1, page_num + 1):
        page_count = page_count + 10
        print('page ', p)
        page_html = None
        page_url_link = url + str(page_count)
        for i in range(5):
            time.sleep(5)
            page_response = requests.get(page_url_link)
            if page_response:
                break
        if not page_response:
            print('No Response for page')
        page_html = page_response.text
        page_soup = BeautifulSoup(page_html, features="html.parser")
        vjk_ids = [element['data-jk'] for element in page_soup.findAll('div', {'class':'jobsearch-SerpJobCard unifiedRow row result'})]
        for vjk_id in vjk_ids:
            print(vjk_id)
            if vjk_id in existing_vjk_ids:
                continue
            else:
                existing_vjk_ids.append(vjk_id)
            job_url_link = 'https://www.indeed.com/viewjob?jk=' + vjk_id
            for i in range(5):
                time.sleep(5)
                job_response = requests.get(job_url_link)
                if job_response:
                    break
            if not job_response:
                print('No Response for job')
            job_html = job_response.text
            with open('/content/html_files_ATL/output' + str(vjk_id) + '.html', 'w', encoding='utf-8') as f:
                f.write(job_html)
            job_title, job_text = 'NA', 'NA'
            job_soup = BeautifulSoup(job_html, features="html.parser")
            job_title = job_soup.find('h1', {'class':'jobsearch-JobInfoHeader-title'})
            job_text = job_soup.find('div', {'class':'jobsearch-jobDescriptionText'})
            try:
                writer.writerow([job_text.text.replace("\n","").strip(),job_title.text])
                count = count + 1
                print(count)
                if page_count >= 5001:
                    fw.close()
                    return
            except:
                print('caught exception')

url='https://www.indeed.com/jobs?q=title%3A%28Software+Engineer%29&l=Atlanta%2C+GA&radius=25&sort=date&start='

run(url,1000)
