import requests # Allows to get the html fille
from bs4 import BeautifulSoup   # Allows to use html and grab different data, convert string in object
import pprint 

response = requests.get('https://news.ycombinator.com/news')
soup_object = BeautifulSoup(response.text, 'html.parser')
links = soup_object.select('.storylink')
subtext = soup_object.select('.subtext')


def sort_stories_by_votes(hnlist):

    return sorted(hnlist, key=lambda k:k['votes'], reverse=True)

def create_costum_hn(links, subtext):

    hn = []
    for idx, item in enumerate(links):
        title = links[idx].getText()
        href = links[idx].get('href', None)
        vote = subtext[idx].select('.score')
        if len(vote):
            points = int(vote[0].getText().replace('points', ''))
            if points > 99:
                hn.append({'Title': title, 'Link':href, 'votes': points})
               
    return sort_stories_by_votes(hn)

pprint.pprint(create_costum_hn(links, subtext))