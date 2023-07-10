from bs4 import BeautifulSoup
import requests
import time

print('put skills that you are not familiar with')
Unfamiliar_skills = input('>')
print(f'filtering out {Unfamiliar_skills}')

def find_jobs():
    html_text = requests.get('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=Android+Development%2CPython&txtLocation=').text
    soup = BeautifulSoup(html_text, 'lxml')
    jobs = soup.find_all('li', class_='clearfix job-bx wht-shd-bx')
    for index, job in enumerate(jobs):
        published_date = job.find('span', class_='sim-posted').span.text
        if 'few' in published_date:
            company_name = job.find('h3', class_='joblist-comp-name').text.replace(' ', '')
            skills = job.find('span', class_='srp-skills').text.replace(' ', '')
            more_info = job.find('h2').a['href']  # Corrected line

            if Unfamiliar_skills not in skills:
                with open(f'posts/{index}.txt', 'w') as f:
                    print(published_date)
                    f.write(f"company name: {company_name.strip()} \n")
                    f.write(f"Required skills: {skills.strip()} \n")
                    f.write(f"more info: {more_info}")  # Fixed string formatting
                    print(f'file saved: {index}')

if __name__ == '__main__':
    while True:
        find_jobs()
        time_wait = 10
        print(f'waiting {time_wait} minutes...')
        time.sleep(time_wait * 60)