import requests
from bs4 import BeautifulSoup

URL = 'https://hh.ru/search/vacancy?text=Qa+automation+engineer'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36',
    'Accept': '*/*',
    'Accept-Encoding': 'gzip, deflate, br',
    'Connection': 'keep-alive'
}
def extract_max_page():

    url = f'{URL}&salary=&ored_clusters=true&items_on_page=100&experience=between1And3&enable_snippets=true&excluded_text=java&hhtmFrom=vacancy_search_list&hhtmFromLabel=vacancy_search_line'

    hh = requests.get(url, headers=headers)

    hh_soup = BeautifulSoup(markup=hh.text, features='html.parser')
    paginator = hh_soup.find(name='nav', attrs={'class': 'magritte-number-pages-wrapper___lYp70_4-0-14'})
    pages = paginator.find_all(name='a')
    page_numbers = []
    for page in pages:
      page_numbers.append(page.text)
    return int(page_numbers[-1])

# if __name__ == "__main__":
#     extract_max_page()

def extract_hh_jobs():
    jobs = []
    for page in range(1):
        result = requests.get(url=f'{URL}&excluded_text=java&items_on_page=100', params={'page': 0}, headers=headers)
        soup = BeautifulSoup(markup=result.text, features='html.parser')
        results = soup.find_all(name='div', attrs={'data-sentry-component': 'VacancySearchItem'})
        for result in results:
            job = result.find('a').text
            jobs.append(job)

            print(job)
    print(f'Total number of jobs: {len(jobs)}')



# if __name__ == "__main__":
#     extract_hh_jobs()

def extract_company_name():
    companies = []
    result = requests.get(url=f'{URL}&excluded_text=java&items_on_page=100', params={'page': 0}, headers=headers)
    soup = BeautifulSoup(markup=result.text, features='html.parser')
    results = soup.find_all(name='div', attrs={'data-sentry-component': 'Company'})
    for result in results:
        company = result.find(name='span', attrs={'data-qa': 'vacancy-serp__vacancy-employer-text'}).text
        companies.append(result)

        print(company)

    print(f'Total number of companies: {len(companies)}')

if __name__ == "__main__":
    extract_company_name()

def extract_company_location():
    locations = []
    result = requests.get(url=f'{URL}', params={'page': 0, 'excluded_text': 'java', 'items_on_page': 100, 'enable_snippets': 'true', 'experience': 'between1And3', 'hhtmFrom': 'vacancy_search_list', 'hhtmFromLabel': 'vacancy_search_line'}, headers=headers)
    print(result.url)
    soup = BeautifulSoup(markup=result.text, features='html.parser')
    results = soup.find_all(name='div', attrs={'data-sentry-component': 'Company'})
    for result in results:
        location = result.find(name='span', attrs={'data-qa': 'vacancy-serp__vacancy-employer-text'}).text
        locations.append(location)

        print(location)

    print(f'Total number of locations: {len(locations)}')

# if __name__ == "__main__":
#     extract_company_location()