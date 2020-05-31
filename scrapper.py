import requests
from bs4 import BeautifulSoup
from threading import Timer

def get_html(url):
    r = requests.get(url)
    return r.text


# def write_csv(data):
#     with open('data.csv', 'a') as f:
#         writer = csv.writer(f)
#         pass


def get_page_data(html):
    soup = BeautifulSoup(html, 'lxml')
    company = soup.find('table', class_='live').find('tr').find_all('a')[0]
    a_text = soup.find('table', class_='live').find('tr').find_all('a')[1]
    # print(a_text)
    print(company.text)
    print(a_text.text, '\n', company, '\n', a_text) 
    

def main():
    url = 'https://www.e-disclosure.ru/'
    get_page_data(get_html(url))




if __name__ == "__main__":
    main()