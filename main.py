from bs4 import BeautifulSoup
import csv
import requests
import time

print('Enter skills that you are not familiar with')
unfamiliar_skills = input('> ')
print(f'Filtering out {unfamiliar_skills}')

def find_jobs():
    html_text = requests.get('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=Android+Development%2CPython&txtLocation=').text
    soup = BeautifulSoup(html_text, 'lxml')
    jobs = soup.find_all('li', class_='clearfix job-bx wht-shd-bx')

    with open('jobs.csv', 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Company Name', 'Required Skills', 'More Info'])

        for index, job in enumerate(jobs):
            published_date = job.find('span', class_='sim-posted').span.text
            if 'few' in published_date:
                company_name = job.find('h3', class_='joblist-comp-name').text.strip()
                skills = job.find('span', class_='srp-skills').text.strip()
                more_info = job.find('h2').a['href']

                if unfamiliar_skills not in skills:
                    writer.writerow([company_name, skills, more_info])

                    print(f'Job saved: {company_name}')

if __name__ == '__main__':
    while True:
        find_jobs()
        time_wait = 10
        print(f'Waiting {time_wait} minutes...')
        time.sleep(time_wait * 60)

        