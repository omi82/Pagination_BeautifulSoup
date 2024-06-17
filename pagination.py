from bs4 import BeautifulSoup
import requests

root = 'https://subslikescript.com'
website = f'{root}/movies_letter-A'
result = requests.get(website)
content = result.text
soup = BeautifulSoup(content, 'lxml')
# print(soup.prettify())

# Pagination
pagination = soup.find('ul', class_='pagination')
pages = pagination.find_all('li', class_='page-item')
last_page = pages[-2].text

links = []
for page in range(1, int(last_page) + 1)[:2]:  # [1, 139+1]
    page_url = f'{website}?page={page}'
    result = requests.get(page_url)
    content = result.text
    soup = BeautifulSoup(content, 'lxml')

    box = soup.find('article', class_='main-article')
    for link in box.find_all('a', href=True):
        links.append(link['href'])

# print(links)

for link in links:
    try:
        print(link)
        page_url = f'{root}/{link}'
        result = requests.get(page_url)
        content = result.text
        soup = BeautifulSoup(content, 'lxml')

        box = soup.find('article', class_='main-article')
        if box is None:
            print(f"Article with class 'main-article' not found for {page_url}")
            continue

        title = box.find('h1').get_text()
        transcript = box.find('div', class_='full-script').get_text(strip=True, separator='\n')
        # print(transcript)

        # Make the title a safe filename
        safe_title = "".join([c if c.isalnum() else "_" for c in title])

        with open(f'{safe_title}.txt', 'w', encoding='utf-8') as file:
            file.write(transcript)
        print(f'Saved transcript for {title}')

    except Exception as e:
        print('________link not working____________')
        print(link)
        print(f'Error: {e}')


