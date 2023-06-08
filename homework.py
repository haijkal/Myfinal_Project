import requests
from bs4 import BeautifulSoup


url = "https://en.wikipedia.org/wiki/List_of_the_verified_oldest_people"
print(url)
response = requests.get(url)
print(response)

soup = BeautifulSoup(response.content, 'html.parser')


table = soup.find('table', class_='wikitable')

oldest_person = None
oldest_age = 0

rows = table.find_all('tr')[1:]  # Exclude the header row
for row in rows:
    columns = row.find_all('td')
    name = columns[1].text.strip()
    age_text = columns[0].text.strip()
    birth_date = columns[2].text.strip()

    try:
        age = int(age_text)
        if age > oldest_age:
            oldest_person = name
            oldest_age = age
    except ValueError:
        # Skip rows with invalid age values
        continue

print(f"The oldest person on earth is {oldest_person} at the age of {oldest_age}.")
