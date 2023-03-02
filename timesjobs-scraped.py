#import modules
import requests
from bs4 import BeautifulSoup
import pandas as pd
import time 

filter_skills = input('Enter the skill you want to filter out: ')   #skill you want to filter out

def find_jobs():
    url = "https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=python&txtLocation="
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html5lib')

    job_cards = soup.find('ul', class_="new-joblist")   #storing all job posts
    jobs = job_cards.find_all('li', class_="clearfix job-bx wht-shd-bx")    #storing all jobs as a list

    jobs_data = []  #empty list to store jobs data

    for job in jobs:
        date_posted = job.find('span', class_="sim-posted").span.text   #fetch date posted
        
        if 'few' in date_posted:    #check if its a recent job
            skills = job.find('span', class_="srp-skills").text.replace('\n','').replace(' ','')    #fetch skills
            
            if filter_skills=='':   #check if there is no skill to filter out 
                company = job.find('h3', class_="joblist-comp-name").text.replace('\n','').strip()
                experience = job.find('li').text[11:]    
                link = job.find('a').attrs['href']
                jobs_data.append([company, experience, skills, date_posted, link])
                
            elif filter_skills not in skills:   #filter out skill
                company = job.find('h3', class_="joblist-comp-name").text.replace('\n','').strip()
                experience = job.find('li').text[11:]    
                jobs_data.append([company, experience, skills, date_posted, link])
                link = job.find('a').attrs['href']


    #make dataframe from jobs data
    df = pd.DataFrame(jobs_data, columns = ['Company', 'Experience Req.', 'Skills', 'Date', 'Link'])

    #storing data in csv and excel file
    df.to_csv('jobs data.csv')
    df.to_excel('jobs data.xlsx')


if __name__=="__main__":
    while True:
        find_jobs()
        time_wait = 15  #time in minutes
        print('Waiting')
        time.sleep(time_wait * 60)
        