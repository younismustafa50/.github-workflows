import requests
from bs4 import BeautifulSoup

print("Script started...")

url = 'https://www.peopleperhour.com/freelance-jobs'
response = requests.get(url)
print(f"HTTP Response Status Code: {response.status_code}")

soup = BeautifulSoup(response.text, 'html.parser')

# Print a snippet of the HTML to verify content
print("HTML snippet:")
print(soup.prettify()[:1000])

# Updated class names based on the provided HTML structure
projects = soup.find_all('li', class_='list__item⤍List⤚2ytmm')

print(f"Found {len(projects)} projects")

for project in projects:
    title_element = project.find('h6', class_='item__title⤍ListItem⤚2FRMT')
    title = title_element.text.strip() if title_element else 'No title found'

    description_element = project.find('p', class_='item__desc⤍ListItem⤚3f4JV')
    description = description_element.text.strip() if description_element else 'No description found'

    print(f"Title: {title}")
    print(f"Description: {description}")
    print("-----")

