# Jobs-scraped-data

Scraper for website "timesjobs".
This is a python program to scrape job posts for the following information:
1. Company name,
2. Experience Required,
3. Skills Required,
4. Publised date, and
5. Link to the job post.

The user will enter the URL of the website with job posts. Moreover, the program will only scrape data of recent jobs only. This functionality was achieved by a condition that the published date should has the word 'few' in it. The program can also filter out skill that you are unfamiliar with. The scraped data will be saved in a CSV and Excel file.
Lastly, the program will wait 15 minutes (can be changed) until it scrapes the data again. 
