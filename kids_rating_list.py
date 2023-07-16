import requests
from bs4 import BeautifulSoup
import csv

players = []

#Get list of players and USCF IDs
with open('./Static Scraping/SJCC Player List - Sheet4.csv', newline='') as f:
    reader = csv.reader(f)
    data = list(reader)

#Getting latest regular rating
def get_rating(uscf_id):

    url = f'https://www.uschess.org/msa/MbrDtlTnmtHst.php?{uscf_id}'
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    rows_main = soup.find_all('tr')
    table_main = rows_main[3]
    tables_secondary = table_main.find_all('table')
    rating_table = tables_secondary[4]
    rows = rating_table.find_all('tr')

    if rows[0].font:
        for row in rows[2:]:
            cells = row.find_all('td')

            if(len(cells[2].text.strip())):
                rating = cells[2].text.split('>')[1].split('(')[0].strip()
                return rating
    else:
        for row in rows[1:]:
            cells = row.find_all('td')

            if(len(cells[2].text.strip())):
                rating = cells[2].text.split('>')[1].split('(')[0].strip()
                return rating

for i in data[1:]:
    id = i[0]
    name = i[1]
    rating = int(get_rating(id))

    players.append((rating, name))

players.sort(reverse = True)

def update_list():
    with open('Kids_Sorted _List.csv', 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerows(players)

update_list()