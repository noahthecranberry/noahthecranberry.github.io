import requests
from bs4 import BeautifulSoup
import csv


#Get Tournament Links
tournaments1 = []

url = 'https://www.uschess.org/msa/AffDtlTnmtHst.php?A6023036'
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')


rows = soup.find_all('tr')[3].find_all('table')[2].find_all('table')[1].find_all('tr')

for row in rows[2:]:
    cells = row.find_all('td')

    if cells[0].text[0:4] == '2023':

        tournament = cells[1].a['href'] + '.0'

        tournaments1.append(tournament)

    else:
        break

links = []

#Scrape Tournament Page for Player Data
def scrape_tournament_page(tournaments):

    for tournament in tournaments:

        url = f'https://www.uschess.org/msa/{tournament}'
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')

        tables = soup.find_all('pre')

        for table in tables:
            anchors = table.find_all('a')[2:]
                
            for anchor in anchors:
                link = anchor['href']
                    
                if '-00' in link:
                    links.append(link)
        
    return links



def scrape_player_page(player_links):
    final_dictionary = {}

    for player_link in player_links:

        url = f'https://www.uschess.org/msa/{player_link}'
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')

        table = soup.find_all('p')[1]
        rows = table.find_all('tr')

        name = rows[0].a.text
        score = float(rows[3].find_all('td')[1].text)
        
        ini_dictionary1 = final_dictionary
        ini_dictionary2 = {name: score}
        final_dictionary = {x: ini_dictionary1.get(x, 0) + ini_dictionary2.get(x, 0)
                    for x in set(ini_dictionary1).union(ini_dictionary2)}

    return final_dictionary


my_dict = scrape_player_page(scrape_tournament_page(tournaments1))

with open ('highScores.csv', 'w') as f:
    for key in my_dict.keys():
        f.write("%s,%s\n"%(key,my_dict[key]))